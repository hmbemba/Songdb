from pathlib import Path


def getFilePath(client, songUrl: str, pathToDb: str):
    invalidCharacters = '<>:"/\|?*'
    fileName = f"{[artist['name'] for artist in client.track(songUrl)['artists'] ][0]} - {client.track(songUrl)['name']}"

    for char in invalidCharacters:
        fileName = fileName.replace(char, '')

    return f"{pathToDb}\{fileName}.md"


def getSongName(client, songUrl: str):
    return client.track(songUrl)['name']


def getArtistsList(client, songUrl: str):
    return [artist['name'] for artist in client.track(songUrl)['artists']]


def getBpm(client, songUrl: str):
    return int(client.audio_analysis(songUrl)['track']['tempo'])


def getKey(client, songUrl: str):
    pitchMap = {
        '0': 'C', '1': 'C#', '2': 'D', '3': 'D#', '4': 'E', '5': 'F', '6': 'F#', '7': 'G', '8': 'G#', '9': 'A', '10': 'A#', '11': 'B'

    }
    pcNumber = client.audio_analysis(songUrl)['track']['key']
    return pitchMap[f'{pcNumber}']


def checkIfDBFileExists(path) -> bool:
    return Path(path).is_file()


def generateDBFileFromSongUrl(client, songUrl: str, pathToDb: str, do_not_overwite=True):
    '''
    Generates a db file then returns a string saying completed
    '''
    dbFilePath = getFilePath(client, songUrl, pathToDb)

    if do_not_overwite:
        if checkIfDBFileExists(dbFilePath):
            return f"NOT COMPLETED: {dbFilePath} ALREADY EXISTS"
    else:
        pass

    songName = getSongName(client, songUrl)
    artists = getArtistsList(client, songUrl)
    bpm = getBpm(client, songUrl)
    key = getKey(client, songUrl)

    with open(dbFilePath, 'w', encoding="utf-8") as f:
        f.write(f"""---
SongName : {songName}
Artist : {artists}
Bpm : {bpm}
Key : {key}
Tags : None
Path :
SpotifyURL : {songUrl}
---
""")
        return f'Completed! : {dbFilePath}'


def getDBFileFromSongUrl(client, songUrl: str) -> str:
    
    '''
    Returns a string of the relevant db info
    '''

    songName = getSongName(client, songUrl)
    artists = getArtistsList(client, songUrl)
    bpm = getBpm(client, songUrl)
    key = getKey(client, songUrl)

    s = f"""---
SongName : {songName}
Artist : {artists}
Bpm : {bpm}
Key : {key}
Tags : None
Path :
SpotifyURL : {songUrl}
---
"""
    return s


def getDataFromPlaylist(client, playlistID) -> list:
    data = []

    for obj in client.playlist(playlistID)['tracks']['items']:
        artists = obj['track']['artists']
        data.append({
            'SongName': f"{obj['track']['name']}",
            'Artists': f"{[artist['name'] for artist in artists]}",
            'Url': f"{obj['track']['external_urls']['spotify']}",
            'Bpm': getBpm(client=client,songUrl=f"{obj['track']['external_urls']['spotify']}" ),
            "Key":getKey(client=client,songUrl=f"{obj['track']['external_urls']['spotify']}" ),
        })
        #return [artist['name'] for artist in artists]
    
    return data
