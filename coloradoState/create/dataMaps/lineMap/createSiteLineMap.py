
import pymongo, sys
sys.path.insert(0, '/s/parsons/b/others/sustain/matt/water_quality/coloradoState/create')
import utils

output = "siteToLineMap.json"
errorFile = "error.txt"
progressFile = "progress.txt"


def createLineSiteMap():
    water_quality_sites = utils.getCollection('co_water_quality_sites')
    lines, count = utils.getCollection('osm_co_lines_geo', noCursorTimeout=True)

    current_index = 0
    progress_output = open(progressFile, "a")

    for entry in lines:
        bodyOfWater = entry['BodyOfWater']
        coordinates = entry['geometry']['coordinates']
        site_list = queryMongoForLineSites(water_quality_sites, coordinates)

        if len(site_list) > 0:
            utils.formatAndWriteData({bodyOfWater: site_list}, output)

        current_index += 1
        percent_done = (current_index / count) * 100
        progress_message = f"{percent_done}% done."
        print(progress_message)
        progress_output.write(progress_message + "\n")

    lines.close()
    progress_output.close()


def queryMongoForLineSites(water_quality_sites, coordinates):

    site_list = []

    for coordinate_pair in coordinates:
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
    utils.formatStartOfFile(output)
    createLineSiteMap()
    utils.formatEndOfFile(output)


if __name__ == "__main__":
    main()