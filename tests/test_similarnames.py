from similarnames import __version__
from similarnames import SimilarNames


def test_version():
    assert __version__ == '0.1.7'

def test_name_split():
    similar_names = SimilarNames()
    similar_names.connectors = ['and']
    similar_names.sep = ','
    name_list = ['John and Jane', 'John, Michael','Maria José and João Silva']

    name_result = []
    for name in name_list:
        name_result += [similar_names.name_split(name)]
    
    expected_result = [['John','Jane'], ['John', 'Michael'],['Maria José', 'João Silva']]
    assert name_result == expected_result

def test_get_max_list():
    similar_names = SimilarNames()
    similar_names.unique_list = [
        ['Joao Silva', 'Joao Siva Rodrigues', 'Joao S. Rodrigues'],
        ['Joao Siva Rodrigues', 'Joao S. Rodrigues'],
        ['Joao Silva', 'Joao Siva Rodrigues', 'Joao S. Rodrigues', 'Joao Silva R.'],
        ['Max Silva','Max Joao', 'Max Silva Rodrigues','Max S. Rodrigues', 'Joao Max Ribeiro']]

    name_result = similar_names.get_max_list(['Joao Silva', 'Joao S. Rodrigues'])
    expected_result = ['Joao Silva', 'Joao Siva Rodrigues', 'Joao S. Rodrigues', 'Joao Silva R.']

    assert name_result == expected_result

def test_low_name():
    similar_names = SimilarNames()
    names = ['Joao Silva', 'Joao Siva Rodrigues', 'Joao S. Rodrigues', 'Joao Silva R.']
    name_result = similar_names.low_name(names)
    expected_result = 'Joao Silva'

    assert name_result == expected_result

def test_norm_name():
    similar_names = SimilarNames()
    similar_names.stop_list = ['jr']
    name = 'João S. Caçá-lôe Jr.'
    name_result = similar_names.norm_name(name)
    expected_result = ['joao', 'caca', 'loe']

    assert name_result == expected_result

def test_get_min_name():
    similar_names = SimilarNames()
    names = ['Joao Silva', 'Joao Siva Rodrigues', 'Joao S. Rodrigues', 'Joao Silva R.']

    name_result = similar_names.get_min_name(names)
    expected_result = 'Joao Silva'

    assert name_result == expected_result   