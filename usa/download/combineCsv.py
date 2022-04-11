
import csv, os

PATH_BASE = '/s/parsons/b/others/sustain/matt/water_quality/usa/download'
processFile = 'process.csv'


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
    processWriter = open(processFile, 'a')
    writer = open(outputFile, 'a')
    fileCounter = 0
    totalFiles = len(files)
    for file in files:
        reader = open(file, 'r')
        lines = reader.readlines()
        lineCounter = 0
        for index, line in enumerate(lines):
            if index > 0:
                writer.write(line)
            lineCounter += 1
            lineProcessMessage = f'{(lineCounter / len(lines)) * 100}% of Lines Processed for Current File'
            processWriter.write(lineProcessMessage)
            print(lineProcessMessage)
        writer.write("\n")
        reader.close()

        fileCounter += 1
        filePercentage = (fileCounter / totalFiles) * 100
        fileProcessMessage = f'**** {filePercentage}% of Files Processed ****'
        processWriter.write(fileProcessMessage)
        print(fileProcessMessage)

    writer.close()
    processWriter.close()


def main():
    print("Hello World")

    directory = os.path.expanduser(PATH_BASE+'/data')
    headerInput = os.path.expanduser(PATH_BASE+'/data/alabama.csv')
    outputFile = os.path.expanduser('combinedCsvData.csv')

    columnNames = getColumnNames(headerInput)   
    writeColumnHeader(columnNames, outputFile)
    files = getFilenames(directory)
    combineCsv(files, outputFile)


if __name__ == "__main__":
    main()
