
'''
https://www.waterqualitydata.us/webservices_documentation/
'''


import csv, os, requests, json
state_file_path = os.path.expanduser('/s/parsons/b/others/sustain/matt/water_quality/coloradoState/download/data/apiMetadata/State.csv')
county_file_path = os.path.expanduser('/s/parsons/b/others/sustain/matt/water_quality/coloradoState/download/data/apiMetadata/County.csv')
characteristic_file_path = os.path.expanduser('/s/parsons/b/others/sustain/matt/water_quality/coloradoState/download/data/apiMetadata/Characteristic.csv')
aperture_characteristics_file_paths_file_path = os.path.expanduser('/s/parsons/b/others/sustain/matt/water_quality/coloradoState/download/data/apiMetadata/CharacteristicsInAperture.json')


def getEndpoint(STATE_CODE, COUNTY_CODE):
    return "https://www.waterqualitydata.us/data/Result/search?countycode=US%3A"+STATE_CODE+"%3A"+COUNTY_CODE+"&mimeType=csv"


def getJSON(file):
    f = open(file)
    jsonObject = json.load(f)
    f.close()
    return jsonObject


def getStateCodeList():
    ignoredStateNames = ['Johnston Atoll', 'Midway Islands', 'Navassa Island', 'Wake Island', 'Baker Island', 'Howland Island', 
    'Jarvis Island', 'Kingman Reef', 'Palmyra Atoll', 'American Samoa', 'Marshall Islands', 'N. Mariana Islands', 'Puerto Rico',
     'Palau', 'Virgin Islands', 'Guam', 'District of Columbia', 'Micronesia']
    stateCodes = []
    with open(state_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Country Code'] == "US" and row['Name'] not in ignoredStateNames:
                stateCodes.append({
                    'Code': row['Code'],
                    'FIPS': row['Fips Code'].zfill(2)
                })
    return stateCodes


def getCountyCodeForState(STATE_CODE):
    countyCodes = []
    with open(county_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['State Code'] == STATE_CODE:
                countyCodes.append(row['County FIPS Code'][1:].zfill(3))
    return countyCodes


def extractCharacteristicNames():
    jsonObject = getJSON(aperture_characteristics_file_paths_file_path)
    names = []
    for entry in jsonObject:
        names.append(entry['name'])


def getCharacterstics():
    characteristicGroups = ['Physical', 'Radiochemical', 'Stable Isotopes']
    characteristicInfo = []
    with open(characteristic_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Group Name'] in characteristicGroups:
                characteristicInfo.append(row['Name'])
    return characteristicInfo


def getDataForUSA():
    stateFIPS = getStateCodeList()
    for state in stateFIPS:
        counties = getCountyCodeForState(state['Code'])
        for county in counties:
            endpoint = getEndpoint(state['FIPS'], county)
            # Make a call to the endpoint


def getDataForColorado():
    counties = getCountyCodeForState('CO')
    for county in counties:
        endpoint = getEndpoint('CO', county)
        print(endpoint)
        # Make a call to the endpoint


def main():
    print("Hello World")
    getDataForColorado()
    # getDataForUSA()


if __name__ == "__main__":
    main()
