from unidecode import unidecode
from nltk.corpus import stopwords

class SimilarNames():

    def allNames(self):
        self.dictNames = {}
        for name in self.df[self.names].unique():
            self.dictNames[name] = self.normName(name)

    def uniqueNames(self):
        self.similarList = []
        for name in self.dictNames.keys():
            self.similarList += [self.getSimilar(self.dictNames[name])]
        
        self.uniqueList = []
        for elem in self.similarList:
            if elem not in self.uniqueList:
                self.uniqueList.append(elem)

    def closeMatches(self, obj, names, sep, connectors, languages, customWords):
        self.sep = sep
        self.connectors = connectors

        self.stopList = []
        for l in languages:
            self.stopList += stopwords.words(l)
        self.stopList += customWords

        self.df = obj.copy()
        self.names = names

        if self.sep != None:
            self.df[self.names] = [self.nameSplit(x) for x in self.df[self.names]]
            self.df = self.df.explode('Authors')
        self.df[self.names] = [x.strip() for x in self.df[self.names]]
        
        self.df['NormName'] = [self.normName(x) for x in self.df[self.names]]
        self.allNames()
        self.uniqueNames()
    
        self.df['CloseMatches'] = [self.getSimilar(x) for x in self.df['NormName']]

        self.df['CloseMatches'] = [self.getMaxList(x) for x in self.df['CloseMatches']]

        self.df['StandardName'] = [self.getMinName(x) for x in self.df['CloseMatches']]
        
        self.df.drop(columns = 'NormName', inplace = True)
        
        return self.df

    def nameSplit(self, name):
        for c in self.connectors:
            name = name.replace(f' {c} ', ', ')
        return name.split(self.sep)

    def maxList(self, name):
        maxList = name
        for dup in self.uniqueList:
            if len(set(name).intersection(dup)) >= 2 and len(dup) > len(name):
                maxList = dup
        return maxList   

    def lowName(names):
        minName = names[0]
        for name in names:
            if len(name) < len(minName):
                minName = name
        return minName

    def normName(self, name):
        name = unidecode(name.lower()).replace('-',' ').replace('.', '').split()
        name = [x for x in name if x not in self.stopList and len(x) > 1]
        return name

    def getSimilar(self, name):
        similarList = []    
        for n in self.dictNames.keys():
            if name[0] == self.dictNames[n][0] and len(set(name).intersection(self.dictNames[n])) >= 2:
                similarList += [n]
        if len(similarList) < 1:
            return [f'Not found: {name}']
        else:
            return similarList

    def getMaxList(self, names):
        maxList = names
        for dup in self.uniqueList:
            if len(set(names).intersection(dup)) >= 2 and len(dup) > len(names):
                maxList = dup
        return maxList

    def getMinName(self, names):
        minName = names[0]
        for name in names:
            if len(name) < len(minName):
                minName = name
        return minName