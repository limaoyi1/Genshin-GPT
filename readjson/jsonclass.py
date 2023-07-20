class Dialog:
    def __init__(self, id, fileName, language, npcName, text, type):
        self.id = id
        self.fileName = fileName
        self.language = language
        self.npcName = npcName
        self.text = text
        self.type = type


class Handed:
    def __init__(self, language, npcName, text, type):
        self.language = language
        self.npcName = npcName
        self.text = text
        self.type = type