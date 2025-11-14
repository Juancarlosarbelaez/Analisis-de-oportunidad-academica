import asyncio

class AgenteTendenciasMercado:


    def __init__(self, datos):
        self.datos = datos
        self.tendencias = {}

    def analizar_tendencia_matricula_temporal(self):
        """Analiza la tendencia de matrícula a lo largo del tiempo"""
        print("Agente de Tendencias: Analizando evolución temporal de matrículas...")

        # Agrupar por período y calcular matrícula total
        tendencia_temporal = self.datos.groupby('PERIODO')['MATRICULA'].sum().sort_index()

        self.tendencias['temporal'] = tendencia_temporal
        print(f"Identificados {len(tendencia_temporal)} períodos con datos de matrícula")
        return tendencia_temporal

    def analizar_tendencia_por_institucion(self):
        """Analiza tendencias por institución"""
        print("Agente de Tendencias: Analizando tendencias por institución...")

        # Top instituciones por matrícula total
        tendencia_institucional = self.datos.groupby('INSTITUCION')['MATRICULA'].sum().sort_values(ascending=False)

        self.tendencias['institucional'] = tendencia_institucional
        print(f"Analizadas {len(tendencia_institucional)} instituciones")
        return tendencia_institucional

    def analizar_tendencia_por_programa(self):
        """Analiza tendencias por programa académico"""
        print(" Agente de Tendencias: Analizando tendencias por programa académico...")

        tendencia_programas = self.datos.groupby('PROGRAMA_ACADEMICO')['MATRICULA'].sum().sort_values(ascending=False)

        self.tendencias['programas'] = tendencia_programas
        print(f"Analizados {len(tendencia_programas)} programas académicos")
        return tendencia_programas

    def analizar_distribucion_sectores(self):
        """Analiza la distribución entre sectores público y privado"""
        print(" Agente de Tendencias: Analizando distribución por sector...")

        tendencia_sectores = self.datos.groupby('SECTOR_IES')['MATRICULA'].sum()

        self.tendencias['sectores'] = tendencia_sectores
        print(f"Analizados sectores: {', '.join(tendencia_sectores.index.tolist())}")
        return tendencia_sectores

    def analizar_areas_conocimiento(self):
        """Analiza tendencias por áreas de conocimiento"""
        print("Agente de Tendencias: Analizando áreas de conocimiento...")

        tendencia_areas = self.datos.groupby('AREA_CONOCIMIENTO')['MATRICULA'].sum().sort_values(ascending=False)

        self.tendencias['areas'] = tendencia_areas
        print(f"Analizadas {len(tendencia_areas)} áreas de conocimiento")
        return tendencia_areas

    async def analizar_todo_concurrente(self) -> None:
        tareas = [
            asyncio.to_thread(self.analizar_tendencia_matricula_temporal),
            asyncio.to_thread(self.analizar_tendencia_por_institucion),
            asyncio.to_thread(self.analizar_tendencia_por_programa),
            asyncio.to_thread(self.analizar_distribucion_sectores),
            asyncio.to_thread(self.analizar_areas_conocimiento),
        ]
        await asyncio.gather(*tareas)
