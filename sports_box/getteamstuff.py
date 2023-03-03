# team stuff
import pandas
import numpy as np

# import userprofile
from IPython.display import display
from nba_api.stats.static import teams
from nba_api.stats.endpoints import teaminfocommon


def getTeam(team):
    t = teams.find_team_by_abbreviation(team)
    # get team logo
    id = list(t.items())[0][1]
    load = teaminfocommon.TeamInfoCommon(team_id=id, season_nullable="2022-23")
    teaminfo = load.team_info_common.get_data_frame()
    # teaminfo = load.team_info_common.get_dict()

    # return teaminfo.loc[0]
    return teaminfo


getTeam("mil")
