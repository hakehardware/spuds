import json
import os
import traceback

from src.utils.logger import logger
import src.utils.constants as constants
from src.utils.utils import Utils
from datetime import datetime
from typing import Dict

class CMJAPI:

    @staticmethod
    def get_cmj(prefix, smapp, config_dir, config_name_override, public, private) -> Dict:
        # Extract common values

        config_name = 'config.mainnet.json'
        if config_name_override:
            config_name = config_name_override

        if not config_dir:
            logger.error(f'{prefix}: No config dir listed in config.yml')
            return None

        try:
            data = None

            # SMAPP has two configs - the node-config.json is the one that is actually used when a node is running.
            if smapp:
                path = os.path.join(config_dir, 'node-config.json')
                logger.info(f'{prefix}: Getting config from {path}')
                with open(path, 'r') as file:
                    node_config = json.load(file)

            else:
                path = os.path.join(config_dir, config_name)
                logger.info(f'{prefix}: Getting config from {path}')
                with open(path, 'r') as file:
                    node_config = json.load(file)

            data = {
                'cmj_poet_servers': ', '.join(node_config.get('main').get('poet-server', constants.CMJ_DEFAULTS['poet_servers'])), # Get the poet servers and join them
                'cmj_cycle_gap': node_config.get('poet', {}).get('cycle-gap', constants.CMJ_DEFAULTS['cycle_gap']),
                'cmj_phase_shift': node_config.get('poet', {}).get('phase-shift', constants.CMJ_DEFAULTS['phase_shift']),
                'cmj_grpc_public': node_config.get('api', {}).get('grpc-public-listener', constants.CMJ_DEFAULTS['grpc_public']),
                'cmj_grpc_private': node_config.get('api', {}).get('grpc-private-listener', constants.CMJ_DEFAULTS['grpc_private']),
                'cmj_atx_cache_size': node_config.get('cache', {}).get('atx-size', constants.CMJ_DEFAULTS['atx_cache_size']),
                'cmj_min_peers': node_config.get('p2p', {}).get('min-peers', constants.CMJ_DEFAULTS['min_peers']),
                'cmj_low_peers': node_config.get('p2p', {}).get('low-peers', constants.CMJ_DEFAULTS['low_peers']),
                'cmj_high_peers': node_config.get('p2p', {}).get('high-peers', constants.CMJ_DEFAULTS['high_peers']),
                'cmj_data_folder': node_config.get('main', {}).get('data-folder', constants.CMJ_DEFAULTS['data_folder']),
                'cmj_metrics_port': node_config.get('main', {}).get('metrics-port', constants.CMJ_DEFAULTS['metrics_port']),
                'cmj_metrics': node_config.get('main', {}).get('metrics', constants.CMJ_DEFAULTS['metrics']),
                'cmj_inbound_fraction': node_config.get('p2p', {}).get('inbound-fraction', constants.CMJ_DEFAULTS['inbound_fraction']),
                'cmj_outbound_fraction': node_config.get('p2p', {}).get('outbound-fraction', constants.CMJ_DEFAULTS['outbound_fraction']),
                'cmj_smsh_max_file_size': node_config.get('smeshing', {}).get('smeshing-opts', {}).get('smeshing-opts-maxfilesize', constants.CMJ_DEFAULTS['smsh_max_file_size']),
                'cmj_smsh_provider': node_config.get('smeshing', {}).get('smeshing-opts', {}).get('smeshing-opts-provider', constants.CMJ_DEFAULTS['smsh_provider']),
                'cmj_smsh_num_units': node_config.get('smeshing', {}).get('smeshing-opts', {}).get('smeshing-opts-numunits', constants.CMJ_DEFAULTS['smsh_num_units']),
                'cmj_smsh_data_dir': node_config.get('smeshing', {}).get('smeshing-opts', {}).get('smeshing-opts-datadir', constants.CMJ_DEFAULTS['smsh_data_dir']),
                'cmj_smsh_nonces': node_config.get('smeshing', {}).get('smeshing-proving-opts', {}).get('smeshing-opts-proving-nonces', constants.CMJ_DEFAULTS['smsh_nonces']),
                'cmj_smsh_threads': node_config.get('smeshing', {}).get('smeshing-proving-opts', {}).get('smeshing-opts-proving-threads', constants.CMJ_DEFAULTS['smsh_threads']),
                'cmj_smsh_coinbase': node_config.get('smeshing', {}).get('smeshing-coinbase', constants.CMJ_DEFAULTS['smsh_coinbase']),
                'cmj_smsh_started': node_config.get('smeshing', {}).get('smeshing-start', constants.CMJ_DEFAULTS['smsh_started']),
                'cmj_date': datetime.now().strftime("%b %d, %Y %I:%M %p")
            }

            # GRPC was having issues with IP addresses so we are replacing those IPs with localhost.
            Utils.replace_local_host(data, prefix)

            if public:
                logger.info(f'Overriding Public GRPC Address with {public}')
                logger.info(f'Old: {data["cmj_grpc_public"]}')
                data['cmj_grpc_public'] = public
            if private:
                logger.info(f'Overriding Private GPRC Address with {private}')
                logger.info(f'Old: {data["cmj_grpc_private"]}')
                data['cmj_grpc_private'] = private

        except FileNotFoundError as e:
            # Log the exception type and message
            logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"Traceback:\n{traceback_info}")

        except json.JSONDecodeError as e:
            # Log the exception type and message
            logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"Traceback:\n{traceback_info}")

        finally:
            return data