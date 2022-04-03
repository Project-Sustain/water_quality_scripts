
import pymongo, sys
sys.path.insert(0, '/s/parsons/b/others/sustain/matt/water_quality/coloradoState/create')
import utils


destination_file = "osm_co_lines_geo.json"
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


def createLineCollection():
    coloradoStateCoordinates = utils.getColoradoStateCoordinates()
    query = {
                '$and': [
                    {'geometry': {'$geoWithin': {'$geometry': {'type': 'MultiPolygon','coordinates': coloradoStateCoordinates}}}},
                    {'$or': waterways}
                ]
            }
    co_water_lines, count = utils.getCollection('osm_lines_geo', query=query, cursorTimeout=False)
    print(f'Number of lines in colorado state: {count}')
    current_index = 0

    for document in co_water_lines:

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