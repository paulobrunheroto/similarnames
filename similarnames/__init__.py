__version__ = '0.1.3'

from .similarnames import SimilarNames

def closeMatches(obj, names, sep = ','):
    sn = SimilarNames()
    return sn.closeMatches(obj, names, sep)