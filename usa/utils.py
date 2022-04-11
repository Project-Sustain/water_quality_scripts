
import os, json, pymongo


waterways = [
    # These come from OSM docs for key:waterway
    # natural
    {"properties.waterway": "stream"},
    {"properties.waterway": "river"},
    {"properties.waterway": "tidal_channel"},
    # manmade
    {"properties.waterway": "canal"},
    {"properties.waterway": "pressurised"},
    {"properties.waterway": "drain"},
    {"properties.waterway": "ditch"},
    {"properties.waterway": "fairway"},
    {"properties.waterway": "fish_pass"},
    # facilities
    {"properties.waterway": "dock"},
    {"properties.waterway": "boaryard"},
    # barriers on waterway
    {"properties.waterway": "dam"},
    {"properties.waterway": "weird"},
    {"properties.waterway": "waterfall"},
    {"properties.waterway": "rapids"},
    {"properties.waterway": "lock_gate"},
    {"properties.waterway": "sluice_gate"},
    # other features on waterway
    {"properties.waterway": "turning_point"},
    {"properties.waterway": "water_point"},
    {"properties.waterway": "fuel"},
]


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
    if '_id' in document:
        del document['_id']
    outputFile = open(file, "a")
    outputFile.write(json.dumps(document, indent=4))
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
