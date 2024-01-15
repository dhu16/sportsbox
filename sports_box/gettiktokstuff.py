from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get(
    "ms_token", None
)

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

    async with TikTokApi()  as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        user = api.user("nba")

        async for video in user.videos(count=5):
            #print(video.id)
            id = str(video.id)
            #print(video.as_dict["desc"])
            vids.update({url + id: video.as_dict["desc"]})

            if len(vids) == 5:
                break

    return vids


async def getnfllinks():
    """Gets 5 recent NFL TikTok links.

    EX: nfllinks = getnfllinks()

    Returns:
        Dict: 5 NBA TikTok video links as keys and captions as values

    """
    vids = {}
    url = "https://www.tiktok.com/@nfl/video/"

    async with TikTokApi()  as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        user = api.user("nfl")

        async for video in user.videos(count=5):
            #print(video.id)
            id = str(video.id)
            #print(video.as_dict["desc"])
            vids.update({url + id: video.as_dict["desc"]})

            if len(vids) == 5:
                break

    return vids


# getnbattdesc()
