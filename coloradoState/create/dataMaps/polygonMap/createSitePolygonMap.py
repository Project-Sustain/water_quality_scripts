
import pymongo, sys
sys.path.insert(0, '/s/parsons/b/others/sustain/matt/water_quality/coloradoState/create')
import utils

output = "siteToPolygonMap.json"
errorFile = "error.txt"
progressFile = "progress.txt"


def createLineSiteMap():
    water_quality_sites = utils.getCollection('co_water_quality_sites')
    polygons, count = utils.getCollection('osm_co_multipolygons_geo', noCursorTimeout=True)

    current_index = 0
    progress_output = open(progressFile, "a")

    for entry in polygons:
        bodyOfWater = entry['BodyOfWater']
        coordinates = entry['geometry']['coordinates']
        site_list = queryMongoForPolygonSites(water_quality_sites, coordinates)

        if len(site_list) > 0:
            utils.formatAndWriteData({bodyOfWater: site_list}, output)

        current_index += 1
        percent_done = (current_index / count) * 100
        progress_message = f"{percent_done}% done."
        print(progress_message)
        progress_output.write(progress_message + "\n")

    polygons.close()
    progress_output.close()


def queryMongoForPolygonSites(water_quality_sites, coordinates):
    try:
        sites_in_this_polygon = water_quality_sites.find(
                {
                    'geometry': {
                        '$geoWithin': {
                            '$geometry': {
                                'type': 'MultiPolygon',
                                'coordinates': coordinates
                            }
                        }
                    }
                }
            )
    except:
        sites_in_this_polygon = []

    site_list = []
    try:
        for site in sites_in_this_polygon:
            site_id = site['properties']['MonitoringLocationIdentifier']
            site_list.append(site_id)
    except:
        output_file = open(errorFile, "a")
        output_file.write(f"ERROR trying to iterate geo within result. Moving on.\n")
        output_file.close()

    for outer_coordinate_list in coordinates:
        for inner_coordinate_list in outer_coordinate_list:
            for coordinate_pair in inner_coordinate_list:
                try:
                    sites_near_coordinate_pair = water_quality_sites.aggregate([
                        {
                            '$geoNear': {
                                'near': { 'type': "Point", 'coordinates': coordinate_pair },
                                'distanceField': "dist.calculated",
                                'maxDistance': 50,
                                'spherical': 'true'
                            }
                        }
                    ])
                except:
                    sites_near_coordinate_pair = []

                for site in sites_near_coordinate_pair:
                    try:
                        site_name = site['properties']['MonitoringLocationIdentifier']
                        if site_name not in site_list:
                            site_list.append(site_name)
                    except:
                        output_file = open(errorFile, "a")
                        output_file.write(f"ERROR trying iterate geo near result. Moving on.\n")
                        output_file.close()

    return site_list


def main():
    print("Hello World")
    createLineSiteMap()
    utils.formatEndOfFile(output)


if __name__ == "__main__":
    main()