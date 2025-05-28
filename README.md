# AWS Lambda com Logging Customizado (AWS Lambda Powertools)

Este projeto demonstra uma função AWS Lambda com:

- **Log customizado** utilizando [AWS Lambda Powertools for Python](https://docs.powertools.aws.dev/lambda/python/latest/core/logger/)
- **Integração com S3** via `boto3`
- **Testes unitários** com `pytest` e `moto`
- **Geração de `correlation_id`**
- **Timestamp em horário de Brasília**

---
## 📦 Sobre o AWS Lambda Powertools

Este projeto utiliza o [AWS Lambda Powertools for Python](https://docs.powertools.aws.dev/lambda/python/latest/core/logger/) — uma biblioteca da AWS que fornece utilitários prontos para funções Lambda em produção.

### 🔧 Funcionalidades utilizadas:

- **Logger estruturado:** Geração automática de logs com informações da execução (cold start, function name, trace id, etc.)
- **Adição de campos customizados:** Como `correlation_id` e `timestamp_br` (data/hora com fuso de São Paulo)
- **Ordenação de chaves do log:** Usando o parâmetro `log_record_order`

---

## Estrutura do Projeto
```tree
├── src/
│ ├── bucket_s3/
│ │ └── bucket_manager.py
│ └── utils/
│ └── logger.py
├── tests/
│ └── test_lambda.py
├── lambda_handler.py
├── requirements.txt
└── README.md
```
---

## Exemplo de Log
```json
{
    "function_name": "example_lambda",
    "service": "exemplo_lambda_log",
    "location": "lambda_handler:8",
    "timestamp_br": "2025-05-27 08:42:48.855",
    "level": "INFO",
    "cold_start": true,
    "correlation_id": "9e9f5b0c-3c4a-4f66-8b68-9c93d25a8df3",
    "xray_trace_id": "1-6835a537-22019900499cbe4018173699",
    "message": "Iniciando execução da função Lambda"
}
```
---

## Requisitos
- Python 3.8+
- AWS CLI configurado (opcional)
- Virtualenv recomendado
---

## Instalação
```bash
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
pip install -r requirements.txt
```
---

## Executando os Testes
```bash
pytest tests/
```
