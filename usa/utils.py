
import os, json, pymongo
from datetime import datetime


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


def getTimestamp():
    return '[' + datetime.now().strftime("%m/%d/%Y %H:%M:%S") + ']'


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


def handleProgress(index, count, outputFile, interval=10000, precision=2):
    if index % interval == 0:
        percent_done = round((index / count) * 100, precision)
        progress_message = f'{getTimestamp()} {percent_done}% {index}/{count}'
        print(progress_message)
        with open(outputFile, 'a') as output:
            output.write(progress_message + "\n")
    if index == count:
        progress_message = f'{getTimestamp()} 100% {index}/{count}'
        print(progress_message)
        with open(outputFile, 'a') as output:
            output.write(progress_message + "\n")


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
    file.seek(-2, os.SEEK_END)
    file.truncate()
    file.write('\n]')
