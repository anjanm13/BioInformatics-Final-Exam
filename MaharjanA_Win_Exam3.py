import os

# Scans throught the Yeast alignments and finds average percentage of GC content throughout
# each gene and writes it to an output file
dirName = "./YeastGenes"
outputFileName = "output.txt"

def main():

    # clears file
    open(outputFileName, "w").close()
    # opens file for writing
    outFile = open(outputFileName, "a")

    currSpecies = ""
    newSpecies = False
    strFileVal = ""

    for filename in os.listdir(dirName):
        orfName = filename[:-4]

        # if the orf name doesn't end in a W, skip
        if not orfName.endswith("W"):
            continue
        
        fileSpecies = orfName[:3]

        # if a new species
        if fileSpecies != currSpecies:
            currSpecies = fileSpecies
            newSpecies = True

        f = os.path.join(dirName, filename)

        # adds all sequences from same species into one string and prints out percentage
        with open(f) as file:
            next(file)
            strFileVal += file.read()

        if (newSpecies):
            newSpecies = False
            outFile.write(f"{currSpecies} average percentage of GC content: {gcPercent(strFileVal)[0]}%\n")
            strFileVal = ""


def gcPercent(strFile):
    lenOfFile = len(strFile)

    cCount = strFile.count('C')
    gCount = strFile.count('G')

    percent = (cCount + gCount) / lenOfFile

    return (round(percent * 100, 2), lenOfFile)


if __name__ == "__main__":
    main()