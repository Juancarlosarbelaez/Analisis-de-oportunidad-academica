"""Model Configuration

Carga la API key desde un archivo `.env` de forma robusta (busca junto
al módulo y luego en el directorio de trabajo).  También permite usar una
variable de entorno alternativa `OPENAI_API_KEY`.
"""
import os
from pathlib import Path
from strands.models.openai import OpenAIModel
from dotenv import load_dotenv

# Intentar cargar .env desde la ubicación del módulo, si existe; si no,
# fallback al .env del directorio de trabajo actual.
base_dir = Path(__file__).resolve().parent
env_path = base_dir / ".env"
if not env_path.exists():
    # find in cwd or parents
    env_path = Path.cwd() / ".env"
if env_path.exists():
    load_dotenv(env_path)
else:
    # última opción: carga por defecto (dejar que load_dotenv busque)
    load_dotenv()

# Prioriza AZURE_OPENAI_API_KEY, si no existe usa OPENAI_API_KEY
AZURE_KEY = os.getenv("AZURE_OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")


def get_configured_model() -> OpenAIModel:
    client_args = {
        "api_key": AZURE_KEY,
        # "api_version": '2024-12-01-preview',
        "base_url": 'https://pnl-maestria.openai.azure.com/openai/v1',
    }
    model = OpenAIModel(
        client_args=client_args,
        model_id="gpt-4.1-nano",
        params={"temperature": 0.2, "max_tokens": 10000},
    )
    return model


