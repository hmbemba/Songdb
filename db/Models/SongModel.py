import os
import edgedb
from db.edbw.EdgeDBModel import EdgeDBModel
from db.edbw.Properties import Type
import pprint
from dotenv import load_dotenv

pp = pprint.PrettyPrinter(indent=4)
load_dotenv()




localClient = edgedb.create_client()

remoteClient = edgedb.create_client(dsn=os.environ['DSN'], tls_security='insecure')
client = remoteClient


SongModel = EdgeDBModel(modelName='Song', client=client) 
SongModel.addProperty(_propertyName = 'title', _propertyType = Type.str, _req = True,)
SongModel.addProperty(_propertyName = 'artist', _propertyType = Type.str, _req = True)
SongModel.addProperty(_propertyName = 'bpm', _propertyType = Type.int32, _req = False)
SongModel.addProperty(_propertyName = 'key', _propertyType = Type.str, _req = False)
SongModel.addProperty(_propertyName = 'songUrl', _propertyType = Type.str, _req = False)


#SongModel.addProperty(_propertyName = 'mainGenre', _propertyType = Type.str, _req = False)



#InvoicesModel.getByProperty(printStr=True, propName='three_word_name', propType=Type.str, _three_word_name='TameHolographcScallop')

#InvoicesModel.insert(printStr=True, _three_word_name="hello world")

#InvoicesModel.updateEntry(uuid="123",printStr=True, title="blade runner")

#InvoicesModel.delEntry(uuid="123", printStr=True)