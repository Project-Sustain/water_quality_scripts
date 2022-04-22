
PATH_BASE = '/s/parsons/b/others/sustain/matt/water_quality/usa'

import json, sys, pymongo, os, logging
from time import sleep
from os.path import exists
from threading import Thread
sys.path.insert(0, PATH_BASE)
import utils

pipeData = "water_quality_pipes.json"
bodiesOfWater = "water_quality_bodies_of_water.json"
riversAndStreams = "water_quality_rivers_and_streams.json"
errorFile = "error.txt"
progressFile = "progress.txt"

PROGRESS_BASE = PATH_BASE+'/dataCollections/progressFiles'

def createCollections(threadNumber, NUM_THREADS, batch):

    site_line_matrix = os.path.expanduser(PATH_BASE+'/adjacentryMatrices/siteLineMatrix.json')
    site_polygon_matrix = os.path.expanduser(PATH_BASE+'/adjacentryMatrices/sitePolygonMatrix.json')
    water_data_file_path = os.path.expanduser(PATH_BASE+'/download/data/combinedData/' + batch)

    errorFile = os.path.expanduser(PATH_BASE+'/dataCollections/error.log')
    progressFile = os.path.expanduser(PROGRESS_BASE+'/progress_'+str(threadNumber)+'.txt')

    logging.basicConfig(filename=errorFile, level=logging.DEBUG, format='%(levelname)s %(name)s %(message)s')
    logger=logging.getLogger(__name__)

    mongo = pymongo.MongoClient("mongodb://lattice-100:27018/")
    db = mongo["sustaindb"]
    pipesCollection = db['water_quality_pipes']
    riversAndStreamsCollection = db['water_quality_rivers_and_streams']
    bodiesOfWaterCollection = db['water_quality_bodies_of_water']

    # Should I be loading these into memory? They're 25MB combined
    siteToLineMap = utils.getJSON(site_line_matrix)
    siteToPolygonMap = utils.getJSON(site_polygon_matrix)

    water_quality_data = utils.getJSON(water_data_file_path)

    documentsForThisThread = [water_quality_data[i] for i in range(len(water_quality_data)) if i == threadNumber or i%NUM_THREADS == threadNumber]

    documentsProcessedByThisThread = 0
    for document in documentsForThisThread:
        try:
            target_site_id = document['MonitoringLocationIdentifier']
            dataIsAssociatedWithPolygon = False
            dataIsAssociatedWithLine = False

            for entry in siteToPolygonMap:
                if dataIsAssociatedWithPolygon: break
                if target_site_id in list(entry.values())[0]:
                    document['BodyOfWater'] = list(entry.keys())[0]
                    dataIsAssociatedWithPolygon = True
                    break

            for entry in siteToLineMap:
                if dataIsAssociatedWithLine or dataIsAssociatedWithPolygon: break
                if target_site_id in list(entry.values())[0]:
                    document['BodyOfWater'] = list(entry.keys())[0]
                    dataIsAssociatedWithLine = True
                    break

            if dataIsAssociatedWithPolygon:
                bodiesOfWaterCollection.insert_one(document)
            elif dataIsAssociatedWithLine:
                riversAndStreamsCollection.insert_one(document)
            else:
                pipesCollection.insert_one(document)

            documentsProcessedByThisThread += 1
            utils.logProgress(documentsProcessedByThisThread, len(documentsForThisThread), progressFile, threadNumber)

        except Exception as e:
            utils.logError(logger, e, threadNumber)


def main(batch, NUM_THREADS):
    for i in range(0, NUM_THREADS):
        thread = Thread(target=createCollections, args=(i, NUM_THREADS, batch))
        thread.start()


if __name__ == "__main__":
    if len(sys.argv) != 3 :
        print('Invalid Args')
        print(f'Usage: python3 {sys.argv[0]} <source_file_name> <number_of_threads>')
        print(f'ex: python3 {sys.argv[0]} cBatch1.json 6')
    else:
        main(sys.argv[1], int(sys.argv[2]))
