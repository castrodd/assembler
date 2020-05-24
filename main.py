import sys
from parser import Parser
from code import Code
from symbolTable import SymbolTable

def createOutputFile():
    currentFileName = sys.argv[1].split(".")[0]
    currentFileName = currentFileName.split("/")[-1]
    outputFileName = currentFileName + ".hack"
    return open(outputFileName, "x")

def generateSymbolTable(table, inputFile):
    programCounter = 0

    while inputFile.hasMoreCommands():
        inputFile.advance()
        #print(inputFile.currentCommand)
        #print(inputFile.commandType())
        if inputFile.isC() or inputFile.isA():
            programCounter += 1
        elif inputFile.isL():
            symbol = inputFile.symbol()
            table.addEntry(symbol, programCounter)
        else:
            pass
    
    inputFile.resetCommands()

def isNumber(symbol):
    try:
        float(symbol)
        return True
    except ValueError:
        return False

def writeToOutputFile(table, inputFile, outputFile):
    currentROMAddress = 16

    while inputFile.hasMoreCommands():
        inputFile.advance()

        if inputFile.isC():
            comp = Code.comp(inputFile.comp())
            dest = Code.dest(inputFile.dest())
            jump = Code.jump(inputFile.jump())

            binaryLine = '111' + comp + dest + jump + '\n'
            #print(binaryLine)
            outputFile.write(binaryLine)

        elif inputFile.isA():
            initialSymbol = inputFile.symbol()
            if isNumber(initialSymbol):
                address = initialSymbol
            elif table.contains(initialSymbol):
                address = table.getAddress(initialSymbol)
            else:
                address = currentROMAddress
                table.addEntry(initialSymbol, address)
                currentROMAddress += 1

            symbol ="{0:>015b}".format(int(address))
            binaryLine = '0' + symbol + '\n'
            #print(binaryLine)
            outputFile.write(binaryLine)
        
        else:
            pass

def closeFiles(inputFile, outputFile):
    inputFile.close()
    outputFile.close()

def main():
    inputFile = Parser(sys.argv[1])
    outputFile = createOutputFile()
    table = SymbolTable()

    generateSymbolTable(table, inputFile)
    #print(table.table)
    writeToOutputFile(table, inputFile, outputFile)
    
    closeFiles(inputFile, outputFile)
    #print("Assembler finished.")

if __name__ == "__main__":
    main()