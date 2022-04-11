
import pymongo, sys
sys.path.insert(0, '/s/parsons/b/others/sustain/matt/water_quality/usa')
import utils


def createSitePolygonMatrix():
    water_quality_sites = utils.getCollection('usa_water_quality_sites')
    polygons, count = utils.getCollection('osm_multipolygons_geo', query={'properties.natural': 'water'}, noCursorTimeout=True)

    current_index = 0
    progress_output = open('polygonProgress.txt', "a")

    for entry in polygons:
        bodyOfWater = entry['BodyOfWater']
        coordinates = entry['geometry']['coordinates']
        site_list = queryMongoForPolygonSites(water_quality_sites, coordinates)

        if len(site_list) > 0:
            utils.formatAndWriteData({bodyOfWater: site_list}, 'sitePolygonMatrix.json')

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
        output_file = open('polygonErrors.txt', "a")
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
                        output_file = open('polygonErrors.txt', "a")
                        output_file.write(f"ERROR trying iterate geo near result. Moving on.\n")
                        output_file.close()

    return site_list


def createSiteLineMatrix():
    water_quality_sites = utils.getCollection('water_quality_sites')
    lines, count = utils.getCollection('osm_lines_geo', query={'$or': utils.waterways}, noCursorTimeout=True)

    current_index = 0
    progress_output = open('lineProgress.txt', "a")

    for entry in lines:
        bodyOfWater = entry['BodyOfWater']
        coordinates = entry['geometry']['coordinates']
        site_list = queryMongoForLineSites(water_quality_sites, coordinates)

        if len(site_list) > 0:
            utils.formatAndWriteData({bodyOfWater: site_list}, 'siteLineMatrix.json')

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
                output_file = open('lineErrors.txt', "a")
                output_file.write(f"ERROR trying iterate geo near result. Moving on.\n")
                output_file.close()

    return site_list


def main():
    print("Hello World")
    # createSitePolygonMatrix()
    # createSiteLineMatrix()


if __name__ == "__main__":
    main()