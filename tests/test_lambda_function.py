from unittest.mock import patch, MagicMock
from lambda_function import lambda_handler


@patch("lambda_function.BucketManager")
def test_lambda_handler_success(mock_bucket_manager_class):
    # Arrange
    mock_bucket_manager = MagicMock()
    mock_bucket_manager.list_buckets_s3.return_value = ["bucket1", "bucket2"]
    mock_bucket_manager_class.return_value = mock_bucket_manager
    
    fake_event = {"test": "value"}
    fake_context = MagicMock()
    
    # Act
    result = lambda_handler(fake_event, fake_context)
    
    # Assert
    assert result["statusCode"] == 200
    assert "bucket1" in result["body"]["buckets"]


@patch("lambda_function.BucketManager")
def test_lambda_handler_failure(mock_bucket_manager_class):
    # Arrange
    mock_bucket_manager = MagicMock()
    mock_bucket_manager.list_buckets_s3.side_effect = Exception("Erro simulado")
    mock_bucket_manager_class.return_value = mock_bucket_manager
    
    fake_event = {}
    fake_context = MagicMock()
    
    # Act
    result = lambda_handler(fake_event, fake_context)
    
    # Assert
    assert result["statusCode"] == 500
    assert "erro" in result["body"]
