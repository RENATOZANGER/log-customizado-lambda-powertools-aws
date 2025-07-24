import logging
import uuid
from zoneinfo import ZoneInfo
import boto3
from aws_lambda_powertools import Logger
from datetime import datetime

boto3.set_stream_logger('botocore', level=logging.WARNING)
boto3.set_stream_logger('boto3', level=logging.WARNING)

logger = Logger(
  service="exemplo_lambda_log",
  log_uncaught_exceptions=True,
  datefmt="%d-%m-%Y %H:%M:%S.%F",
  log_record_order=[
    "function_name", "service", "location","timestamp",
    "level", "cold_start", "correlation_id", "message"
  ]
)
