
import  sys
sys.path.insert(0, '/s/parsons/b/others/sustain/matt/water_quality/coloradoState/create')
import utils
from station import stations


destinationFile = "co_water_quality_sites.json"


def reformatStations():
    for station in stations:
        station['MonitoringLocationIdentifier'] = station['properties']['MonitoringLocationIdentifier']
        utils.formatAndWriteData(station, destinationFile)


def main():
    print("Hello World")
    utils.formatStartOfFile(destinationFile)
    reformatStations()
    utils.formatEndOfFile(destinationFile)


if __name__ == "__main__":
    main()