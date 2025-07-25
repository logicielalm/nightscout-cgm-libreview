import pytest
from unittest.mock import Mock, patch
from app.nightscout.nightscout_client import NightscoutClient

@pytest.fixture
def nightscout_client():
    return NightscoutClient("https://nightscout.test", "test-api-secret")

@pytest.fixture
def mock_glucose_data():
    return {
        "data": {
            "graphData": [{
                "ValueInMgPerDl": 120,
                "Timestamp": "2023-07-25T10:00:00Z"
            }]
        }
    }

# def test_upload_entries_success(nightscout_client, mock_glucose_data):
#     with patch('requests.post') as mock_post:
#         mock_response = Mock()
#         mock_response.status_code = 200
#         mock_post.return_value = mock_response

#         result = nightscout_client.upload_entries(mock_glucose_data)
#         assert result.status_code == 200

# def test_format_entries(nightscout_client, mock_glucose_data):
#     entries = nightscout_client._format_entries(mock_glucose_data)
#     assert isinstance(entries, list)
#     assert len(entries) > 0

# @pytest.mark.parametrize("api_secret", ["test_secret", None])
# def test_nightscout_client_headers(api_secret):
#     client = NightscoutClient("https://nightscout.test", api_secret)
#     headers = client.get_headers()  # Changed from _get_headers to get_headers
    
#     assert "Content-Type" in headers
#     assert headers["Content-Type"] == "application/json"
    
#     if api_secret:
#         assert "API-SECRET" in headers
#     else:
#         assert "API-SECRET" not in headers