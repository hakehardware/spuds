from prometheus_client import Gauge
from src.utils.logger import logger

class Publisher:
    def __init__(self) -> None:
        # Aggregates
        self.node_assigned_layers_gauge = Gauge('node_assigned_layers', 'Assigned layers for all nodes', labelnames=['node_name', 'node_id', 'coinbase', 'status', 'date', 'timer', 'reward'])
        self.node_spuds_online_gauge = Gauge('node_spuds_online_gauge', 'Spuds Online (Online/Offline)', labelnames=['app'])
        
        # Node Online State
        self.node_online_gauge = Gauge('node_online', 'Denotes if a node is online', labelnames=['node_id', 'node_name', 'state'])
        self.node_offline_gauge = Gauge('node_offline', 'Denotes if a node is offline', labelnames=['node_id', 'node_name', 'state'])

        # Node Sync State
        self.node_synced_gauge = Gauge('node_synced', 'Denotes if a node is synced', labelnames=['node_id', 'node_name', 'state'])
        self.node_not_synced_gauge = Gauge('node_not_synced', 'Denotes if a node is not synced', labelnames=['node_id', 'node_name', 'state'])

        # Node Smeshing State
        self.node_smeshing_gauge = Gauge('node_smeshing', 'Denotes if a node is smeshing', labelnames=['node_id', 'node_name', 'state'])
        self.node_not_smeshing_gauge = Gauge('node_not_smeshing', 'Denotes if a node is not smeshing', labelnames=['node_id', 'node_name', 'state'])

        # Node Synced Layer
        self.node_synced_layer = Gauge('node_synced_layer', 'Denotes the synced layer for a node', labelnames=['node_id', 'node_name'])


    def publish(self, data):
        self.node_assigned_layers_gauge.clear()
        self.node_spuds_online_gauge.labels('Spuds').set(1)

        for layer in data['layers']:
            self.node_assigned_layers_gauge.labels(
                node_name=layer['node_name'], 
                node_id=layer['node_id'], 
                coinbase=layer['reward_coinbase'], 
                status=layer['status'], 
                date=layer['layer_time_local'], 
                timer=layer['timer_string'], 
                reward=layer['reward_string']).set(int(layer['layer'])
            )

        for node in data['nodes']:
            node_name = node['node_name']
            node_id = node['node_id']

            online = 1 if node['online'] else 0
            offline = 0 if node['online'] else 1

            synced = 1 if node['synced'] else 0
            not_synced = 0 if node['synced'] else 1

            smeshing = 1 if node['smeshing'] else 0
            not_smeshing = 0 if node['smeshing'] else 1

            synced_layer = node['synced_layer']

            self.node_online_gauge.labels(node_id=node_id, node_name=node_name, state="online").set(online)
            self.node_offline_gauge.labels(node_id=node_id, node_name=node_name, state="offline").set(offline)

            self.node_synced_gauge.labels(node_id=node_id, node_name=node_name, state="synced").set(synced)
            self.node_not_synced_gauge.labels(node_id=node_id, node_name=node_name, state="not synced").set(not_synced)

            self.node_smeshing_gauge.labels(node_id=node_id, node_name=node_name, state="smeshing").set(smeshing)
            self.node_not_smeshing_gauge.labels(node_id=node_id, node_name=node_name, state="not smeshing").set(not_smeshing)
            
            self.node_synced_layer.labels(node_id=node_id, node_name=node_name).set(synced_layer)


