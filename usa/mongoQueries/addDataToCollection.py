
BASE_PATH = '/s/parsons/b/others/sustain/matt/water_quality/usa'

import pymongo, sys, os
sys.path.insert(0, BASE_PATH)
import utils


site_line_matrix_path = os.path.expanduser(BASE_PATH+'/adjacentryMatrices/siteLineMatrix.json')
site_polygon_matrix_path = os.path.expanduser(BASE_PATH+'/adjacentryMatrices/sitePolygonMatrix.json')


def main(file):
    fileName = file.split('.')[0]
    new_data_path = os.path.expanduser(BASE_PATH+'/download/data/combinedData/'+file)
    newData = utils.getJSON(new_data_path)
    siteLineMatrix = utils.getJSON(site_line_matrix_path)
    sitePolygonMatrix = utils.getJSON(site_polygon_matrix_path)

    mongo = pymongo.MongoClient("mongodb://lattice-100:27018/")
    db = mongo['sustaindb']
    bodiesOfWater = db['water_quality_bodies_of_water']
    riversAndStreams = db['water_quality_rivers_and_streams']
    pipes = db['water_quality_pipes']

    count = len(newData)
    index = 0
    progress_output = open('progress.txt', 'a')
    progress_output.write(f'Beginning processing for {file}\n')

    for data in newData:
        targetSiteID = data['MonitoringLocationIdentifier']
        siteFound = waterBodyAssociatedWithSite(targetSiteID, sitePolygonMatrix, bodiesOfWater)
        if not siteFound:
            waterBodyAssociatedWithSite(targetSiteID, siteLineMatrix, riversAndStreams)
        if not siteFound:
            pipes.insert_one(data)

        index += 1
        utils.handleProgress(index, count, f'{fileName}_progress.txt')

    progress_output.close()


def waterBodyAssociatedWithSite(siteID, matrix, collection):
    for entry in matrix:
        bodyOfWater = list(entry.keys())[0]
        siteList = list(entry.values())[0]
        if siteID in siteList:
            entry['BodyOfWater'] = bodyOfWater
            collection.insert_one(entry)
            return True
    return False


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print('Please provide a file path')
    main(sys.argv[1])
    