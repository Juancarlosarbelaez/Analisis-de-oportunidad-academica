# Análisis de Oportunidad Académica

## Descripción

Repositorio para el análisis de tendencias de mercado académico utilizando agentes de inteligencia artificial. El sistema procesa datos de programas académicos y genera visualizaciones y reportes para identificar oportunidades de mercado.

## Contenido del Repositorio

- `programas_equivalentes.xlsx`: Base de datos de programas académicos equivalentes con información de matrículas, instituciones y características de los programas.
- `analisis_tendencias_ia.py`: Script principal que utiliza agentes de IA para analizar tendencias de mercado y generar visualizaciones.
- `lector_tablas_SNIES.ipynb`: Notebook para lectura y procesamiento de tablas SNIES.
- `Analisis_de_tendencias.ipynb`: Notebook de análisis de tendencias.

## Análisis con Agentes de IA

### Requisitos

Instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

O instalar manualmente:

```bash
pip install pandas openpyxl matplotlib seaborn numpy
```

### Uso

Ejecutar el script de análisis:

```bash
python3 analisis_tendencias_ia.py
```

### Funcionalidades

El script implementa cuatro agentes especializados:

1. **Agente de Análisis de Datos**: Carga y preprocesa los datos del archivo Excel.
2. **Agente de Tendencias de Mercado**: Identifica patrones y tendencias en:
   - Evolución temporal de matrícula
   - Tendencias por institución
   - Tendencias por programa académico
   - Distribución por sectores (público/privado)
   - Distribución por áreas de conocimiento

3. **Agente de Visualización**: Genera gráficas profesionales:
   - Tendencia temporal de matrícula
   - Top 10 instituciones por matrícula
   - Distribución de programas académicos
   - Distribución por sectores
   - Distribución por áreas de conocimiento
   - Dashboard completo con múltiples visualizaciones

4. **Agente de Recomendaciones**: Genera insights estratégicos y recomendaciones basadas en el análisis.

### Salidas Generadas

El script genera los siguientes archivos:

- `tendencia_temporal_matricula.png`: Gráfica de evolución temporal
- `top_instituciones_matricula.png`: Top 10 instituciones
- `distribucion_programas.png`: Distribución por programas
- `distribucion_sectores.png`: Distribución sector público/privado
- `distribucion_areas_conocimiento.png`: Distribución por áreas
- `dashboard_completo.png`: Dashboard integrado con todas las visualizaciones
- `reporte_analisis_tendencias.txt`: Reporte con insights y recomendaciones

### Ejemplo de Salida

Cuando se ejecuta el script, verás una salida similar a:

```
================================================================================
SISTEMA DE ANÁLISIS DE TENDENCIAS DE MERCADO CON AGENTES DE IA
================================================================================

📋 FASE 1: ANÁLISIS Y PREPROCESAMIENTO DE DATOS
🤖 Agente de Análisis: Cargando datos...
✓ Datos cargados: 177 registros, 44 columnas

📊 FASE 2: IDENTIFICACIÓN DE TENDENCIAS DE MERCADO
🤖 Agente de Tendencias: Analizando evolución temporal de matrículas...

📈 FASE 3: GENERACIÓN DE VISUALIZACIONES
🤖 Agente de Visualización: Creando gráfica de tendencia temporal...
✓ Gráfica guardada: tendencia_temporal_matricula.png

💡 FASE 4: GENERACIÓN DE INSIGHTS Y RECOMENDACIONES
✅ ANÁLISIS COMPLETADO EXITOSAMENTE
```

El reporte generado incluye insights como:
- Institución líder en matrícula
- Programas académicos más populares
- Distribución entre sectores público y privado
- Áreas de conocimiento dominantes
- Recomendaciones estratégicas para oportunidades de mercado

## Licencia

Este proyecto está bajo la licencia MIT.