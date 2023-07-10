import asyncio
import json
from shazamio import Shazam,  Serialize
import os

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

PATH = "./MusicDir/"
musicData = { 'songs': []}
songInfo = {}
for file in os.listdir(PATH):
    youtubeLink = asyncio.run(getYoutubeLink(PATH + file))
    shazSongInfo =  asyncio.run(getSongInfo(PATH + file))
    songInfo['title'] = shazSongInfo['track']['title']
    songInfo['images'] = shazSongInfo['track']['images']
    songInfo['youtube_uri'] = youtubeLink
    songInfo['path'] = os.path.abspath(PATH + file)
    musicData['songs'].append(songInfo)

with open("musicData.json", 'w') as outfile:
    json.dump(musicData, outfile, indent = 2)