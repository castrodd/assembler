import sys
from parser import Parser
from code import Code

def output():
    currentFileName = sys.argv[1].split(".")[0]
    currentFileName = currentFileName.split("/")[-1]
    outputFileName = currentFileName + ".hack"
    return open(outputFileName, "x")

def main():

    assembly = Parser(sys.argv[1])
    binary = output()

    while assembly.hasMoreCommands():
    
        assembly.advance()

        if assembly.isC():
            comp = Code.comp(assembly.comp())
            dest = Code.dest(assembly.dest())
            jump = Code.jump(assembly.jump())

            binaryLine = '111' + comp + dest + jump + '\n'
            binary.write(binaryLine)

        elif assembly.isA():
            symbol ="{0:>015b}".format(int(assembly.symbol()))
            binaryLine = '0' + symbol + '\n'
            binary.write(binaryLine)
        
        else:
            continue
    
    assembly.close()
    binary.close()
    print("Assembler finished.")

if __name__ == "__main__":
    main()