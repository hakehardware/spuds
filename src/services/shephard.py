import asyncio
import traceback

from src.utils.logger import logger
from src.services.aggregator import Aggregator
from src.services.normalizer import Normalizer
from src.services.publisher import Publisher
import src.utils.constants as constants
from prometheus_client import start_http_server

class Shephard:


    @staticmethod
    async def herd(config) -> None:
        logger.info('Starting Shephard Service')

        logger.info(f'Starting prometheus client http server on port {config["prometheus_client_port"]}')
        start_http_server(config["prometheus_client_port"])

        publisher = Publisher()

        while True:
            try:
                data = await Aggregator.run(config)
                n_data = await Normalizer.normalize(data)

                logger.info('Initialized Publisher')
                publisher.publish(n_data)

                logger.info(f'Shephard Complete. Waiting {constants.REFRESH_RATE} seconds.')

            except Exception as e:
                # Log the exception type and message
                logger.error(f"Exception type: {type(e).__name__}, Message: {str(e)}")

                # Log the traceback information
                traceback_info = traceback.format_exc()
                logger.error(f"Traceback:\n{traceback_info}")

                break
            await asyncio.sleep(constants.REFRESH_RATE)
