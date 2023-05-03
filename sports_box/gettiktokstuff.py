import json
from tiktokapipy.async_api import AsyncTikTokAPI


# MOCK CLASSES


class MockVideo(object):
    def __init__(self, id):
        self.id = id

    desc = "Video caption"


async def getnbalinks():
    """Gets 5 recent NBA TikTok links.

    EX: nbalinks = getnbalinks()

    Returns:
        Dict: 5 NBA TikTok video links as keys and captions as values

    """
    vids = {}
    url = "https://www.tiktok.com/@nba/video/"

    async with AsyncTikTokAPI() as api:
        user = await api.user("nba", video_limit=5)
        async for video in user.videos:
            # print(video.id)
            id = str(video.id)
            vids.update({url + id: video.desc})

    return vids


async def getnfllinks():
    """Gets 5 recent NFL TikTok links.

    EX: nfllinks = getnfllinks()

    Returns:
        Dict: 5 NBA TikTok video links as keys and captions as values

    """
    vids = {}
    url = "https://www.tiktok.com/@nfl/video/"

    async with AsyncTikTokAPI() as api:
        user = await api.user("nfl", video_limit=5)
        async for video in user.videos:
            # print(video.id)
            id = str(video.id)
            vids.update({url + id: video.desc})

    return vids


# getnbattdesc()
