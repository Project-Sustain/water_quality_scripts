
PATH_BASE = '/s/parsons/b/others/sustain/matt/water_quality/coloradoState/create'

import os, sys

sys.path.insert(0, PATH_BASE)
import utils

outputFile = "cleanMetadata.json"
inputFile = "fieldMetadata.json"


def cleanMetadata():
    input = utils.getJSON(inputFile)
    for entry in input:
        if 'min' in entry and entry['min'] == 0:
            del entry['min']

        if 'max' in entry and entry['max'] == 0:
            pass
        else:
            utils.formatAndWriteData(entry, outputFile)

def main():
    print("Hello World")
    utils.formatStartOfFile(outputFile)
    cleanMetadata()
    utils.formatEndOfFile(outputFile)


if __name__ == "__main__":
    main()
