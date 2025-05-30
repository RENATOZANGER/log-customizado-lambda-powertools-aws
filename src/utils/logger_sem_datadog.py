# import logging
# import uuid
# from logging import LogRecord
# from zoneinfo import ZoneInfo
#
# import boto3
# from aws_lambda_powertools import Logger
# from datetime import datetime
# from aws_lambda_powertools.logging.formatter import LambdaPowertoolsFormatter
#
# boto3.set_stream_logger('botocore', level=logging.WARNING)
# boto3.set_stream_logger('boto3', level=logging.WARNING)
#
# class CustomFormatter(LambdaPowertoolsFormatter):
#     def serialize(self, log: LogRecord) -> str:
#         # remover logs relacionados ao datadog
#         datadog_keys = [key for key in log.keys() if key.startswith("dd.")]
#         for key in datadog_keys:
#             log.pop(key)
#         return self.json_serializer(log)
#
# logger = Logger(service="exemplo_lambda_log",
#                 log_uncaught_exceptions=True,
#                 logger_formatter=CustomFormatter(),
#                 )
#
# def log_customizado():
#     logger.remove_keys(
#         ["function_memory_size", "function_arn", "timestamp","function_request_id"]
#     )
#
#     logger.append_keys(
#         timestamp_br=datetime.now(tz=ZoneInfo("America/Sao_Paulo")).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
#         correlation_id=str(uuid.uuid4())
#     )
