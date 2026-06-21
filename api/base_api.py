import requests

from utils.logger import logger

from config .env import config


class BaseAPI:

    def __init__(self):

        self.base_url = config["base_url"]

    def send(self, method, url, **kwargs):

        full_url = self.base_url + url

        logger.info("=" * 50)
        logger.info(f"request url: {full_url}")
        logger.info(f"request method: {method}")

        if kwargs.get("headers"):
            logger.info(
                f"request headers: {kwargs['headers']}"
            )

        if kwargs.get("json"):
            logger.info(
                f"request body: {kwargs['json']}"
            )

        try:

            response = requests.request(
                method=method,
                url=full_url,
                timeout=10,
                **kwargs
            )

            logger.info(
                f"status code: {response.status_code}"
            )

            logger.info(
                f"response body: {response.text}"
            )

            return response

        except Exception as e:

            logger.error(
                f"request error: {e}"
            )

            raise