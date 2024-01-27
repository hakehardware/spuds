import requests
from typing import Dict
from src.utils.logger import logger

BASE_URL = 'https://spacemesh-api-v2.swarmbit.io'
HEADERS = {
    'x-api-key': '90e19edf-bfe3-46ef-89f3-a68fade35632'
}
# Yes there is an API key here. If it is abused then this will be disabled and no one can use it. 

class TTAPI:
    @staticmethod
    async def get_reward_data(account, min_layer) -> Dict:
        LIMIT = 50
        rewards = []
        offset = 0
        layer_met = False
        counter = 0

        if min_layer:
            while not layer_met:
                url = f'{BASE_URL}/account/{account}/rewards?sort=desc&limit={LIMIT}&offset={offset}'

                response = requests.get(url, HEADERS)
                if response.status_code == 200:
                    logger.info('Received Response from Account Rewards API')

                    data = response.json()
                    for entry in data:
                        if entry['layer'] < min_layer:
                            layer_met = True
                            break
                        reward = round(entry['rewards']/1000000000, 2)
                        #logger.info(f'Appending layer {entry["layer"]}')
                        rewards.append({
                            'reward': reward,
                            'reward_string': f'{reward} SMH',
                            'node_id': entry['smesherId'],
                            'layer': entry['layer']
                        })
                else:
                    logger.error('Received Error Connectiong to Rewards API')
                    break
                offset+=50

                if counter > 10:
                    logger.error('Breaking account reward loop as counter has exceeded limit. Max 500 results')
                    break
        else:
            print('No min layer, only running once')
            url = f'{BASE_URL}/account/{account}/rewards?sort=desc&limit={LIMIT}&offset={offset}'
            response = requests.get(url, HEADERS)

            if response.status_code == 200:
                data = response.json()
                rewards.extend(data)
            else:
                logger.error('Received Error Connectiong to Rewards API')

        return rewards