class Parser:
    def __init__(self, path):
        self.file = open(path, 'r')
        self.commands = self.file.readlines()
        self.currentCommand = None
    
    def hasMoreCommands(self):
        return len(self.commands) > 0
    
    def advance(self):
        if self.hasMoreCommands():
            self.currentCommand = self.commands.pop(0)
            return True
        return False
    
    def commandType(self):
        mostSignificantCharacter = self.currentCommand[0]
        if mostSignificantCharacter == "@":
            return "A_COMMAND"
        elif mostSignificantCharacter == "(":
            return "L_COMMAND"
        elif mostSignificantCharacter == "/":
            return None
        elif mostSignificantCharacter.isspace():
            return None
        else:
            return "C_COMMAND"
    
    def isC(self):
        return self.commandType() == "C_COMMAND"
    
    def isA(self):
        return self.commandType() == "A_COMMAND"
    
    def symbol(self):
        currentCommandType = self.commandType()
        if currentCommandType == "A_COMMAND":
            return self.currentCommand[1:]
        elif currentCommandType == "L_COMMAND":
            return self.currentCommand[1:-1]
        return None
    
    def dest(self):
        if "=" in self.currentCommand:
            return self.currentCommand.split("=")[0]
        return None
    
    def comp(self):
        if "=" in self.currentCommand:
            return self.currentCommand.split("=")[1]
        elif ";" in self.currentCommand:
            return self.currentCommand.split(";")[0]
        return None
    
    def jump(self):
        if ";" in self.currentCommand:
            return self.currentCommand.split(";")[1]
        return None

    def close(self):
        if self.file:
            self.file.close()