<h1> sportsbox </h1>

<p>Discord bot displaying sports news and convenient stats. </p>


![](https://img.shields.io/badge/license-Apache--2.0-brightgreen)
![](https://img.shields.io/github/issues/dhu16/sportsbox)
[![Build Status](https://github.com/dhu16/sportsbox/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/dhu16/sportsbox/actions?query=workflow%3A%22Build+Status%22)
[![codecov](https://codecov.io/gh/dhu16/sportsbox/branch/main/graph/badge.svg?token=UHT46NYQGX)](https://codecov.io/gh/dhu16/sportsbox)
[![PyPI](https://img.shields.io/pypi/v/sports-box)](https://pypi.org/project/sports-box/)

<h2> Overview </h2>

<p> This Discord bot allows users to view NBA and NFL news, scores, and stats on their servers with easy commands. I always found it annoying to constantly search up stats for a game I was monitoring while studying and I was too lazy to install official apps too. This alleviates the inconvenience of always having to manually search up stats or open one's phone while working or playing games with friends as Discord is usually always open on someone's computer.  </p>

</br>

## Installation

`pip install sportsbox`

<h3> Usage </h3>

```py

from sportsbox import showUpcomingGames, getPlayer, playerStats, playerNextNGames, getTeam, getScores, getNBANews, getNFLNews

#Get basic player information and career regular season stats returned as dataframes
player_info_df = getPlayer("Lebron James")
player_stats_df = playerStats("Lebron James")

#Show upcoming next N games for a player as a matplotlib plot
showUpcomingGames("Lebron James", 3)

#Get upcoming next N games with more details for a player returned as a dataframe
player_games_df = playerNextNGames("Lebron James", "3")

#Get basic team information returned as dataframe
team_info_df = getTeam("mil")

#Get today's NBA box scores returned as a list of Game objects
today_scores = getScores()

#Get 5 recent NBA or NFL articles returned as set of Article objects
nbanews = getNBANews()
nflnews = getNFLNews()

```

## Game class attributes
Attribute Variable | Value |
------------ | :-----------: |
gameStatus | `1` not started, `2` in progress, `3` finished |
gameStatusText | `start time (ET)`, `Qx and time remaining`, `FINAL`  | 
homeTeam | EX: `LAL` | 
hWins | home team wins | 
hLosses | home team losses | 
hScore | home team's current score | 
awayTeam | EX: `LAC` | 
aWins | away team wins |
aLosses | away team losses |
aScore | away team's current score |


## Article class attributes
Attribute Variable | Value |
------------ | :-----------: |
headline | headline of the ESPN article |
description | description of the ESPN article | 
link | link to ESPN article | 


</br>

## Invite as Discord bot 

Invite [sportsbox](https://discord.com/api/oauth2/authorize?client_id=1089389802840920195&permissions=2147576832&scope=bot) to your Discord server!

<h3> Commands </h3>

`!nbanews` - Shows 5 random recent NBA news articles

`!nflnews` - Shows 5 random recent NFL news articles

`!nbascores` - Shows today's NBA box scores

</br>

## Development

Read [CONTRIBUTING.md](CONTRIBUTING.md) file


