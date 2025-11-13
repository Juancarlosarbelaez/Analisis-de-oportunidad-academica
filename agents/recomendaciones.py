from datetime import datetime
from utils.io import write_report

class AgenteRecomendaciones:
    """
    Agente de IA especializado en generar insights y recomendaciones.
    Analiza los resultados y proporciona conclusiones estratégicas.
    """

    def __init__(self, datos, tendencias):
        self.datos = datos
        self.tendencias = tendencias
        self.recomendaciones = []

    def generar_insights(self):
        """Genera insights basados en el análisis de datos"""
        print("\n🤖 Agente de Recomendaciones: Generando insights...")

        insights = []

        # Insight 1: Institución líder
        if 'institucional' in self.tendencias and len(self.tendencias['institucional']) > 0:
            institucion_lider = self.tendencias['institucional'].index[0]
            matricula_lider = self.tendencias['institucional'].values[0]
            insights.append(f"📌 La institución líder en matrícula es '{institucion_lider}' "
                          f"con {int(matricula_lider):,} estudiantes matriculados.")

        # Insight 2: Programa más popular
        if 'programas' in self.tendencias and len(self.tendencias['programas']) > 0:
            programa_popular = self.tendencias['programas'].index[0]
            matricula_programa = self.tendencias['programas'].values[0]
            insights.append(f"📌 El programa académico más popular es '{programa_popular}' "
                          f"con {int(matricula_programa):,} estudiantes.")

        # Insight 3: Distribución sectorial
        if 'sectores' in self.tendencias and len(self.tendencias['sectores']) > 0:
            total_matricula = self.tendencias['sectores'].sum()
            for sector, matricula in self.tendencias['sectores'].items():
                porcentaje = (matricula / total_matricula) * 100
                insights.append(f"📌 El sector {sector} representa el {porcentaje:.1f}% "
                              f"de la matrícula total.")

        # Insight 4: Área de conocimiento dominante
        if 'areas' in self.tendencias and len(self.tendencias['areas']) > 0:
            area_dominante = self.tendencias['areas'].index[0]
            matricula_area = self.tendencias['areas'].values[0]
            insights.append(f"📌 El área de conocimiento dominante es '{area_dominante}' "
                          f"con {int(matricula_area):,} estudiantes.")

        return insights

    def generar_recomendaciones_estrategicas(self):
        """Genera recomendaciones estratégicas"""
        print("\n🤖 Agente de Recomendaciones: Generando recomendaciones estratégicas...")

        recomendaciones = []

        # Recomendación 1: Oportunidades de mercado
        if 'programas' in self.tendencias and len(self.tendencias['programas']) > 0:
            recomendaciones.append("💡 Oportunidad de Mercado: Los programas con mayor demanda "
                                 "representan áreas de alta oportunidad para inversión y expansión.")

        # Recomendación 2: Análisis competitivo
        if 'institucional' in self.tendencias and len(self.tendencias['institucional']) > 0:
            recomendaciones.append("💡 Análisis Competitivo: Las instituciones líderes marcan "
                                 "las tendencias del mercado. Estudiar sus estrategias puede "
                                 "proporcionar ventajas competitivas.")

        # Recomendación 3: Diversificación
        if 'areas' in self.tendencias and len(self.tendencias['areas']) > 1:
            recomendaciones.append("💡 Diversificación: Considerar la diversificación hacia "
                                 "múltiples áreas de conocimiento para mitigar riesgos y "
                                 "capturar diferentes segmentos de mercado.")

        # Recomendación 4: Sector público vs privado
        if 'sectores' in self.tendencias and len(self.tendencias['sectores']) > 0:
            recomendaciones.append("💡 Estrategia Sectorial: Analizar las diferencias entre "
                                 "sectores público y privado para identificar nichos "
                                 "específicos de oportunidad.")

        return recomendaciones

    def generar_reporte_completo(self, insights, recomendaciones):
        """Genera un reporte completo en formato texto"""
        print("\n🤖 Agente de Recomendaciones: Generando reporte completo...")

        reporte = []
        reporte.append("=" * 80)
        reporte.append("REPORTE DE ANÁLISIS DE TENDENCIAS DE MERCADO ACADÉMICO")
        reporte.append("=" * 80)
        reporte.append(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        reporte.append("")

        reporte.append("\n" + "=" * 80)
        reporte.append("INSIGHTS PRINCIPALES")
        reporte.append("=" * 80)
        for insight in insights:
            reporte.append(insight)

        reporte.append("\n" + "=" * 80)
        reporte.append("RECOMENDACIONES ESTRATÉGICAS")
        reporte.append("=" * 80)
        for rec in recomendaciones:
            reporte.append(rec)

        reporte.append("\n" + "=" * 80)
        reporte.append("CONCLUSIÓN")
        reporte.append("=" * 80)
        reporte.append("Este análisis proporciona una visión integral de las tendencias de mercado")
        reporte.append("en el sector académico. Las visualizaciones generadas permiten identificar")
        reporte.append("patrones clave, oportunidades de crecimiento y áreas de mejora estratégica.")
        reporte.append("=" * 80)

        # Guardar reporte
        write_report('reporte_analisis_tendencias.txt', reporte)
        print("✓ Reporte guardado: reporte_analisis_tendencias.txt")

        # También imprimir en consola
        print('\n'.join(reporte))
