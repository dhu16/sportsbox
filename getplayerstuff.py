#favorite player data
import pandas
import numpy as np
import userprofile
from IPython.display import display
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import PlayerNextNGames
#from nbaHeadshots import getHeadshotById, getAllHeadshots

def getPID(player): #helper function to get player ID
    p = players.find_players_by_full_name(player)
    d = p[0]
    id = list(d.items())[0][1]

    return id

def getPlayer(player): #use this basic info to build player profile page

    #getHeadshotById(id)
    id = getPID(player)
    load = commonplayerinfo.CommonPlayerInfo(player_id=id)
    playerinfo = load.common_player_info.get_data_frame()

    display(playerinfo.loc[0])


def playerStats(player): #show career stats of player

    id = getPID(player)
    load = playercareerstats.PlayerCareerStats(player_id=id)
    stats = load.career_totals_regular_season.get_data_frame()
    stats.style.set_caption(player + "'s Stats")

    display(stats) #horizontal stats


def playerNextNGames(player, n): #show next n games for player

    s = str(n)
    id = getPID(player)
    load = PlayerNextNGames(number_of_games=s, player_id=id, season_all="2022-23",season_type_all_star="Regular Season")
    upcoming = load.next_n_games.get_data_frame()
    upcoming.style.set_caption(player + "'s Upcoming " + s + " Games")

    display(upcoming.to_string())

#getPlayer("Lebron James")
#playerStats("Lebron James")
#playerNextNGames("Lebron James", 3)