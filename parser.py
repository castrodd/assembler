class Parser:
    def __init__(self, path):
        self.file = open(path, 'r')
        self.originalCommands = self.file.readlines()
        self.commands = self.originalCommands.copy()
        self.currentCommand = None

    def resetCommands(self):
        self.commands = self.originalCommands.copy()
        self.currentCommand = None
    
    def hasMoreCommands(self):
        return len(self.commands) > 0
    
    def advance(self):
        if self.hasMoreCommands():
            self.currentCommand = self.commands.pop(0)
            return True
        return False
    
    def commandType(self):
        try:
            mostSignificantCharacter = self.currentCommand.strip()[0]
        except:
            return None
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
    
    def isL(self):
        return self.commandType() == "L_COMMAND"

    def symbol(self):
        command = self.currentCommand.split("/")[0]
        currentCommandType = self.commandType()
        if currentCommandType == "A_COMMAND":
            return command.strip().replace("@", "")
        elif currentCommandType == "L_COMMAND":
            symbol = command.strip().replace("(", "")
            return symbol.replace(")", "").rstrip()
        return None
    
    def dest(self):
        command = self.currentCommand.split("/")[0]
        if "=" in command:
            return command.strip().split("=")[0]
        return None
    
    def comp(self):
        command = self.currentCommand.split("/")[0]
        if "=" in self.currentCommand:
            return command.strip().split("=")[1]
        elif ";" in self.currentCommand:
            return command.strip().split(";")[0]
        return None
    
    def jump(self):
        command = self.currentCommand.split("/")[0]
        if ";" in command:
            return command.strip().split(";")[1]
        return None

    def close(self):
        if self.file:
            self.file.close()