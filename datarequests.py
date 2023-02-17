from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
#from nbaHeadshots import getHeadshotById, getAllHeadshots

def getPlayer(player):

    p = players.find_players_by_full_name(player)
    d = p[0]
    #getHeadshotById(id)
    id = list(d.items())[0][1]
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=id)

    print(player_info.get_json())


getPlayer("Lebron James")