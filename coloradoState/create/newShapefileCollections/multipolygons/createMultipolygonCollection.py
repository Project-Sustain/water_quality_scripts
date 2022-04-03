
import pymongo, sys
sys.path.insert(0, '/s/parsons/b/others/sustain/matt/water_quality/coloradoState/create')
import utils


destination_file = "osm_co_multipolygons_geo.json"


def createLineCollection():
    coloradoStateCoordinates = utils.getColoradoStateCoordinates()
    query = {
                '$and': [
                    {'properties.natural': 'water'},
                    {'geometry': {'$geoWithin': {'$geometry': {'type': 'MultiPolygon','coordinates': coloradoStateCoordinates}}}}
                ]
            }
    co_water_multipolygons, count = utils.getCollection('osm_multipolygons_geo', query=query, cursorTimeout=False)
    current_index = 0

    for document in co_water_multipolygons:

        document['BodyOfWater'] = str(document['_id'])
        utils.formatAndWriteData(document, destination_file)

        percent_done = (current_index / count) * 100
        print(f'{percent_done}% done processing.')
        current_index += 1


def main():
    print("Hello World")
    utils.formatStartOfFile(destination_file)
    createLineCollection()
    utils.formatEndOfFile(destination_file)


if __name__ == "__main__":
    main()