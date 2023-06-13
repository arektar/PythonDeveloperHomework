from config import Config
import requests
import json
from typing import Optional


class LangModel(object):
    def __init__(self):
        self.root_url = Config.LANGMOD_SERVICE_URL
        self.token = Config.LANGMOD_SERVICE_TOKEN

    def get_url(self, method: str) -> str:
        url = self.root_url + \
              "/api/l3m/" + method + \
              "?llm_type=gigachat" + \
              "&t=0.7" + \
              "&tp=0.2" + \
              "&token=" + self.token

        return url

    def chat(self, messages: list[dict]) -> Optional[str]:
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        url = self.get_url('chat')
        data = json.dumps(messages)

        resp = requests.post(url, headers=headers, data=data)
        parsed = self.parse_resp(resp)
        if parsed:
            return parsed["answer"]

    def parse_resp(self, response: requests.Response) -> Optional[dict]:
        parsed = None
        if response.status_code == 200 and response.text:
            parsed = json.loads(response.text)
        else:
            print("LangModel bad request")
            print(f"Code: {response.status_code}")
            print(f"Body: {response.text}")
            if Config.ERRORS_RISING:
                raise NameError(f"Bad Lang Model responce. Code: {response.status_code} Body: {response.text}")

        return parsed
