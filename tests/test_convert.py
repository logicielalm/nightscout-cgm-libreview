from datetime import datetime
from typing import List
from unittest.mock import Mock
from zoneinfo import ZoneInfo
import pytest
from app.convert import convert_to_glucose_data_list
from app.libreview.glucose_data_result import GlucoseDataResult
from app.libreview.glucose_data_result_item_result import GlucoseDataResultItemResult

@pytest.fixture
def mock_glucose_data():
    mockResponse = Mock()
    mockResponse.status_code = 200
    mock = Mock()
    mock.response = mockResponse
    mock.glucose_values: List[GlucoseDataResultItemResult] = [ # type: ignore
        GlucoseDataResultItemResult(
            valueInMgPerDl=120,
            timestamp="7/25/2025 9:35:16 PM"
        ),
        GlucoseDataResultItemResult(
            valueInMgPerDl=140,
            timestamp="7/26/2025 10:15:00 PM"
        )
    ]

    return mock #GlucoseDataResult(glucose_values=glucose_values)

def test_convert_to_glucose_data_list_success(mock_glucose_data):
    # Arrange
    timezone = ZoneInfo("America/Montreal")
    
    # Act
    result = convert_to_glucose_data_list(mock_glucose_data, timezone)
    
    # Assert
    assert len(result) == 2
    
    # Check first entry
    assert result[0].sgv == 120
    assert result[0].type == "sgv"
    assert result[0].device == "librelink-python"
    assert result[0].date == 1753493716000

    # Check second entry
    assert result[1].sgv == 140
    assert result[1].type == "sgv"
    assert result[1].device == "librelink-python"
    assert result[1].date == 1753582500000

def test_convert_to_glucose_data_list_empty():
    # Arrange
    mockResponse = Mock()
    mockResponse.status_code = 200
    empty_glucose_data = Mock()
    empty_glucose_data.response = mockResponse
    empty_glucose_data.glucose_values: List[GlucoseDataResultItemResult] = []
    timezone = ZoneInfo("America/Montreal")
    
    # Act
    result = convert_to_glucose_data_list(empty_glucose_data, timezone)
    
    # Assert
    assert len(result) == 0

def test_convert_to_glucose_data_list_timezone_conversion():
    # Arrange
    mockResponse = Mock()
    mockResponse.status_code = 200
    glucose_data = Mock()
    glucose_data.response = mockResponse
    glucose_data.glucose_values: List[GlucoseDataResultItemResult] = [
        GlucoseDataResultItemResult(
            valueInMgPerDl=120,
            timestamp="7/25/2025 9:35:16 PM"
        )
    ]

    
    # Test with different timezones
    montreal_tz = ZoneInfo("America/Montreal")
    utc_tz = ZoneInfo("UTC")
    
    # Act
    montreal_result = convert_to_glucose_data_list(glucose_data, montreal_tz)[0]
    utc_result = convert_to_glucose_data_list(glucose_data, utc_tz)[0]
    
    # Assert
    assert montreal_result.date != utc_result.date  # Times should be different due to timezone
    time_diff = abs(montreal_result.date - utc_result.date)
    assert time_diff > 0  # Should have some time difference