
PATH_BASE = '/s/parsons/b/others/sustain/matt/water_quality/coloradoState/create'

import os, sys

sys.path.insert(0, PATH_BASE)
import utils

outputFile = "fieldMetadata.json"
co_river_data_file_path = os.path.expanduser(PATH_BASE+'/dataCollections/co_water_quality_rivers_and_streams.json')


def buildFieldMetadata():
    pointData = utils.getJSON(co_river_data_file_path)
    fieldMetadata = []
    count = len(pointData)
    index = 0
    for entry in pointData:
        observation = list(entry.items())[0]
        objectToUpdate = getEntryFromMetadata(observation[0], fieldMetadata)
        if not bool(objectToUpdate):
            fieldMetadata.append(addObservationToMetadata(observation))
        else: 
            fieldMetadata.remove(objectToUpdate)
            fieldMetadata.append(checkAndUpdateMetadata(observation, objectToUpdate))
        index += 1
        print(f'{(index/count) * 100}%')


    for entry in fieldMetadata: print(entry)
    for entry in fieldMetadata: utils.formatAndWriteData(entry, outputFile)


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
    utils.formatStartOfFile(outputFile)
    buildFieldMetadata()
    utils.formatEndOfFile(outputFile)


if __name__ == "__main__":
    main()
