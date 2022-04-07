
'''
https://www.waterqualitydata.us/webservices_documentation/
'''

BASE_URL = '/s/parsons/b/others/sustain/matt/water_quality/coloradoState/download/data'

import csv, os, requests, json
state_file_path = os.path.expanduser(BASE_URL+'/apiMetadata/State.csv')
county_file_path = os.path.expanduser(BASE_URL+'/apiMetadata/County.csv')
characteristic_file_path = os.path.expanduser(BASE_URL+'/apiMetadata/Characteristic.csv')
aperture_characteristics_file_paths_file_path = os.path.expanduser(BASE_URL+'/apiMetadata/CharacteristicsInAperture.json')


# This works!!!
test = "https://www.waterqualitydata.us/data/Result/search?countycode=US%3A08%3A069&characteristicName=Calcium&mimeType=csv"


def getEndpoint(STATE_CODE, COUNTY_CODE, CHARACTERISTIC):
    return "https://www.waterqualitydata.us/data/Result/search?countycode=US%3A"+STATE_CODE+"%3A"+COUNTY_CODE+"&characteristicName="+CHARACTERISTIC+"&mimeType=csv"


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
    return names


def getCharacterstics():
    characteristicNames = extractCharacteristicNames()
    characteristicInfo = []
    with open(characteristic_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Name'] in characteristicNames:
                characteristicInfo.append(row['Name'])
    return characteristicInfo


def getDataForUSA():
    stateFIPS = getStateCodeList()
    characteristics = getCharacterstics()
    for state in stateFIPS:
        counties = getCountyCodeForState(state['Code'])
        for county in counties:
            for characteristic in characteristics:
                # Make a call to the endpoint, store result
                endpoint = getEndpoint(state['FIPS'], county, characteristic)
                response = requests.get(endpoint)
                decoded_content = response.content.decode('utf-8')


def getDataForColorado():
    characteristics = getCharacterstics()
    counties = getCountyCodeForState('CO')
    for county in counties:
        for characteristic in characteristics:
            endpoint = getEndpoint('CO', county, characteristic)
            # Make a call to the endpoint, store result


def main():
    print("Hello World")
    # test_call = "https://www.waterqualitydata.us/data/Result/search?countycode=US%3A08%3A069&characteristicName=Calcium&mimeType=csv"
    # response = requests.get(test_call)
    # print(response)


if __name__ == "__main__":
    main()
