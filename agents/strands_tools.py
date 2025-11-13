import asyncio
from strands import tool
from typing import Any

from agents import (
    AgenteAnalisisDatos,
    AgenteTendenciasMercado,
    AgenteVisualizacion,
    AgenteRecomendaciones,
    AgentePresentacion,
)


def make_tools_registry(context: dict, archivo_excel: str):
    """Factory que crea un objeto con herramientas decoradas con `@tool`.

    Cada herramienta actualiza `context` (diccionario compartido) y devuelve
    un mensaje de estado. Se devuelve la instancia para que el planner la
    registre pasando los métodos ligados (`bound methods`).
    """

    class Tools:
        def __init__(self, ctx: dict, archivo: str):
            self._context = ctx
            self.archivo_excel = archivo

        @tool
        def herramienta_carga_y_preprocesamiento(self, prompt: str) -> str:
            print("\n📋 FASE 1: ANÁLISIS Y PREPROCESAMIENTO DE DATOS")
            print("-" * 80)
            agente_datos = AgenteAnalisisDatos(self.archivo_excel)
            datos = agente_datos.cargar_datos()
            datos = agente_datos.preprocesar_datos()
            resumen = agente_datos.obtener_resumen_estadistico()
            self._context['datos'] = datos
            self._context['resumen'] = resumen
            return "✓ Datos cargados y preprocesados."

        @tool
        def herramienta_identificacion_tendencias(self, prompt: str) -> str:
            print("\n📊 FASE 2: IDENTIFICACIÓN DE TENDENCIAS DE MERCADO")
            print("-" * 80)
            datos = self._context.get('datos')
            if datos is None:
                return "⚠️ No se encontraron datos para analizar."
            agente_tendencias = AgenteTendenciasMercado(datos)
            asyncio.run(agente_tendencias.analizar_todo_concurrente())
            self._context['tendencias'] = agente_tendencias.tendencias
            return "✓ Tendencias identificadas."

        @tool
        def herramienta_generacion_visualizaciones(self, prompt: str) -> str:
            print("\n📈 FASE 3: GENERACIÓN DE VISUALIZACIONES")
            print("-" * 80)
            datos = self._context.get('datos')
            tendencias = self._context.get('tendencias')
            if datos is None or tendencias is None:
                return "⚠️ No se pueden generar visualizaciones por falta de datos o tendencias."
            agente_viz = AgenteVisualizacion(datos, tendencias)
            asyncio.run(agente_viz.crear_todas_graficas(top_n=10))
            self._context['imagenes'] = agente_viz.figuras
            return f"✓ Visualizaciones generadas ({len(agente_viz.figuras)} archivos)."

        @tool
        def herramienta_insights_y_recomendaciones(self, prompt: str) -> str:
            print("\n💡 FASE 4: GENERACIÓN DE INSIGHTS Y RECOMENDACIONES")
            print("-" * 80)
            datos = self._context.get('datos')
            tendencias = self._context.get('tendencias')
            if datos is None or tendencias is None:
                return "⚠️ No se pueden generar insights debido a datos incompletos."
            agente_recom = AgenteRecomendaciones(datos, tendencias)
            insights = agente_recom.generar_insights()
            recomendaciones = agente_recom.generar_recomendaciones_estrategicas()
            agente_recom.generar_reporte_completo(insights, recomendaciones)
            self._context['insights'] = insights
            self._context['recomendaciones'] = recomendaciones
            return f"✓ Insights y recomendaciones generados ({len(insights)} insights, {len(recomendaciones)} recomendaciones)."

        @tool
        def herramienta_generar_presentacion(self, prompt: str) -> str:
            print("\n🎞️ FASE 5: GENERACIÓN DE PRESENTACIÓN")
            print("-" * 80)
            resumen = self._context.get('resumen')
            tendencias = self._context.get('tendencias')
            insights = self._context.get('insights')
            recomendaciones = self._context.get('recomendaciones')
            imagenes = self._context.get('imagenes')
            if not all([resumen, tendencias, insights, recomendaciones, imagenes]):
                return "⚠️ La presentación no se puede generar por información incompleta."
            agente_presentacion = AgentePresentacion(
                resumen=resumen,
                tendencias=tendencias,
                insights=insights,
                recomendaciones=recomendaciones,
                imagenes=imagenes,
            )
            agente_presentacion.generar_presentacion("presentacion_analisis_tendencias.pptx")
            return "✓ Presentación generada."

    return Tools(context, archivo_excel)
