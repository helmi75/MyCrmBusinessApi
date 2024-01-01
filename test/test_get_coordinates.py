import pytest
from unittest.mock import patch, MagicMock
import os
import sys

# Obtenez le chemin absolu du répertoire parent à partir de l'emplacement du script
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Ajoutez le chemin du répertoire parent au chemin de recherche de Python
sys.path.insert(0, parent_dir)

from utils.distance_calculator import get_coordinates

@pytest.fixture
def mock_requests_get():
    with patch('requests.get') as mock_get:
        yield mock_get

def test_get_coordinates_success(mock_requests_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_data = {
        'features': [
            {'geometry': {'coordinates': [1.23, 4.56]}}
        ]
    }
    mock_response.json.return_value = mock_data
    mock_requests_get.return_value = mock_response

    address = '123 Main St'
    result = get_coordinates(address)

    expected_coordinates = [4.56, 1.23]  # Inverted order
    assert result == expected_coordinates

def test_get_coordinates_no_features(mock_requests_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_data = {
        'features': []
    }
    mock_response.json.return_value = mock_data
    mock_requests_get.return_value = mock_response

    address = '456 Elm St'
    result = get_coordinates(address)

    assert result is None

