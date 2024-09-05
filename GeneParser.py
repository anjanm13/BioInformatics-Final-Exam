import os
import re

dirName = "./studio6/YeastGenes"
outputFileName = "output.txt"

def main():
    # clears file
    open(outputFileName, "w").close()
    # opens file for writing
    outFile = open(outputFileName, "a")
    outFile.write("Output of Ace2 Binding Motif Search (ORFname and Amount of Occurrances of Motif Sequence)")
    for filename in os.listdir(dirName):
        f = os.path.join(dirName, filename)
        with open(f) as file:
            # skips first line
            next(file)
            # looks for ace2 motif, and returns an list for all matches of sequence
            pattern = [m.start() for m in re.finditer('CCAGC', file.read())]
            # writes it to file with ORFname and amount of occurrances
            outFile.write(f'\n{filename[:-4]}: {len(pattern)}')

if __name__ == "__main__":
    main()