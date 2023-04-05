# fantasy data
"""
from espn_api.football import League

# extra parameters to access my private fantasy football league
sw_id = '{}'
espns2 = (
)


# Helper function to get user's fantasy team - case sensitive
def getMyTeam(teamname):
    lg = League(league_id=1088987341, year=2022, espn_s2=espns2, swid=sw_id)
    myteam = ""
    for t in lg.teams:
        if t.team_name == teamname:
            myteam = t
            break

    return myteam


# Get user's fantasy roster
def myRoster(teamname):
    myteam = getMyTeam(teamname)
    return myteam.roster


myRoster("Handoff Hu")
# print(getMyTeam("Handoff Hu"))

"""
