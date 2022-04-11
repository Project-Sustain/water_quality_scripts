
PATH_BASE = '/s/parsons/b/others/sustain/matt/water_quality/usa'

import os, sys
sys.path.insert(0, PATH_BASE+'/create')
import utils

pipeData = "water_quality_pipes.json"
bodiesOfWater = "water_quality_bodies_of_water.json"
riversAndStreams = "water_quality_rivers_and_streams.json"
errorFile = "error.txt"
progressFile = "progress.txt"

site_line_matrix = os.path.expanduser(PATH_BASE+'/adjacentryMatrices/siteLineMatrix.json')
site_polygon_matrix = os.path.expanduser(PATH_BASE+'/adjacentryMatrices/sitePolygonMatrix.json')

water_data_file_path = os.path.expanduser(PATH_BASE+'/download/data/data.json') # Update this when it's ready


def createCollections():
    siteToLineMap = utils.getJSON(site_line_matrix)
    siteToPolygonMap = utils.getJSON(site_polygon_matrix)
    water_quality_data = utils.getJSON(water_data_file_path)
    count = len(water_quality_data)

    current_index = 0
    progress_output = open(progressFile, "a")

    for document in water_quality_data:
        target_site_id = document['MonitoringLocationIdentifier']
        dataIsAssociatedWithPolygon = False
        dataIsAssociatedWithLine = False

        for entry in siteToPolygonMap:
            if dataIsAssociatedWithPolygon: break
            site_list = list(entry.values())[0]
            for site in site_list:
                if site == target_site_id:
                    document['BodyOfWater'] = list(entry.keys())[0]
                    dataIsAssociatedWithPolygon = True
                    break

        for entry in siteToLineMap:
            if dataIsAssociatedWithLine or dataIsAssociatedWithPolygon: break
            site_list = list(entry.values())[0]
            for site in site_list:
                if site == target_site_id:
                    document['BodyOfWater'] = list(entry.keys())[0]
                    dataIsAssociatedWithLine = True
                    break

        if dataIsAssociatedWithPolygon:
            utils.formatAndWriteData(document, bodiesOfWater)
        elif dataIsAssociatedWithLine:
            utils.formatAndWriteData(document, riversAndStreams)
        else:
            utils.formatAndWriteData(document, pipeData)

        current_index += 1
        percent_done = (current_index / count) * 100
        progress_message = f"{percent_done}%"
        print(progress_message)
        progress_output.write(progress_message + "\n")


def main():
    print('Hello World')
    # utils.formatStartOfFile(pipeData)
    # utils.formatStartOfFile(riversAndStreams)
    # utils.formatStartOfFile(bodiesOfWater)
    # createCollections()
    # utils.formatEndOfFile(pipeData)
    # utils.formatEndOfFile(riversAndStreams)
    # utils.formatEndOfFile(bodiesOfWater)


if __name__ == "__main__":
    main()
