import pandas as pd

class AgenteAnalisisDatos:
    """
    Agente de IA especializado en análisis de datos académicos.
    Procesa y limpia los datos para prepararlos para el análisis.
    """

    def __init__(self, archivo_excel):
        self.archivo = archivo_excel
        self.datos = None

    def cargar_datos(self):
        """Carga los datos del archivo Excel"""
        print("🤖 Agente de Análisis: Cargando datos...")
        self.datos = pd.read_excel(self.archivo)
        print(f"✓ Datos cargados: {self.datos.shape[0]} registros, {self.datos.shape[1]} columnas")
        return self.datos

    def preprocesar_datos(self):
        """Preprocesa y limpia los datos"""
        print("\n🤖 Agente de Análisis: Preprocesando datos...")

        # Limpiar valores nulos en columnas importantes
        self.datos['MATRICULA'].fillna(0, inplace=True)

        # Crear columnas derivadas útiles
        self.datos['PERIODO_COMPLETO'] = self.datos['AÑO_x'].astype(str) + '-' + self.datos['SEMESTRE_x'].astype(str)

        print("✓ Datos preprocesados")
        return self.datos

    def obtener_resumen_estadistico(self):
        """Genera un resumen estadístico de los datos"""
        print("\n📊 Resumen Estadístico:")
        print(f"   • Total de registros: {len(self.datos)}")
        print(f"   • Instituciones únicas: {self.datos['INSTITUCION'].nunique()}")
        print(f"   • Programas académicos únicos: {self.datos['PROGRAMA_ACADEMICO'].nunique()}")
        print(f"   • Períodos analizados: {self.datos['PERIODO'].nunique()}")
        return {
            'total_registros': len(self.datos),
            'instituciones': self.datos['INSTITUCION'].nunique(),
            'programas': self.datos['PROGRAMA_ACADEMICO'].nunique(),
            'periodos': self.datos['PERIODO'].nunique()
        }
