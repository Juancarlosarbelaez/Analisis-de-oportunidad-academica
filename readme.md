# Instrucciones de uso del proyecto

## Preparación del entorno

1. Crear el entorno virtual:

```bash
python -m venv venv
```

2. Activarlo (Linux / macOS - bash/zsh):

```bash
source venv/bin/activate
# alternativa: usar ". venv/bin/activate"
```

3. Instalar dependencias:

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
OPENAI_API_KEY=tu_clave...
```

- Para Azure OpenAI:

```
AZURE_OPENAI_API_KEY=tu_clave_azure
