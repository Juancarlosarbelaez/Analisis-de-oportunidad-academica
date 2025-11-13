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

# Crear el archivo de ambiente para la API key
1. Copia el archivo de ejemplo:
```bash
cp .env.example .env
```
2. Abre `.env` y coloca tu API key (no subir este archivo al repositorio):
```
API_KEY=tu_api_key_aqui
```

Se incluye un archivo `.env.example` con las variables necesarias. Añade `.env` a tu `.gitignore` para evitar subirlo por error.

