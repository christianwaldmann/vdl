class FileParser:
    def __init__(self, filepath):
        self.filepath = filepath

    def GetNonEmptyLinesAsList(self):
        with open(self.filepath, "r") as f:
            return [line for line in f.readlines() if line and line != "\n"]
