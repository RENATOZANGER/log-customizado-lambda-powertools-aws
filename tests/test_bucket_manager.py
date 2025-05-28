from moto import mock_aws
import boto3
from src.bucket_s3.bucket_manager import BucketManager

@mock_aws
def test_list_buckets_returns_bucket_names():
    # Arrange
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="test-bucket-1")
    s3.create_bucket(Bucket="test-bucket-2")

    manager = BucketManager()

    # Act
    buckets = manager.list_buckets_s3()

    # Assert
    assert "test-bucket-1" in buckets
    assert "test-bucket-2" in buckets
    assert len(buckets) == 2


@mock_aws
def test_list_buckets_returns_empty_list():
    # Arrange
    manager = BucketManager()

    # Act
    buckets = manager.list_buckets_s3()

    # Assert
    assert buckets == []
