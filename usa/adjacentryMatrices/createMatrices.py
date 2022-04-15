
import json, sys, pymongo
sys.path.insert(0, '/s/parsons/b/others/sustain/matt/water_quality/usa')
import utils


def createSitePolygonMatrix():
    
    mongo = pymongo.MongoClient("mongodb://lattice-100:27018/")
    db = mongo["sustaindb"]
    water_quality_sites = db['water_quality_sites']

    polygonCursor = db['osm_multipolygons_geo'].find({'properties.natural': 'water'}, no_cursor_timeout=True)
    count = polygonCursor.count()

    index = 0
    outputFile = open('sitePolygonMatrix.json', 'a')
    # outputFile.write('[\n')

    try:
        for document in polygonCursor:
            index += 1
            if index > getLastProcessedDocument('polygonProgress.txt'):
                bodyOfWater = document['BodyOfWater']
                coordinates = document['geometry']['coordinates']
                site_list = queryMongoForPolygonSites(water_quality_sites, coordinates)

                if len(site_list) > 0:
                    outputFile.write(json.dumps({bodyOfWater: site_list}, indent=4))
                    outputFile.write(',\n')

                utils.handleProgress(index, count, 'polygonProgress.txt', 1, 6)

    except Exception as e:
        with open('polygonErrors.txt', 'a') as f:
            f.write(utils.getTimestamp())
            f.write(str(e))
            f.write('\n')
            print(e)
            print('Recursing...')
            createSitePolygonMatrix()
        
    outputFile.close()
    polygonCursor.close()
    utils.formatEndOfFile(outputFile)


def getLastProcessedDocument(file):
    with open(file, 'r') as f:
        return int(f.readlines()[-1].split(' ')[3].split('/')[0])


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
                },
                no_cursor_timeout = True
            )
    except:
        sites_in_this_polygon = []

    site_list = []
    try:
        for site in sites_in_this_polygon:
            site_id = site['properties']['MonitoringLocationIdentifier']
            site_list.append(site_id)
    except:
        with open('polygonErrors.txt', "a") as f:
            f.write(f"{utils.getTimestamp()} ERROR trying to iterate geo within result. Moving on.\n")

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
                        with open('polygonErrors.txt', "a") as f:
                            f.write(f"{utils.getTimestamp()} ERROR trying to iterate geo within result. Moving on.\n")

    return site_list


def createSiteLineMatrix():

    mongo = pymongo.MongoClient("mongodb://lattice-100:27018/")
    db = mongo["sustaindb"]
    water_quality_sites = db['water_quality_sites']

    lineCursor = db['osm_lines_geo'].find({'properties.natural': 'water'}, no_cursor_timeout=True)
    count = lineCursor.count()

    index = 0
    outputFile = open('siteLineMatrix.json', 'a')
    # outputFile.write('[\n')

    try:
        for document in lineCursor:
            index += 1
            if index > getLastProcessedDocument('lineProgress.txt'):
                bodyOfWater = document['BodyOfWater']
                coordinates = document['geometry']['coordinates']
                site_list = queryMongoForLineSites(water_quality_sites, coordinates)

                if len(site_list) > 0:
                    outputFile.write(json.dumps({bodyOfWater: site_list}), indent=4)
                    outputFile.write(',\n')

                utils.handleProgress(index, count, 'lineProgress.txt', 1, 6)

    except Exception as e:
        with open('lineErrors.txt', 'a') as f:
            f.write(utils.getTimestamp())
            f.write(str(e))
            f.write('\n')
            print(e)
            print('Recursing...')
            createSiteLineMatrix()

    utils.formatEndOfFile(outputFile)
    lineCursor.close()
    outputFile.close()


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
                with open('lineErrors.txt', "a") as f:
                    f.write(f'{utils.getTimestamp()} ERROR trying iterate geo near result. Moving on.\n')

    return site_list


def main():
    print("Hello World")
    createSitePolygonMatrix()
    createSiteLineMatrix()


if __name__ == "__main__":
    main()