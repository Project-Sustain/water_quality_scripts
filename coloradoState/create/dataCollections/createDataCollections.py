
import sys
sys.path.insert(0, '/s/parsons/b/others/sustain/matt/water_quality/coloradoState/create')
import utils

pointData = "co_water_quality_point_data.json"
bodiesOfWater = "co_water_quality_bodies_of_water.json"
riversAndStreams = "co_water_quality_rivers_and_streams.json"
errorFile = "error.txt"
progressFile = "progress.txt"


def createCollections():
    siteToLineMap = utils.getJSON('siteToLineMap.json')
    siteToPolygonMap = utils.getJSON('siteToPolygonMap.json')
    water_quality_data, count = utils.getCollection("co_water_quality_data")

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
            utils.formatAndWriteData(document, pointData)

        current_index += 1
        percent_done = (current_index / count) * 100
        progress_message = f"{percent_done}%"
        print(progress_message)
        progress_output.write(progress_message + "\n")


def main():
    utils.formatStartOfFile(pointData)
    utils.formatStartOfFile(riversAndStreams)
    utils.formatStartOfFile(bodiesOfWater)
    createCollections()
    utils.formatEndOfFile(pointData)
    utils.formatEndOfFile(riversAndStreams)
    utils.formatEndOfFile(bodiesOfWater)


if __name__ == "__main__":
    main()
