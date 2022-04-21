
import csv, os, sys

PATH_BASE = '/s/parsons/b/others/sustain/matt/water_quality/usa/download'
progressFile = 'progress.csv'

sys.path.insert(0, '/s/parsons/b/others/sustain/matt/water_quality/usa')
import utils


def getColumnNames(fileName):
    columnNames = []
    with open(fileName, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = ',')
        for row in csv_reader:
            columnNames.append(row)
            break
    return columnNames[0]


def getFilenames(directory):
    files = []
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if os.path.isfile(file):
            files.append(os.path.expanduser(file))
    return files


def writeColumnHeader(columnNames, file):
    with open(file, 'w', newline='') as csvfile:
        fields = columnNames
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()


def combineCsv(files, outputFile):
    writer = open(outputFile, 'a')
    for file in files:
        reader = open(file, 'r')
        lines = reader.readlines()
        lineCounter = 0
        for index, line in enumerate(lines):
            if index > 0:
                writer.write(line)
            lineCounter += 1
            utils.handleProgress(lineCounter, len(lines), progressFile)
        reader.close()
        print('File Finished Processing')


    writer.close()


def main():
    print("Hello World")

    directory = os.path.expanduser(PATH_BASE+'/data/batch3')
    headerInput = os.path.expanduser(PATH_BASE+'/data/batch3/washington.csv')
    outputFile = os.path.expanduser(PATH_BASE+'/data/combinedData/combinedBatch3.csv')

    columnNames = getColumnNames(headerInput)   
    writeColumnHeader(columnNames, outputFile)
    files = getFilenames(directory)
    combineCsv(files, outputFile)


if __name__ == "__main__":
    main()
