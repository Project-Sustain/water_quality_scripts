
PATH_BASE = '/s/parsons/b/others/sustain/matt/water_quality/coloradoState/create'

import json
import sys

sys.path.insert(0, PATH_BASE)
import utils

def main():
    metadata = []
    fieldMetadata = utils.getJSON('cleanMetadata.json')
    for entry in fieldMetadata:
        metadata.append({
            'name': entry['name'],
            'temporal': True,
            'hideByDefault': False
        })

    with open("apertureMetadata.json", 'a') as f:
        f.write(json.dumps(metadata, indent=4))


if __name__ == "__main__":
    main()
