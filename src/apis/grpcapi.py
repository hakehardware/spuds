import asyncio
import traceback
import binascii
import base64

from src.utils.logger import logger
from src.libs.grpc_lib import ActivationClient, AdminClient, NodeClient, SmesherClient, CheckOnline, MeshClient
from typing import Dict
from src.utils.utils import Utils

class GRPCAPI:
    @staticmethod
    async def check_online(ip) -> Dict:
        try:
            online = await asyncio.to_thread(CheckOnline.check_online, ip)
            return online
        except Exception as e:
            # Log the exception type and message
            logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"Traceback:\n{traceback_info}")
            return False
        
    @staticmethod
    async def get_highest_atx(ip) -> Dict:
        try:
            activation_client = ActivationClient(ip)
            results = await asyncio.to_thread(activation_client.get_highest_atx)

            return results
        
        except Exception as e:
            # Log the exception type and message
            logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"Traceback:\n{traceback_info}")

            return None

    @staticmethod
    async def get_version(ip) -> Dict:
        try:
            node_client = NodeClient(ip)
            results = await asyncio.to_thread(node_client.get_version)

            return results
        
        except Exception as e:
            # Log the exception type and message
            logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"Traceback:\n{traceback_info}")

            return None
        
    @staticmethod
    async def get_build(ip) -> Dict:
        try:
            node_client = NodeClient(ip)
            results = await asyncio.to_thread(node_client.get_build)

            return results
        
        except Exception as e:
            # Log the exception type and message
            logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"Traceback:\n{traceback_info}")

            return None

    @staticmethod
    async def get_node_status(ip) -> Dict:
        try:
            node_client = NodeClient(ip)
            results = await asyncio.to_thread(node_client.get_node_status)

            data = {
                'grpc_peers': results.get("status", {}).get("connectedPeers", "None"),
                'grpc_is_synced': results.get("status",  {}).get("isSynced", False),
                'grpc_synced_layer': results.get("status",  {}).get("syncedLayer",  {}).get("number", "0"),
                'grpc_top_layer': results.get("status",  {}).get("topLayer",  {}).get("number", "0"),
                'grpc_verified_layer': results.get("status",  {}).get("verifiedLayer",  {}).get("number", "0"),
            }

            return data
        
        except Exception as e:
            # Log the exception type and message
            logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"Traceback:\n{traceback_info}")

            return None

    @staticmethod
    async def get_current_epoch(ip) -> Dict:
        try:
            mesh_client = MeshClient(ip)
            results = await asyncio.to_thread(mesh_client.get_current_epoch)

            return results.get('epochnum', {}).get('number', None)

        except Exception as e:
            # Log the exception type and message
            logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"Traceback:\n{traceback_info}")

            return None

    @staticmethod
    async def get_node_info(ip) -> Dict:
        try:
            node_client = NodeClient(ip)
            results = await asyncio.to_thread(node_client.get_node_info)

            data = {
                'grpc_first_genesis': results.get("firstGenesis", "0"),
                'grpc_epoch_size': results.get("epochSize", "0"),
                'grpc_effective_genesis': results.get("effectiveGenesis", "0")
            }

            return data
        except Exception as e:
            # Log the exception type and message
            logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"Traceback:\n{traceback_info}")
            return None
        
    @staticmethod
    async def get_is_smeshing(ip) -> Dict:
        try:
            smesher_client = SmesherClient(ip)
            results = await asyncio.to_thread(smesher_client.get_is_smeshing)

            return results.get('isSmeshing', None)

        except Exception as e:
            # Log the exception type and message
            logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"Traceback:\n{traceback_info}")

            return None

    @staticmethod
    async def get_node_id(ip) -> Dict:
        try:
            smesher_client = SmesherClient(ip)
            results = await asyncio.to_thread(smesher_client.get_smesher_id)
            node_id = results.get("publicKey", None)
            data = None

            if node_id:
                base64_bytes = base64.b64decode(node_id)
                node_id_hex = binascii.hexlify(base64_bytes).decode('utf-8')

                data = {
                    'grpc_node_id_base64': node_id,
                    'grpc_node_id': node_id_hex,
                }
        
        except Exception as e:
            # Log the exception type and message
            logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"Traceback:\n{traceback_info}")

        finally:
            return data

    @staticmethod
    async def get_reward_coinbase(ip) -> Dict:
        try:
            smesher_client = SmesherClient(ip)
            results = await asyncio.to_thread(smesher_client.get_coinbase)

            return results.get("accountId", {}).get("address", None)
        
        except Exception as e:
            # Log the exception type and message
            logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"Traceback:\n{traceback_info}")

            return None
        
    @staticmethod
    async def get_event_stream(ip) -> Dict:
        try:
            admin_client = AdminClient(ip)
            results = await asyncio.to_thread(admin_client.get_event_stream)
            assigned_layers = None
            events = []

            for event in results:
                eligibilities = event.get("eligibilities", None)
                poetwaitproof = event.get("poetWaitProof", None)
                beacon = event.get("beacon", None)
                init_start = event.get("initStart", None)
                init_complete = event.get("initComplete", None)

                if eligibilities is not None:
                    layers = [item['layer'] for item in eligibilities['eligibilities'] for _ in range(item['count'])]
                    events.append({
                        'grpc_event_event_name': 'Layer Eligibilities',
                        'grpc_event_message': f'{event["help"]}, {eligibilities["epoch"]}, {layers}',
                        'grpc_event_date': Utils.get_date(event['timestamp']),
                    })

                    assigned_layers = layers
                    
                elif poetwaitproof is not None:
                    events.append({
                        'grpc_event_event_name': 'PoET Wait Proof',
                        'grpc_event_message': f'{event["help"]}, Target Epoch {event["poetWaitProof"]["target"]}, Publish Epoch {event["poetWaitProof"]["publish"]}, Wait {int(event["poetWaitProof"]["wait"].split(".")[0])}',
                        'grpc_event_date': Utils.get_date(event['timestamp']),
                    })

                elif beacon is not None:
                    events.append({
                        'grpc_event_event_name': 'Beacon',
                        'grpc_event_message': f'{event["help"]}, Epoch {event["beacon"]["epoch"]}',
                        'grpc_event_date': Utils.get_date(event['timestamp']),
                    })

                elif init_start is not None:
                    events.append({
                        'grpc_event_event_name': 'PoST Data Initialization',
                        'grpc_event_message': f'{event["help"]}, Node ID {event["initStart"]["smesher"]}, ATX {event["initStart"]["commitment"]}',
                        'grpc_event_date': Utils.get_date(event['timestamp']),
                    })

                elif init_complete is not None:
                    events.append({
                        'grpc_event_event_name': 'PoST Data Initialization Completed',
                        'grpc_event_message': event["help"],
                        'grpc_event_date': Utils.get_date(event['timestamp']),
                    })
                    
                else:
                    events.append({
                        'grpc_event_event_name': 'Untracked Event',
                        'grpc_event_message': str(event),
                        'grpc_event_date': Utils.get_date(event['timestamp']),
                    })
            return {
                'grpc_events': events,
                'assigned_layers': assigned_layers
            }

        except Exception as e:
            # Log the exception type and message
            logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"Traceback:\n{traceback_info}")
            return False

    @staticmethod
    async def get_post_setup_status(ip) -> Dict:
        try:
            smesher_client = SmesherClient(ip)
            results = await asyncio.to_thread(smesher_client.get_post_setup_status)

            post_state = results.get("status",  {}).get("state", None)
            post_data_dir = results.get("status",  {}).get("opts",  {}).get("dataDir", None)
            provider_id = results.get("status",  {}).get("opts",  {}).get("providerId", None)
            max_file_size = results.get("status",  {}).get("opts",  {}).get("maxFileSize", None)
            space_units = results.get("status",  {}).get("opts",  {}).get("numUnits", 0)
            max_file_size_gib = int(int(max_file_size) / 1024**3) if max_file_size else 0
            size_gib = space_units * 64 if space_units > 0 else 0

            data = {
                'grpc_max_file_size_gib': max_file_size_gib,
                'grpc_max_file_size_gib_string': f'{max_file_size_gib} GiB',
                'grpc_space_units': space_units,
                'grpc_size_gib': size_gib,
                'grpc_size_gib_string': f'{size_gib} GiB',
                'grpc_post_state': post_state,
                'grpc_post_data_dir': post_data_dir,
                'grpc_provider_id': provider_id
            }

            return data
        except Exception as e:
            # Log the exception type and message
            logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"Traceback:\n{traceback_info}")

            return None

    @staticmethod
    async def get_grpc(private, public, prefix) -> Dict:
        try:
            logger.info(f'{prefix}: Getting grpc data for {private} and {public}')
            data = None

            online = await GRPCAPI.check_online(public)

            if not online:
                logger.warn(f'{prefix}: GRPC Server is offline. Node may still be initializing')
                data = {}
            else:
                tasks = [
                    GRPCAPI.get_highest_atx(public),
                    GRPCAPI.get_version(public),
                    GRPCAPI.get_build(public),
                    GRPCAPI.get_node_status(public),
                    GRPCAPI.get_current_epoch(public),
                    GRPCAPI.get_is_smeshing(private),
                    GRPCAPI.get_node_id(private),
                    GRPCAPI.get_reward_coinbase(private),
                    GRPCAPI.get_post_setup_status(private),
                    GRPCAPI.get_event_stream(private)
                ]

                [highest_atx, version, build, node_status, current_epoch, is_smeshing, node_id, reward_coinbase, post_setup_status, event_stream] = await asyncio.gather(*tasks)

                events = event_stream.get('grpc_events', {})
                assigned_layers = event_stream.get('assigned_layers', [])

                data = {
                    'online': True,
                    'highest_atx': highest_atx,
                    'version': version,
                    'build': build,
                    'node_status': node_status,
                    'current_epoch': current_epoch,
                    'is_smeshing': is_smeshing,
                    'node_id': node_id,
                    'reward_coinbase': reward_coinbase,
                    'post_setup_status': post_setup_status,
                    'events': events,
                    'assigned_layers': assigned_layers
                }
        
        except Exception as e:
            # Log the exception type and message
            logger.error(f"{prefix}: Exception type: {type(e).__name__}, Message: {str(e)}")

            # Log the traceback information
            traceback_info = traceback.format_exc()
            logger.error(f"{prefix}: Traceback:\n{traceback_info}")
        
        finally:
            return data
