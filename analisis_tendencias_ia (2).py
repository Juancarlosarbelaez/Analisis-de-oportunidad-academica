import asyncio
import sys

from strands import Agent
from model_config import get_configured_model

# Importamos los agentes y el factory de herramientas
from agents import (
    AgenteAnalisisDatos,
    AgenteTendenciasMercado,
    AgenteVisualizacion,
    AgenteRecomendaciones,
    AgentePresentacion,
)
from agents.strands_tools import make_tools_registry


def main():
    """Punto de entrada: crea el contexto, registra las herramientas y ejecuta el Planner."""
    # Contexto compartido entre herramientas
    global _context
    _context = {}

    archivo_excel = 'programas_equivalentes.xlsx'

    # Crear registry de herramientas ligado al contexto
    tools_registry = make_tools_registry(_context, archivo_excel)

    planner_instructions = (
        "Eres un PLANNER responsable de coordinar un análisis de tendencias "
        "de mercado académico.  Deberás invocar las herramientas en el "
        "orden correcto: (1) carga y preprocesamiento de datos, (2) "
        "identificación de tendencias, (3) generación de visualizaciones, "
        "(4) insights y recomendaciones, y (5) creación de la presentación."
    )

    planner = Agent(
        model=get_configured_model(),
        name="Planner",
        system_prompt=planner_instructions,
        tools=[
            tools_registry.herramienta_carga_y_preprocesamiento,
            tools_registry.herramienta_identificacion_tendencias,
            tools_registry.herramienta_generacion_visualizaciones,
            tools_registry.herramienta_insights_y_recomendaciones,
            tools_registry.herramienta_generar_presentacion,
        ],
    )

    print("\n" + "=" * 80)
    print("SISTEMA DE ANÁLISIS DE TENDENCIAS DE MERCADO CON AGENTES DE IA")
    print("=" * 80)
    print("Iniciando ejecución a través del Planner de strands...")
    print("=" * 80 + "\n")

    try:
        resultado = planner("Iniciar análisis de tendencias de mercado académico")
        print("\n" + str(resultado))
    except Exception as e:
        print("Error durante la ejecución del Planner:", e, file=sys.stderr)
        raise

    imagenes = _context.get('imagenes', [])
    print("\n" + "=" * 80)
    print("ANÁLISIS COMPLETADO EXITOSAMENTE")
    print("=" * 80)
    print(f"\nArchivos generados:")
    for i, figura in enumerate(imagenes, 1):
        print(f"  {i}. {figura}")
    print(f"  {len(imagenes) + 1}. reporte_analisis_tendencias.txt")
    print(f"  {len(imagenes) + 2}. presentacion_analisis_tendencias.pptx")
    print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":
    main()