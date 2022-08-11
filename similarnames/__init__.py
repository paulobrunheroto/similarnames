__version__ = '0.1.6'

from .similarnames import SimilarNames

def closeMatches(obj, names, sep = ',', connectors = ['and','e','y'], languages = ['english', 'portuguese', 'spanish'], customWords = None):
    if connectors == None:
        connectors = []
    else:
        if not isinstance(connectors, list):
            connectors = [connectors]

    if languages == None:
        languages = []
    else:
        if not isinstance(languages, list):
            languages = [languages]

    if customWords == None:
        customWords = []
    else:
        if not isinstance(customWords, list):
            customWords = [customWords]

    sn = SimilarNames()
    return sn.closeMatches(obj, names, sep, connectors, languages, customWords)