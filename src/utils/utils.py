import os
import yaml

from src.utils.logger import logger
from dateutil import tz as dateutil_tz
from datetime import datetime, timedelta, timezone

class Utils:
    @staticmethod
    def read_yaml_file(file_path):
        logger.info(f'Opening config from {file_path}')
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'r') as file:
            try:
                data = yaml.safe_load(file)
                return data
            except yaml.YAMLError as e:
                print(f"Error reading YAML file: {e}")
                return None
            
    @staticmethod
    def replace_local_host(data, prefix):
        logger.info(f'{prefix}: Replacing 0.0.0.0 and 127.0.0.1 with localhost')
        if '0.0.0.0' in data['cmj_grpc_public']:
            data['cmj_grpc_public'] = data['cmj_grpc_public'].replace('0.0.0.0', 'localhost')

        if '127.0.0.1' in data['cmj_grpc_public']:
            data['cmj_grpc_public'] = data['cmj_grpc_public'].replace('127.0.0.1', 'localhost')

        if '0.0.0.0' in data['cmj_grpc_private']:
            data['cmj_grpc_private'] = data['cmj_grpc_private'].replace('0.0.0.0', 'localhost')

        if '127.0.0.1' in data['cmj_grpc_private']:
            data['cmj_grpc_private'] = data['cmj_grpc_private'].replace('127.0.0.1', 'localhost')

    @staticmethod
    def get_date(data):

        # Define UTC and your local time zone
        utc_zone = dateutil_tz.tzutc()
        local_zone = dateutil_tz.tzlocal()

        # Remove the fractional seconds and 'Z' from the input string
        data = data.split('.')[0]
        data = data.rstrip('Z')

        # Convert the input string to a datetime object with UTC time zone
        utc_datetime = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S")
        utc_datetime = utc_datetime.replace(tzinfo=utc_zone)

        # Convert the UTC datetime to the local time zone
        local_datetime = utc_datetime.astimezone(local_zone)

        return local_datetime.strftime("%b %d, %Y %H:%M:%S")
    
    @staticmethod
    def calculate_layer_date(layer):
        # Hardcoded start date "2023-07-14T08:00:00Z"
        start_date_str = "2023-07-14T08:00:00Z"

        # Convert the input string to a datetime object
        start_date = datetime.strptime(start_date_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

        # Calculate the future date by adding the specified number of 5-minute intervals
        future_date = start_date + timedelta(minutes=layer*5)

        to_zone = dateutil_tz.tzlocal()

        current_date_local = datetime.now()

        current_date_local = current_date_local.astimezone(to_zone)
        layer_time_local = future_date.astimezone(to_zone)

        minutes = (layer_time_local - current_date_local).total_seconds() / 60
        if minutes > 0:
            timer_string = Utils.format_minutes_to_hours_and_minutes(minutes)
        else:
            timer_string = '0h 0m'

        status = 'Waiting' if minutes > 0 else 'Completed'

        return {
            'layer': layer,
            'layer_time_local': layer_time_local.strftime("%b %d, %Y %H:%M:%S"),
            'timer_string': timer_string,
            'minutes': int(minutes),
            'status': status
        }
    
    @staticmethod
    def format_minutes_to_hours_and_minutes(total_minutes):
        hours = total_minutes // 60
        minutes = total_minutes % 60

        return f'{int(hours)}h {int(minutes)}m'