
PATH_BASE = '/s/parsons/b/others/sustain/matt/water_quality/usa'

import os, sys, pymongo

sys.path.insert(0, PATH_BASE)
import utils

def buildFieldMetadata(data, collection):
    fieldMetadata = [{ "name" : "epoch_time", "type" : "DATE", "minDate" : -2191239000000, "maxDate" : 1709991300000 }]
    count = len(data)
    index = 0
    for entry in data:
        observation = list(entry.items())[0]
        objectToUpdate = getEntryFromMetadata(observation[0], fieldMetadata)
        if not bool(objectToUpdate):
            fieldMetadata.append(addObservationToMetadata(observation))
        else: 
            fieldMetadata.remove(objectToUpdate)
            fieldMetadata.append(checkAndUpdateMetadata(observation, objectToUpdate))
        index += 1
        print(f'{(index/count) * 100}% Generating Metadata for {collection}')

    cleanMetadata(fieldMetadata, collection)


def cleanMetadata(metadata, collection):
    cleanMetadata = []
    index = 0
    count = len(metadata)
    for entry in metadata:
        if 'min' in entry and entry['min'] == 0:
            del entry['min']

        if 'max' in entry and entry['max'] == 0:
            pass
        else:
            cleanMetadata.append(entry)
        
        index += 1
        print(f'{(index/count) * 100}% Cleaning Metadata for {collection}')

    addMetadataToCollection(collection, cleanMetadata)


def addMetadataToCollection(collection, fieldMetadata):
    mongo = pymongo.MongoClient("mongodb://lattice-100:27018/")
    db = mongo["sustaindb"]
    db["Metadata"].insert(
        {
            "collection" : collection, 
            "fieldMetadata": fieldMetadata
        }
    )


def checkAndUpdateMetadata(observation, objectToUpdate):
    if objectToUpdate['type'] == 'NUMBER':
        try:
            if observation[1] < objectToUpdate['min']:
                objectToUpdate['min'] = observation[1]
            if observation[1] > objectToUpdate['max']:
                objectToUpdate['max'] = observation[1]
        except:
            pass
    elif objectToUpdate['type'] == 'STRING':
        if observation[1] not in objectToUpdate['values']:
            objectToUpdate['values'].append(observation[1])
    return objectToUpdate


def getEntryFromMetadata(observationName, fieldMetadata):
    for entry in fieldMetadata:
        if entry['name'] == observationName:
            return entry
    return {}


def addObservationToMetadata(observation):
    name = observation[0]
    value = observation[1]
    valueType = type(value)
    if valueType == int or valueType == float:
        metadata = {
            'name': name,
            'type': 'NUMBER',
            'min': value,
            'max': value
        }
    elif valueType == str:
        metadata = {
            'name': name,
            'type': 'STRING',
            'values': [value]
        }
    return metadata


def main():
    print("Hello World")

    rivers_and_streams_data_file_path = os.path.expanduser(PATH_BASE+'/dataCollections/water_quality_rivers_and_streams.json')
    bodies_of_water_data_file_path = os.path.expanduser(PATH_BASE+'/dataCollections/water_quality_bodies_of_water.json')
    pipe_data_file_path = os.path.expanduser(PATH_BASE+'/dataCollections/water_quality_pipes.json')

    riversAndStreams = utils.getJSON(rivers_and_streams_data_file_path)
    bodiesOfWater = utils.getJSON(bodies_of_water_data_file_path)
    pipes = utils.getJSON(pipe_data_file_path)

    buildFieldMetadata(riversAndStreams, 'water_quality_rivers_and_sreams')
    buildFieldMetadata(bodiesOfWater, 'water_quality_bodies_of_water')
    buildFieldMetadata(pipes, 'water_quality_pipes')


if __name__ == "__main__":
    main()
