import os
import requests
import json
from werkzeug.exceptions import BadRequest


class EventbriteDispatcher:
    EVENTBRITE_URL = 'https://www.eventbriteapi.com/v3'

    def __check_api_token(self):
        if not self.api_token:
            raise BadRequest("Cannot send request to Eventbrite.")

    def __init__(self):
        self.api_token = os.environ['API_TOKEN_EVENTBRITE']
        self.__check_api_token()

    def get_all_events(self):
        self.__check_api_token()
        headers = {
            "Authorization": f'Bearer {self.api_token}'
        }
        params = {
            "page_size": 6,
            "order_by": "start_desc"
        }
        events = requests.get(url=f'{self.EVENTBRITE_URL}/users/me/events/', headers=headers, params=params)
        if events.status_code != 200:
            raise BadRequest("Response from Eventbrite no successfull.")
        json_events = events.content.decode('utf8')
        ret_json = json.loads(json_events)
        return ret_json
