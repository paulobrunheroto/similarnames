__version__ = '0.1.7'

from .similarnames import SimilarNames

def close_matches(obj, names, sep = ',', connectors = ['and','e','y'], languages = ['english', 'portuguese', 'spanish'], custom_words = None):
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

    if custom_words == None:
        custom_words = []
    else:
        if not isinstance(custom_words, list):
            custom_words = [custom_words]

    sn = SimilarNames()
    return sn.close_matches(obj, names, sep, connectors, languages, custom_words)