# tests
from sports_box import (
    getPID,
    PlayerInfo,
    PlayerStats,
    PlayerGames,
    PlayerId,
    TeamId,
    getTName,
)
from unittest.mock import patch
from unittest import TestCase

# from typing import List
# import pytest
# import pandas as pd


sample_id_data = {
    'id': 2544,
    'full_name': 'LeBron James',
    'first_name': 'LeBron',
    'last_name': 'James',
    'is_active': True,
}

sample_player_data = {
    'headers': [
        'PERSON_ID',
        'FIRST_NAME',
        'LAST_NAME',
        'DISPLAY_FIRST_LAST',
        'DISPLAY_LAST_COMMA_FIRST',
        'DISPLAY_FI_LAST',
        'PLAYER_SLUG',
        'BIRTHDATE',
        'SCHOOL',
        'COUNTRY',
        'LAST_AFFILIATION',
        'HEIGHT',
        'WEIGHT',
        'SEASON_EXP',
        'JERSEY',
        'POSITION',
        'ROSTERSTATUS',
        'GAMES_PLAYED_CURRENT_SEASON_FLAG',
        'TEAM_ID',
        'TEAM_NAME',
        'TEAM_ABBREVIATION',
        'TEAM_CODE',
        'TEAM_CITY',
        'PLAYERCODE',
        'FROM_YEAR',
        'TO_YEAR',
        'DLEAGUE_FLAG',
        'NBA_FLAG',
        'GAMES_PLAYED_FLAG',
        'DRAFT_YEAR',
        'DRAFT_ROUND',
        'DRAFT_NUMBER',
        'GREATEST_75_FLAG',
    ],
    'data': [
        [
            2544,
            'LeBron',
            'James',
            'LeBron James',
            'James, LeBron',
            'L. James',
            'lebron-james',
            '1984-12-30T00:00:00',
            'St. Vincent-St. Mary HS (OH)',
            'USA',
            'St. Vincent-St. Mary HS (OH)/USA',
            '6-9',
            '250',
            19,
            '6',
            'Forward',
            'Active',
            'Y',
            1610612747,
            'Lakers',
            'LAL',
            'lakers',
            'Los Angeles',
            'lebron_james',
            2003,
            2022,
            'N',
            'Y',
            'Y',
            '2003',
            '1',
            '1',
            'Y',
        ]
    ],
}
sample_player_stats = {
    'headers': [
        'PLAYER_ID',
        'LEAGUE_ID',
        'Team_ID',
        'GP',
        'GS',
        'MIN',
        'FGM',
        'FGA',
        'FG_PCT',
        'FG3M',
        'FG3A',
        'FG3_PCT',
        'FTM',
        'FTA',
        'FT_PCT',
        'OREB',
        'DREB',
        'REB',
        'AST',
        'STL',
        'BLK',
        'TOV',
        'PF',
        'PTS',
    ],
    'data': [
        [
            2544,
            '00',
            0,
            1413,
            1412,
            53833.0,
            14075,
            27886,
            0.504733,
            2240,
            6511,
            0.344033,
            8060,
            10968,
            0.734865,
            1658,
            8948,
            10606,
            10371,
            2180,
            1067,
            4935,
            2595,
            38450,
        ]
    ],
}
sample_player_games = {
    'headers': [
        'GAME_ID',
        'GAME_DATE',
        'HOME_TEAM_ID',
        'VISITOR_TEAM_ID',
        'HOME_TEAM_NAME',
        'VISITOR_TEAM_NAME',
        'HOME_TEAM_ABBREVIATION',
        'VISITOR_TEAM_ABBREVIATION',
        'HOME_TEAM_NICKNAME',
        'VISITOR_TEAM_NICKNAME',
        'GAME_TIME',
        'HOME_WL',
        'VISITOR_WL',
    ],
    'data': [],
}

sample_team_id = {
    'id': 1610612749,
    'full_name': 'Milwaukee Bucks',
    'abbreviation': 'MIL',
    'nickname': 'Bucks',
    'city': 'Milwaukee',
    'state': 'Wisconsin',
    'year_founded': 1968,
}


# PLAYER ID TEST
def mock_get_playerid(player_id):
    return 2544


class PlayerIdTest(TestCase):
    def setUp(self):
        self.playerid = PlayerId("Lebron James")

    @patch('nba_api.stats.static.players.find_players_by_full_name', mock_get_playerid)
    def test_first(self):
        mock_id = self.playerid.get_data()
        assert mock_id == sample_id_data['id']


# PLAYER INFO TEST
def mock_get_playerinfo(player_id):
    return sample_player_data


class PlayerInfoTest(TestCase):
    def setUp(self):
        self.playerinfo = PlayerInfo(2544)

    @patch('nba_api.stats.endpoints.commonplayerinfo', mock_get_playerinfo)
    def test_getplayer(self):
        mock_data = self.playerinfo.get_data()

        assert mock_data == sample_player_data


# PLAYER STATS TEST
def mock_get_playerstats(player_id):
    return sample_player_stats


class PlayerStatsTest(TestCase):
    def setUp(self):
        self.playerstats = PlayerStats(2544)

    @patch('nba_api.stats.endpoints.playercareerstats', mock_get_playerstats)
    def test_getpstats(self):
        mock_data = self.playerstats.get_data()

        assert mock_data == sample_player_stats


# PLAYER NEXT GAMES TEST
def mock_get_playergames(player_id):
    return sample_player_stats


class PlayerGamesTest(TestCase):
    def setUp(self):
        self.playergames = PlayerGames(
            number_of_games="3", player_id=2544, season_all="2021-22", season_type_all_star="Regular Season"
        )

    @patch('nba_api.stats.endpoints.PlayerNextNGames', mock_get_playergames)
    def test_nextgames(self):
        mock_data = self.playergames.get_data()

        assert mock_data == sample_player_games


# TEAM ID TEST
def mock_get_teamid(team_id):
    return 1610612749


class TeamIdTest(TestCase):
    def setUp(self):
        self.teamid = TeamId("mil")

    @patch('nba_api.stats.static.teams.find_team_by_abbreviation', mock_get_teamid)
    def test_teamInfo(self):
        mock_id = self.teamid.get_data()
        assert mock_id == sample_team_id['id']


# def test_myroster():
# length = myRoster("Handoff Hu")

# assert len(length) == 16


# def test_teamstanding():
# t = getMyTeam("Handoff Hu")

# assert t.final_standing == 3


def test_team1():
    t = getTName(0)

    assert t == "atl"


def test_atlcolor1():
    t = getTName(1)

    assert t == "bos"
