from db.Models.SongModel import SongModel
from edgedb.errors import ConstraintViolationError
from db.edbw.Properties import Type
from spotipy_stuff.Spotipy_API_Config import spotipy_client
import pprint
from spotipy_stuff.interface import getDataFromPlaylist
import fire

pp = pprint.PrettyPrinter(indent=4, sort_dicts=True)

def insertPlaylist(playlistUrl:str):
    '''
    Insert all the songs in a playlist into the db
    The Song db model requires the song name to be unique
    so if a song name has already been taken it will spit out an error
    '''
    for entry in getDataFromPlaylist(
        client=spotipy_client, 
        playlistID=playlistUrl):
        try:
            SongModel.insertEntry(
            _title = entry['SongName'],
            _artist= entry['Artists'],
            _songUrl = entry['Url'],
            _key = entry['Key'],
            _bpm = entry['Bpm']
            
        )
            print(f"Song: '{entry['SongName']}' added to db")
        except ConstraintViolationError as e:
            print(f"Song: '{entry['SongName']}' already in db")

def insertPlaylists(*playlistURLs:str):
    for pl in playlistURLs:
        insertPlaylist(playlistUrl=pl)

def getAllPlaylistsFromAUser(userId:str) -> list:
    '''
    Given this user link https://open.spotify.com/user/22z57fkqz6sunlhyv42yk4sba?si=e46bb621b2c5427c
    the spotify ID comes after "/user/"
    "22z57fkqz6sunlhyv42yk4sba" in this case
    A full path won't work
        
    --> Maybe try to handle that <---
    '''
    if userId:
        _playlists = spotipy_client.user_playlists(userId)
        #playlists = [f"{num} {item['name']} {item['uri']}" for num,item in enumerate(_playlists['items'])]
        #pp.pprint(playlists)
        print(_playlists)
    else:
        raise ValueError("No spotify user id entered")

def insertAllSongsFromAllPlaylistsFromAUser(userID:str):
    #insertPlaylists(getAllPlaylistsFromAUser(userID))
    getAllPlaylistsFromAUser(userID)

def getByBpm(bpm:int)->list:
    return [object for object in SongModel.getByProperty(printStr=False,propName="bpm",propType=Type.int32,_bpm = bpm)]

def getByBpmPrintFormatted(bpm:int, plusOrMinus = 5)->str:
    '''
    Returns a formatted string of all the songs that match the given bpm
    The default is plus or minus 5
    '''
    for x in range(-plusOrMinus, plusOrMinus+1, 1):
        for item in getByBpm(bpm +x):
            print(
                f'''
                SongName: {item.title}
                Artist: {item.artist}
                Bpm: {item.bpm}
                Key: {item.key}
                Url: {item.songUrl}
                -----------------
                '''
            )

def getByArtistName(artistName:str)->list:
    return [object for object in SongModel.getAll() if artistName.lower() in object.artist.lower()]

def getByArtistNamePrintFormatted(artistName:str)->str:
    '''
    Returns a formatted string of all the songs that match the given artist name
    '''
    for item in getByArtistName(artistName):
        print(
            f'''
            SongName: {item.title}
            Artist: {item.artist}
            Bpm: {item.bpm}
            Key: {item.key}
            Url: {item.songUrl}
            -----------------
            '''
        )

def getByKeyPrintFormatted(key:str)->str:
    '''
    Returns a formatted string of all the songs that match the given key
    '''
    for item in [object for object in SongModel.getAll() if key.lower() in object.key.lower()]:
        print(
            f'''
            SongName: {item.title}
            Artist: {item.artist}
            Bpm: {item.bpm}
            Key: {item.key}
            Url: {item.songUrl}
            -----------------
            '''
        )


def getAllPrintFormatted():
    for item in [object for object in SongModel.getAll()]:
        print(
                f'''
                SongName: {item.title}
                Artist: {item.artist}
                Bpm: {item.bpm}
                Key: {item.key}
                Url: {item.songUrl}
                -----------------
                '''
            )
   
if __name__ == '__main__':
  fire.Fire({
      'insertplaylist': insertPlaylist,
      'getbyartist': getByArtistNamePrintFormatted,
      'getbybpm':getByBpmPrintFormatted,
      'getall': getAllPrintFormatted,
      'getbykey':getByKeyPrintFormatted,
      'insertplaylists': insertPlaylists,
      'insertallsongsfromallplaylistsfromuser':insertAllSongsFromAllPlaylistsFromAUser
  })