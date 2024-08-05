import json
from shared.req import req
from shared.entity import account_entity

class account:
    def __init__(self) -> None:
        self.req_service = req()
    
    def get_account(self, game_name: str, tag_line: str):
        """Get the puuid of a player by their game name and tag line (Example#EUW)."""
        resp = self.req_service.get_api(f"riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}")
        return account_entity(resp)
        
if __name__ == "__main__":
    a = account()
    print(a.get_account("LinkLink", "GBP"))
    