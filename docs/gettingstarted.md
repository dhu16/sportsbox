# Getting Started/Examples


## Installation

`pip install sports-box`

<h3> General Usage </h3>

```python

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

```

</br>

<h3> Discord Bot Commands </h3>

`!nbanews` - Shows 5 random recent NBA news articles

`!nflnews` - Shows 5 random recent NFL news articles

`!nbascores` - Shows today's NBA box scores

`!nbavids` - Shows 5 recent NBA Tiktoks

`!nflvids` - Shows 5 recent NFL Tiktoks