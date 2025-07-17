from src.bucket_s3.bucket_manager import BucketManager
from src.utils.logger import logger
import uuid

@logger.inject_lambda_context(log_event=False)
def lambda_handler(event, context):
    logger.remove_keys(["function_memory_size", "function_arn","function_request_id"])
    logger.append_keys(correlation_id=str(uuid.uuid4()))
    
    logger.info("Iniciando execução da função Lambda", extra={"Payload": event})
    
    bucket_manager = BucketManager()
    try:
        buckets = bucket_manager.list_buckets_s3()
        logger.info("Buckets retornados do manager", extra={"buckets": buckets})
        return {"statusCode": 200, "body": {"buckets": buckets}}
    except Exception as e:
        logger.exception("Erro geral no handler")
        return {"statusCode": 500, "body": {"erro": str(e)}}
