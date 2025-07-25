from datetime import datetime
import pytest
from unittest.mock import Mock, patch
from app.libreview.libreview_client import LibreViewClient
from app.libreview.auth_info_result import AuthInfoResult
from app.libreview.glucose_data_result import GlucoseDataResult

@pytest.fixture
def libreview_client():
    return LibreViewClient("https://api.libreview.test")

@pytest.fixture
def mock_login_response():
    mock = Mock()
    mock.status_code = 200
    mock.json.return_value = {
        "data": {
            "authTicket": {
                "token": "test-token",
                "expires": "1769025102"
            },
            "user": {
                "id": "test-user-id"
            }
        }
    }
    return mock

@pytest.fixture
def mock_response_get_glucose_data():
    mock = Mock()
    mock.status_code = 200
    mock.json.return_value = {
        "data": {
            "graphData": [{
                "ValueInMgPerDl": 120,
                "Timestamp": "2023-07-25T10:00:00Z"
            }]
        }
    }
    return mock

def test_librelink_login_success(libreview_client, mock_login_response):
    with patch('app.libreview.libreview_client.requests.post', return_value=mock_login_response):
        result = libreview_client.librelink_login("test@test.com", "password")
        
        assert isinstance(result, AuthInfoResult)
        assert result.success is True
        assert result.user_id == "test-user-id"
        assert result.token == "test-token"
        assert result.expires == datetime.fromtimestamp(1769025102)
        

def test_get_glucose_data_success(libreview_client, mock_response_get_glucose_data):
    with patch('app.libreview.libreview_client.requests.get', return_value=mock_response_get_glucose_data):
        auth_info = Mock()
        auth_info.user_id = "test-user-id"
        auth_info.token = "test-token"
        
        result = libreview_client.get_glucose_data(auth_info)
        assert isinstance(result, GlucoseDataResult)
        assert len(result.glucose_values) == 1

@pytest.mark.parametrize("status_code", [400, 401, 403, 500])
def test_librelink_login_error(libreview_client, status_code):
    mock_error_response = Mock()
    mock_error_response.status_code = status_code
    mock_error_response.raise_for_status.side_effect = Exception("API Error")

    with patch('app.libreview.libreview_client.requests.post', return_value=mock_error_response):
        with pytest.raises(Exception):
            libreview_client.librelink_login("test@test.com", "password")