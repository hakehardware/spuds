import json

from src.utils.logger import logger
from src.utils.utils import Utils
from src.apis.ttapi import TTAPI

class Normalizer:
    # ====== ACCOUNTS
    @staticmethod
    def accounts(data):
        # Get the reward coinbases that are associated with the host
        accounts = []
        for node in data:
            reward_coinbase = node.get('grpc', {}).get('reward_coinbase', None)
            if reward_coinbase not in accounts:
                accounts.append(reward_coinbase)

        return accounts
    
    # ====== LAYERS
    @staticmethod
    def add_layer_data(data):
        # Get data for all the layers
        logger.info('Adding supplemental data to layers.')

        layers = []
        for node in data:
            for layer in node['grpc']['assigned_layers']:
                response = Utils.calculate_layer_date(layer)
                response['reward_coinbase'] = node['grpc']['reward_coinbase']
                response['node_id'] = node['grpc']['node_id']['grpc_node_id']
                response['node_name'] = node['node_name']
                layers.append(response)

        return layers
    
    @staticmethod
    def divide_layers_by_account(layers):
        # Divide layers by account
        logger.info('Sorting layers by account to get min layer')

        accounts = {}
        for layer in layers:
            if not accounts.get(layer['reward_coinbase'], None):
                accounts[layer['reward_coinbase']] = {
                    'layers': [],
                    'account': layer['reward_coinbase']
                }

            accounts[layer['reward_coinbase']]['layers'].append(layer)

        return accounts
    
    @staticmethod
    async def get_reward_details(accounts):
        all_layers = []
        # For each account, find the lowest layer, then join with reward results
        logger.info('Getting reward details for each account and the corresponding layers')

        for value in accounts.values():
            min_layer = min(value['layers'], key=lambda x: x['layer'])
            rewards = await TTAPI.get_reward_data(value['account'], min_layer['layer'])

            for layer in value['layers']:
                match = None
                for reward in rewards:
                    if reward['layer'] == layer['layer'] and reward['node_id'] == layer['node_id']:
                        match = reward
                        break

                # If there is a match then that means a reward was received, so update status and add reward amount
                if match:
                    layer['reward_string'] = match['reward_string']
                    layer['status'] = 'Received'

                # If there was not a match, and the layer has passed, then the reward may have been missed. There is a 2 minute buffer
                elif not match and layer['minutes'] < -2:
                    layer['status'] = 'Missed'
                    layer['reward_string'] = '0 SMH'
                # Otherwise we are still just waitin for the layer to occur. 
                else:
                    layer['reward_string'] = 'Waiting'

                all_layers.append(layer)

        return all_layers

    @staticmethod
    async def normalize_layers(data):
        # Calculates layer date and adds supplemental data to layers such a reward_coinbase and node_id
        # Then uses TTAPI to grab reward details to determine reward amount + if a reward was missed or is pending

        # Add supplemental data to layers
        layers = Normalizer.add_layer_data(data)

        # Divide layers by account so we can then get min layer 
        accounts = Normalizer.divide_layers_by_account(layers)

        # For each account, find the lowest layer, then join with reward results
        normalized_layers = await Normalizer.get_reward_details(accounts)

        return normalized_layers

    # ======= NODES
    def nodes(data):
        nodes = []
        for node in data:
            nodes.append({
                'node_name': node['node_name'],
                'node_id': node.get('grpc', {}).get('node_id', {}).get('grpc_node_id_base64', None),
                'online': node.get('grpc', {}).get('online', False),
                'synced': node.get('grpc', {}).get('node_status', {}).get('grpc_is_synced', False),
                'smeshing': node.get('grpc', {}).get('is_smeshing', False),
                'synced_layer': node.get('grpc', {}).get('node_status', {}).get('grpc_synced_layer', 0),
            })

        return nodes
            

    @staticmethod
    async def normalize(data):
        accounts = Normalizer.accounts(data)
        normalized_layers = await Normalizer.normalize_layers(data)
        nodes = Normalizer.nodes(data)

        return {
            'accounts': accounts,
            'layers': normalized_layers,
            'nodes': nodes
        }