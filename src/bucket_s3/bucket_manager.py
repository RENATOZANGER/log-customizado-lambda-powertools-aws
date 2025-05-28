import boto3
from botocore.exceptions import BotoCoreError, ClientError
from src.utils.logger import logger

class BucketManager:
    def __init__(self):
        self.s3_client = boto3.client("s3")
        
    def list_buckets_s3(self):
        logger.info("Iniciando listagem de buckets S3")
        try:
            response = self.s3_client.list_buckets()
            if not response.get("Buckets"):
                logger.warning("Nenhum bucket encontrado", extra={"payload": ""})
                return []
            bucket_names = [bucket["Name"] for bucket in response.get("Buckets", [])]
            logger.info("Buckets encontrados com sucesso", extra={"payload": bucket_names})
            return bucket_names
        except (BotoCoreError, ClientError) as e:
            logger.error("Erro ao listar buckets", extra={"payload": {"erro": str(e)}})
            raise
