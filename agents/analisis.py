import pandas as pd

class AgenteAnalisisDatos:
    

    def __init__(self, archivo_excel):
        self.archivo = archivo_excel
        self.datos = None

    def cargar_datos(self):
        """Carga los datos del archivo Excel"""
        print("Agente de Análisis: Cargando datos...")
        self.datos = pd.read_excel(self.archivo)
        print(f"✓ Datos cargados: {self.datos.shape[0]} registros, {self.datos.shape[1]} columnas")
        return self.datos

    def preprocesar_datos(self):
        """Preprocesa y limpia los datos"""
        print("Agente de Análisis: Preprocesando datos...")
        # Validar columnas requeridas mínimas
        columnas_requeridas = ['MATRICULA']
        for col in columnas_requeridas:
            if col not in self.datos.columns:
                raise ValueError(f"Columna requerida faltante en el dataset: {col}")

        
        anio_cols = [c for c in self.datos.columns if c.upper().startswith('AÑO')]
        semestre_cols = [c for c in self.datos.columns if c.upper().startswith('SEMESTRE')]
        if anio_cols and semestre_cols:
            col_anio = anio_cols[0]
            col_semestre = semestre_cols[0]
            self.datos['PERIODO'] = self.datos[col_anio].astype(str) + '-' + self.datos[col_semestre].astype(str)
        elif 'PERIODO' not in self.datos.columns:
           
        # Limpiar valores nulos en matrícula
         self.datos['MATRICULA'].fillna(0, inplace=True)

         print("✓ Datos preprocesados")
        return self.datos

    def obtener_resumen_estadistico(self):
        """Genera un resumen estadístico de los datos"""
        print("Resumen Estadístico:")
        print(f"   • Total de registros: {len(self.datos)}")
        print(f"   • Instituciones únicas: {self.datos['INSTITUCION'].nunique()}")
        print(f"   • Programas académicos únicos: {self.datos['PROGRAMA_ACADEMICO'].nunique()}")
        periodos = self.datos['PERIODO'].nunique() if 'PERIODO' in self.datos.columns else 0
        print(f"   • Períodos analizados: {periodos}")
        return {
            'total_registros': len(self.datos),
            'instituciones': self.datos['INSTITUCION'].nunique() if 'INSTITUCION' in self.datos.columns else 0,
            'programas': self.datos['PROGRAMA_ACADEMICO'].nunique() if 'PROGRAMA_ACADEMICO' in self.datos.columns else 0,
            'periodos': periodos
        }
