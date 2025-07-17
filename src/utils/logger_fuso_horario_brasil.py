# import logging
# from zoneinfo import ZoneInfo
# from datetime import datetime, timezone
# import boto3
# from aws_lambda_powertools import Logger
# from aws_lambda_powertools.logging.formatter import LambdaPowertoolsFormatter

# # --- 1. Configurações Boto3 para reduzir ruído ---
# boto3.set_stream_logger('botocore', level=logging.WARNING)
# boto3.set_stream_logger('boto3', level=logging.WARNING)

# BRAZIL_TZ = ZoneInfo("America/Sao_Paulo")


# class CustomBrazilTimeFormatter(LambdaPowertoolsFormatter):
#     def formatTime(self, record, datefmt=None):
#         dt_utc = datetime.fromtimestamp(record.created, tz=timezone.utc)
#         dt_br_tz = dt_utc.astimezone(BRAZIL_TZ)
#         formatted_time = dt_br_tz.strftime("%d-%m-%Y %H:%M:%S")
#         milliseconds = f"{dt_br_tz.microsecond // 1000:03d}"  # Garante 3 dígitos
#         tz_offset = dt_br_tz.strftime("%z")  # Ex: -0300
#         return f"{formatted_time}.{milliseconds}{tz_offset}"
    
# logging.setLogRecordFactory(logging.LogRecord)

# logger = Logger(
#     service="exemplo_lambda_log",
#     log_uncaught_exceptions=True,
#     logger_formatter=CustomBrazilTimeFormatter(),
#     datefmt=None,
#     utc=False
# )
