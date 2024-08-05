class account_entity:
    def __init__(self, puuid, game_name, tag_line):
        self.puuid = puuid
        self.game_name = game_name
        self.tag_line = tag_line
        
    def __init__(self, json):
        self.puuid = json["puuid"]
        self.game_name = json["gameName"]
        self.tag_line = json["tagLine"]
        
    def __str__(self):
        return f"{self.game_name}#{self.tag_line}"
