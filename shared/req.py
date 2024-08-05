import requests
import yaml
import logging

class req:
    def __init__(self) -> None:
        # Load api key and set service url.
        with open("conf.yaml", "r") as file:
            conf = yaml.safe_load(file)
            self.api_key = conf["api_key"]
            match conf["region"]:
                case "europe":
                    self.service_url = "https://europe.api.riotgames.com/"
                case "asia":
                    self.service_url = "https://asia.api.riotgames.com/"
                case "americas":
                    self.service_url = "https://americas.api.riotgames.com/"
            
        logging.debug(f"Requests module initialised. API key: {self.api_key}")
    
    def get_api(self, url: str):
        """Get the response of an API request."""
        resp = requests.get(self.service_url + url, headers={"X-Riot-Token": self.api_key})
        if resp.status_code == 200:
            return resp.json()
        else:
            logging.error(f"API request failed for {url}. Status code: {resp.status_code}")
            raise Exception("API request failed.")
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    r = req()
    print(r.get_api("riot/account/v1/accounts/by-riot-id/LinkLink/GBP"))