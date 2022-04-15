'''
This script just moves MonitoringLocationIdentifier to the top level of the sites collection
'''

import pymongo, sys
from bson.objectid import ObjectId


def main():
    mongo = pymongo.MongoClient("mongodb://lattice-100:27018/")
    db = mongo["sustaindb"]
    sitesCollection = db['water_quality_sites']
    cursor = sitesCollection.find()
    count = cursor.count()
    index = 0
    outputFile = open('siteUpdateProgress.txt', 'a')

    for document in cursor:
        id = str(document['_id'])
        monitoringID = document['properties']['MonitoringLocationIdentifier']
        sitesCollection.update_one( { '_id': ObjectId(id) }, { '$set': { 'MonitoringLocationIdentifier': monitoringID } } )
        index += 1
        if index % 50 == 0:
            message = f'{round((index / count) * 100, 3)}%, {index} out of {count} documents processed'
            outputFile.write(message + '\n')
            print(message)

    outputFile.close()


if __name__ == "__main__":
    main()
