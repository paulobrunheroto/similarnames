from unidecode import unidecode
from nltk.corpus import stopwords

class SimilarNames():

    def all_names(self):
        self.dict_names = {}
        for name in self.df[self.names].unique():
            self.dict_names[name] = self.norm_name(name)

    def unique_names(self):
        self.similar_list = []
        for name in self.dict_names.keys():
            self.similar_list += [self.get_similar(self.dict_names[name])]
        
        self.unique_list = []
        for elem in self.similar_list:
            if elem not in self.unique_list:
                self.unique_list.append(elem)

    def close_matches(self, obj, names, sep, connectors, languages, custom_words):
        self.sep = sep
        self.connectors = connectors

        self.stop_list = []
        for l in languages:
            self.stop_list += stopwords.words(l)
        self.stop_list += custom_words

        self.df = obj.copy()
        self.names = names

        if self.sep != None:
            self.df[self.names] = [self.name_split(x) for x in self.df[self.names]]
            self.df = self.df.explode('Authors')
        
        self.df['norm_name'] = [self.norm_name(x) for x in self.df[self.names]]
        self.all_names()
        self.unique_names()
    
        self.df['close_matches'] = [self.get_similar(x) for x in self.df['norm_name']]

        self.df['close_matches'] = [self.get_max_list(x) for x in self.df['close_matches']]

        self.df['StandardName'] = [self.get_min_name(x) for x in self.df['close_matches']]
        
        self.df.drop(columns = 'norm_name', inplace = True)
        
        return self.df

    def name_split(self, name):
        for c in self.connectors:
            name = name.replace(f' {c} ', ', ')
        return [x.strip() for x in name.split(self.sep)]

    def low_name(self, names):
        min_name = names[0]
        for name in names:
            if len(name) < len(min_name):
                min_name = name
        return min_name

    def norm_name(self, name):
        name = unidecode(name.lower()).replace('-',' ').replace('.', '').split()
        name = [x.strip() for x in name if x not in self.stop_list and len(x) > 1]
        return name

    def get_similar(self, name):
        similar_list = []    
        for n in self.dict_names.keys():
            if name[0] == self.dict_names[n][0] and len(set(name).intersection(self.dict_names[n])) >= 2:
                similar_list += [n]
        if len(similar_list) < 1:
            return [f'Not found: {name}']
        else:
            return similar_list

    def get_max_list(self, names):
        max_list = names
        for dup in self.unique_list:
            if len(set(names).intersection(dup)) >= 2 and len(dup) > len(names):
                max_list = dup
        return max_list

    def get_min_name(self, names):
        min_name = names[0]
        for name in names:
            if len(name) < len(min_name):
                min_name = name
        return min_name