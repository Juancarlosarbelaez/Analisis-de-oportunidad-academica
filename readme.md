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
OPENAI_API_KEY=sk-...tu_clave...
```

- Para Azure OpenAI:

```
AZURE_OPENAI_API_KEY=tu_clave_azure
AZURE_OPENAI_KEY=tu_clave_azure    # alternativa de nombre
AZURE_OPENAI_ENDPOINT=https://<tu-recurso>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT_NAME=nombre_del_deployment
```

3. Mantén tu `.env` fuera del control de versiones (ya está ignorado en `.gitignore`). Nunca subas claves reales al repositorio.

4. Carga las variables en tu sesión (bash):

```bash
set -o allexport; source .env; set +o allexport
```

Otras alternativas:

```bash
export $(grep -v '^#' .env | xargs)
```

O desde Python usando `python-dotenv`:

```python
from dotenv import load_dotenv
load_dotenv('.env')
```

## Ejecución del script `analisis_tendencias_ia (2).py`

1. Asegúrate de que el entorno virtual esté activado y las dependencias instaladas.

2. Asegúrate de haber creado y cargado `.env` (ver sección anterior).

3. Ejecuta el script. El nombre contiene espacios y paréntesis — usa comillas:

```bash
python "analisis_tendencias_ia (2).py"
```

4. Salida y ubicación de resultados:
- El script imprime progreso en consola.
- Puede generar `reporte_analisis_tendencias.txt` en el directorio del proyecto.

## Notas sobre configuración de modelo (Azure vs OpenAI público)

- Si usas OpenAI público (platform.openai.com), define `OPENAI_API_KEY`.
- Si usas Azure OpenAI, define `AZURE_OPENAI_API_KEY` (o `AZURE_OPENAI_KEY`), `AZURE_OPENAI_ENDPOINT` y `AZURE_OPENAI_DEPLOYMENT_NAME`.

El archivo `model_config.py` del proyecto ya intenta leer estas variables y construir el `base_url` necesario para la librería. Si proporcionas `AZURE_OPENAI_ENDPOINT` como `https://mi-recurso.openai.azure.com`, el código añadirá `/openai/v1` automáticamente si es necesario.

## Solución de errores comunes

- Error 401: "Access denied due to invalid subscription key or wrong API endpoint"
  - Causa: clave inválida o endpoint incorrecto para Azure.
  - Pasos de diagnóstico:
    1. Verifica las variables en tu sesión:

    ```python
    import os
    print('AZURE_KEY:', bool(os.getenv('AZURE_OPENAI_API_KEY') or os.getenv('AZURE_OPENAI_KEY')))
    print('AZURE_ENDPOINT:', os.getenv('AZURE_OPENAI_ENDPOINT'))
    print('DEPLOYMENT:', os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME'))
    print('OPENAI_KEY:', bool(os.getenv('OPENAI_API_KEY')))
    ```

    2. Verifica en el Portal de Azure que la clave esté activa y que el recurso sea del tipo correcto (Azure OpenAI / Cognitive Services según tu configuración).
    3. Asegúrate de usar el `AZURE_OPENAI_ENDPOINT` correcto (ej. `https://mi-recurso.openai.azure.com`). No incluyas rutas extra si ya las añadió el código.
    4. Si la clave se ha filtrado accidentalmente, rótala desde el portal de Azure / OpenAI.

- Error por nombre de deployment/model inválido
  - Asegúrate de que `AZURE_OPENAI_DEPLOYMENT_NAME` sea exactamente el nombre del deployment que creaste en Azure.

## Comprobaciones rápidas desde consola

```bash
# Ver variables cargadas
python - <<'PY'
import os
print('AZURE_KEY set:', bool(os.getenv('AZURE_OPENAI_API_KEY') or os.getenv('AZURE_OPENAI_KEY')))
print('AZURE_ENDPOINT:', os.getenv('AZURE_OPENAI_ENDPOINT'))
print('OPENAI_KEY set:', bool(os.getenv('OPENAI_API_KEY')))
PY
```

## Seguridad

- Si detectas que alguna clave fue subida al repositorio, bórrala y rótala inmediatamente desde Azure/OpenAI.
- No incluyas claves en commits futuros; usa `.env` local y `.env.example` para documentar nombres de variables.

---

Si quieres, puedo:

- Añadir un pequeño script `scripts/check_env.sh` que valide las variables necesarias antes de ejecutar.
- Integrar una comprobación al inicio del `analisis_tendencias_ia (2).py` para mostrar errores claros si faltan variables.

Dime qué prefieres y lo agrego.
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

