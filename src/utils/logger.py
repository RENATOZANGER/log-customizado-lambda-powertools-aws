import logging
import uuid
import boto3
from aws_lambda_powertools import Logger
from datetime import datetime
import pytz

boto3.set_stream_logger('botocore', level=logging.WARNING)
boto3.set_stream_logger('boto3', level=logging.WARNING)

logger = Logger(service="exemplo_lambda_log",
                log_uncaught_exceptions=True,
                log_record_order=[
                    "function_name", "service", "location","timestamp_br",
                     "level", "cold_start", "correlation_id", "xray_trace_id", "message"
                    ]
                )

def log_customizado():
    logger.remove_keys(
        ["function_memory_size", "function_arn", "timestamp","function_request_id"]
    )
    
    logger.append_keys(
        timestamp_br=datetime.now(tz=pytz.timezone("America/Sao_Paulo")).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
        correlation_id=str(uuid.uuid4())
    )
