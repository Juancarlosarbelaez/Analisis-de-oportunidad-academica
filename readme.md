# Primero crear el ambiente virtual
```bash
python -m venv venv
```

# Luego activarlo (Linux / macOS - bash/zsh)
```bash
source venv/bin/activate
# o de forma equivalente
. venv/bin/activate
```

# Instalar los requerimientos
```bash
pip install -r requirements.txt
```

## Crear el archivo de ambiente para las API keys

1. Copia el archivo de ejemplo:

```bash
cp .env.example .env
```

2. Abre `.env` y completa las variables según el proveedor que uses.

- Para OpenAI (API pública):

```
OPENAI_API_KEY=sk-...tu_clave...
```

- Para Azure OpenAI (si aplicas):

```
AZURE_OPENAI_KEY=tu_clave_azure
AZURE_OPENAI_ENDPOINT=https://<tu-recurso>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT_NAME=nombre_del_deployment
AZURE_OPENAI_REGION=region_opcional
```

3. Mantén tu `.env` fuera del control de versiones (ya está ignorado en `.gitignore`). Nunca subas claves reales al repositorio.

4. Cómo cargar las variables en tu sesión local (bash):

- Opción simple (exporta todas las variables del archivo):

```bash
set -o allexport; source .env; set +o allexport
```

- Opción con `grep` (ignora comentarios):

```bash
export $(grep -v '^#' .env | xargs)
```

- Opción desde Python con `python-dotenv` (recomendada cuando tu app lo soporte):

```python
# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv('.env')
```

5. Nota sobre prioridades: si usas Azure OpenAI, configura las variables `AZURE_...` y tu código debe preferirlas; si usas OpenAI público, usa `OPENAI_API_KEY`.

Se incluye un archivo `.env.example` con las variables necesarias. Añade `.env` a tu `.gitignore` para evitar subirlo por error.

