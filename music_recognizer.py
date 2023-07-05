import asyncio
import json
from shazamio import Shazam,  Serialize

async def getYoutubeLink(filePath):
    shazam = Shazam()
    out = await shazam.recognize_song(filePath)
    result = Serialize.full_track(data=out)
    youtube_data = await shazam.get_youtube_data(link=result.track.youtube_link)
    serialized_youtube = Serialize.youtube(data=youtube_data)
    return serialized_youtube.uri;

async def getSongInfo(filePath):
    shazam = Shazam()
    out = await shazam.recognize_song(filePath)
    return out

youtubeLink = asyncio.run(getYoutubeLink("Faded.mp3"))
shazSongInfo =  asyncio.run(getSongInfo("Faded.mp3"))

songInfo = shazSongInfo['track']
songInfo['youtube_uri'] = youtubeLink
print(songInfo)