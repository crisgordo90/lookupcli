import requests
import logging
import json
import time

MAX_RETRIES = 2
BASE_WAITING_TIMER = 1


class RequestHandler:
    @staticmethod
    def log_and_sleep(error_msg: str, minutes: int):
        """
        Logs any error and waits for an amount of minutes
        :param error_msg: Log any specific error failure
        :param minutes: time in minutes
        """
        logging.exception(error_msg)
        logging.error("Retrying the request in %s minutes", minutes)
        time.sleep(minutes * 60)

    def lookup_info(self, url: str, ip: str):
        """
        Fetch the look up info for the given IP
        :param url: The url to lookup the ip info
        :param ip: Lookup a ip that has not been previously used
        :return: The dictionary of the lookup info for the given IP
        """
        retries_attempts = 0
        waiting_timer = BASE_WAITING_TIMER
        while retries_attempts < MAX_RETRIES:
            try:
                response = requests.get(f"{url}/{ip}")
                json_text = response.text
                return json.loads(json_text)
            except Exception as e:
                retries_attempts += 1
                waiting_timer += waiting_timer // 2
                logging.error("The data requested to the API was not found")
                self.log_and_sleep(e, waiting_timer)
        raise Exception("We were not able to fetch the info from the ip s%", ip)
