import asyncio
import json

from src.utils.logger import logger
from typing import Dict
from src.apis.cmjapi import CMJAPI
from src.apis.grpcapi import GRPCAPI
from src.apis.ttapi import TTAPI

class Aggregator:
    async def scrape(node_config):
        config_dir, smapp, name = node_config['config_dir'], node_config['smapp'], node_config['name']
        prefix = f'[{name}]'

        logger.info(f'{prefix}: Starting Scraper...')

        cmj = CMJAPI.get_cmj(prefix, smapp, config_dir)
        # logger.info(json.dumps(cmj, indent=4))

        if not cmj:
            logger.error(f'{prefix}: Failed to get CONFIG. Skipping node.')
            return None
        
        grpc = await GRPCAPI.get_grpc(cmj['cmj_grpc_private'], cmj['cmj_grpc_public'], prefix)
        # logger.info(json.dumps(grpc, indent=4))

        return {
            'cmj': cmj,
            'grpc': grpc,
            'node_name': name
        }

    async def run(config) -> Dict:
        logger.info('Running Aggregator Service')
        
        tasks = [Aggregator.scrape(node) for node in config['nodes']]
        data = await asyncio.gather(*tasks)

        # Remove any nodes with no data
        filtered_list = [value for value in data if value is not None]

        return filtered_list
        