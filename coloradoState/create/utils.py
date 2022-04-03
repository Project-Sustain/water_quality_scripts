
import os, json, pymongo


def getJSON(file):
    f = open(file)
    jsonObject = json.load(f)
    f.close()
    return jsonObject


def getCollection(collection, query={}, noCursorTimeout=False):
    mongo = pymongo.MongoClient("mongodb://lattice-100:27018/")
    db = mongo["sustaindb"]
    cursor = db[collection].find(query, no_cursor_timeout=noCursorTimeout)
    count = cursor.count()
    return cursor, count


def getColoradoStateCoordinates():
    mongo = pymongo.MongoClient("mongodb://lattice-100:27018/")
    db = mongo["sustaindb"]
    coloradoState = db['osm_multipolygons_geo'].find({"properties.osm_id": "161961"})[0]
    coordinates = coloradoState['geometry']['coordinates']
    return coordinates


def formatAndWriteData(document, file):
    del document['_id']
    outputFile = open(file, "a")
    outputFile.write(json.dumps(document))
    outputFile.write(',\n')
    outputFile.close()


def formatStartOfFile(file):
    outputFile = open(file, "a")
    outputFile.write('[\n')
    outputFile.close()


def formatEndOfFile(file):
    with open(file, 'rb+') as filehandle:   
        filehandle.seek(-2, os.SEEK_END)
        filehandle.truncate()

    outputFile = open(file, "a")
    outputFile.write('\n]')
    outputFile.close()
