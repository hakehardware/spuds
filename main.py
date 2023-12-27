import argparse
import asyncio
import traceback
import sys

from src.utils.logger import logger
from src.utils.utils import Utils
from src.services.shephard import Shephard
import src.utils.constants as constants

async def run() -> None:
    # Load configs
    config = Utils.read_yaml_file(args.config)
    if config == None:
        logger.error("Empty config. Are you sure the path is right, or that the config was filled out?")
        sys.exit(1)

    logger.info(f'Config Found: {config}')

    try:

        logger.info('Launching Services')
        await asyncio.gather(
            asyncio.create_task(Shephard.herd(config))
        )

    except asyncio.CancelledError:
        logger.info('Shutdown Event Captured. Attempting to shutdown services gracefully.')
        pass

    except Exception as e:
        # Log the exception type and message
        logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

        # Log the traceback information
        traceback_info = traceback.format_exc()
        logger.error(f"Traceback:\n{traceback_info}")

if __name__ == "__main__":
    logger.info(f'Starting Spuds {constants.VERSION}')

    # Configure argparse
    parser = argparse.ArgumentParser(description='Spuds is the best way to monitor and track your Spacemesh nodes!')
    parser.add_argument('-c', '--config', type=str, required=True, help='Path to the configuration file')

    # Get args
    args = parser.parse_args()

    try:
        asyncio.run(run())

    except KeyboardInterrupt:
        pass

    except Exception as e:
        # Log the exception type and message
        logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

        # Log the traceback information
        traceback_info = traceback.format_exc()
        logger.error(f"Traceback:\n{traceback_info}")

    logger.info('All services shutdown. Exiting')