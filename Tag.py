class Tag:
    def __init__(self, name, keyPhrases):
        self.name = name
        self.keyPhrases = keyPhrases
    
    def isin(self, betaling):
        for phrase in self.keyPhrases:
            try:
                if phrase.lower() in betaling.forklaring.lower():
                    return True
            except:
                continue
        
        return False


class Tags(list):
    def __init__(self, items=None):
        if items is None:
            items = []
        super().__init__(items)
    
    def getTags(self):
        tagList = []
        for tag in self:
            tagList.append(tag.name)
        return tagList
    
    def containsName(self, tagname):
        for tag in self:
            if tag.name == tagname:
                return True
        return False
    
    def containsNameList(self, tagnameList):
        for tagName in tagnameList:
            for tag in self:
                if tag.name == tagName:
                    return True
        return False
    