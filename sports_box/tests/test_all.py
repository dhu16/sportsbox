# tests
from sports_box import getMyTeam, getPID, myRoster, getPlayer, playerStats, playerNextNGames, getTeam, getTName
from unittest.mock import patch
from typing import List
import pytest
import pandas as pd


def test_first():
    assert getPID("Lebron James") == 2544


def test_getplayer():
    # dfcolumns = ['PERSON_ID', 'FIRST_NAME', 'LAST_NAME', 'DISPLAY_FIRST_LAST', 'DISPLAY_LAST_COMMA_FIRST', 'DISPLAY_FI_LAST', 'PLAYER_SLUG', 'BIRTHDATE', 'SCHOOL', 'COUNTRY', 'LAST_AFFILIATION', 'HEIGHT', 'WEIGHT', 'SEASON_EXP', 'JERSEY', 'POSITION', 'ROSTERSTATUS', 'GAMES_PLAYED_CURRENT_SEASON_FLAG', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CODE', 'TEAM_CITY', 'PLAYERCODE', 'FROM_YEAR', 'TO_YEAR', 'DLEAGUE_FLAG', 'NBA_FLAG', 'GAMES_PLAYED_FLAG', 'DRAFT_YEAR', 'DRAFT_ROUND', 'DRAFT_NUMBER', 'GREATEST_75_FLAG']

    playerdf = getPlayer("Lebron James")
    columns = playerdf.columns.tolist()

    assert len(columns) == 33


def test_getpstats():
    # dfcolumns = ['PLAYER_ID', 'LEAGUE_ID', 'Team_ID', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']

    statsdf = playerStats("Lebron James")
    columns = statsdf.columns.tolist()

    assert len(columns) == 24


def test_nextgames():
    gamesdf = playerNextNGames("Lebron James", 3)
    columns = gamesdf.columns.tolist()

    assert len(columns) == 13


def test_teamInfo():
    teamdf = getTeam("mil")
    columns = teamdf.columns.tolist()

    assert len(columns) == 16


def test_myroster():
    l = myRoster("Handoff Hu")

    assert len(l) == 16


def test_teamstanding():
    t = getMyTeam("Handoff Hu")

    assert t.final_standing == 3


def test_team1():
    t = getTName(0)

    assert t == "atl"

def test_atlcolor1():
    t = getTName(1)

    assert t == "bos"