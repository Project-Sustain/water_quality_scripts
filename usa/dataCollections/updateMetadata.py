
import pymongo, sys
from threading import Lock
from threading import Thread


def updateMetadata(threadNumber, numberOfThreads, collection):

    mongo = pymongo.MongoClient("mongodb://lattice-100:27018/")
    db = mongo['sustaindb']
    cursor = db[collection]

    

    dataLock = Lock()

    with dataLock:
        pass
        # do stuff with lock

    # now its released

def main(numberOfThreads, collection):

    mongo = pymongo.MongoClient("mongodb://lattice-100:27018/")
    db = mongo['sustaindb']
    metadata = db['Metadata']
    metadata.delete_one({'collection': 'water_quality_bodies_of_water'})
    metadata.delete_one({'collection': 'water_quality_rivers_and_streams'})
    metadata.delete_one({'collection': 'water_quality_pipes'})

    threads = []
    for i in range(1, numberOfThreads+1):
        thread = Thread(updateMetadata(i, numberOfThreads, collection))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()


if __name__ == '__main__':

    numberOfThreads = sys.argv[1]
    collection = sys.argv[2]
    main(numberOfThreads, collection)
