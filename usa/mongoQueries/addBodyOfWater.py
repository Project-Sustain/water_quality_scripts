
import pymongo, sys
from bson.objectid import ObjectId
sys.path.insert(0, '/s/parsons/b/others/sustain/matt/water_quality/usa')
import utils


def updateCollection(collection, findQuery, progressFile):
    cursor = collection.find(findQuery)
    numberOfDocuments = cursor.count()
    index = 0
    progress_output = open(progressFile, 'a')
    for document in cursor:
        id = str(document['_id'])
        collection.update_one( { '_id': ObjectId(id) }, { '$set': { 'BodyOfWater': id } } )
        index += 1
        progress_message = f'{(index / numberOfDocuments) * 100}%'
        print(progress_message)
        progress_output.write(progress_message + "\n")
    progress_output.close()


def testAddField(db):
    cursor = db['osm_larimer_water_polygons'].find({ 'properties.natural': 'water' })
    for document in cursor:
        id = str(document['_id'])
        db['osm_larimer_water_polygons'].update_one({'_id': ObjectId(id)}, { '$set': {'TestUpdate2': id} })


def main():
    mongo = pymongo.MongoClient("mongodb://lattice-100:27018/")
    db = mongo["sustaindb"]

    print("Working on Multipolygons")
    polygonCollection = db['osm_multipolygons_geo']
    polygonQuery = {'properties.natural': 'water'}
    updateCollection(polygonCollection, polygonQuery, 'polygonProgress.txt')

    print("Working on Lines")
    lineCollection = db['osm_lines_geo']
    lineQuery = {'$or': utils.waterways}
    updateCollection(lineCollection, lineQuery, 'lineProgress.txt')


if __name__ == "__main__":
    main()
