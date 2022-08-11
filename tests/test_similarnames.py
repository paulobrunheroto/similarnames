from similarnames import __version__
from similarnames import SimilarNames


def test_version():
    assert __version__ == '0.1.6'

def test_nameSplit():
    similarNames = SimilarNames()
    similarNames.connectors = ['and']
    similarNames.sep = ','
    nameList = ['John and Jane', 'John, Michael','Maria José and João Silva']

    nameResult = []
    for name in nameList:
        nameResult += [similarNames.nameSplit(name)]
    
    expectedResult = [['John','Jane'], ['John', 'Michael'],['Maria José', 'João Silva']]
    assert nameResult == expectedResult

def test_getMaxList():
    similarNames = SimilarNames()
    similarNames.uniqueList = [
        ['Joao Silva', 'Joao Siva Rodrigues', 'Joao S. Rodrigues'],
        ['Joao Siva Rodrigues', 'Joao S. Rodrigues'],
        ['Joao Silva', 'Joao Siva Rodrigues', 'Joao S. Rodrigues', 'Joao Silva R.'],
        ['Max Silva','Max Joao', 'Max Silva Rodrigues','Max S. Rodrigues', 'Joao Max Ribeiro']]

    nameResult = similarNames.getMaxList(['Joao Silva', 'Joao S. Rodrigues'])
    expectedResult = ['Joao Silva', 'Joao Siva Rodrigues', 'Joao S. Rodrigues', 'Joao Silva R.']

    assert nameResult == expectedResult

def test_lowName():
    similarNames = SimilarNames()
    names = ['Joao Silva', 'Joao Siva Rodrigues', 'Joao S. Rodrigues', 'Joao Silva R.']
    nameResult = similarNames.lowName(names)
    expectedResult = 'Joao Silva'

    assert nameResult == expectedResult

def test_normName():
    similarNames = SimilarNames()
    similarNames.stopList = ['jr']
    name = 'João S. Caçá-lôe Jr.'
    nameResult = similarNames.normName(name)
    expectedResult = ['joao', 'caca', 'loe']

    assert nameResult == expectedResult

def test_getMinName():
    similarNames = SimilarNames()
    names = ['Joao Silva', 'Joao Siva Rodrigues', 'Joao S. Rodrigues', 'Joao Silva R.']

    nameResult = similarNames.getMinName(names)
    expectedResult = 'Joao Silva'

    assert nameResult == expectedResult   