import matplotlib.pyplot as plt
import seaborn as sns
import asyncio
from utils.io import save_figure

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

class AgenteVisualizacion:


    def __init__(self, datos, tendencias):
        self.datos = datos
        self.tendencias = tendencias
        self.figuras = []

    def crear_grafica_tendencia_temporal(self):
        """Crea gráfica de tendencia temporal de matrícula"""
        print("Agente de Visualización: Creando gráfica de tendencia temporal...")

        fig, ax = plt.subplots(figsize=(12, 6))

        tendencia = self.tendencias.get('temporal')
        if tendencia is not None and len(tendencia) > 0:
            ax.plot(tendencia.index, tendencia.values, marker='o', linewidth=2, markersize=8)
            ax.set_xlabel('Período', fontsize=12, fontweight='bold')
            ax.set_ylabel('Matrícula Total', fontsize=12, fontweight='bold')
            ax.set_title('Tendencia de Matrícula a lo Largo del Tiempo', fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()

            # Guardar figura usando el objeto `fig` para evitar condiciones de carrera
            fig.savefig('tendencia_temporal_matricula.png', dpi=300, bbox_inches='tight')
            self.figuras.append('tendencia_temporal_matricula.png')
            print("✓ Gráfica guardada: tendencia_temporal_matricula.png")

        plt.close()

    def crear_grafica_top_instituciones(self, top_n=10):
        """Crea gráfica de top instituciones por matrícula"""
        print("Agente de Visualización: Creando gráfica de top instituciones...")

        fig, ax = plt.subplots(figsize=(12, 8))

        tendencia = self.tendencias.get('institucional')
        if tendencia is not None and len(tendencia) > 0:
            top_instituciones = tendencia.head(top_n)

            colors = sns.color_palette("viridis", len(top_instituciones))
            ax.barh(range(len(top_instituciones)), top_instituciones.values, color=colors)
            ax.set_yticks(range(len(top_instituciones)))
            ax.set_yticklabels([inst[:50] + '...' if len(inst) > 50 else inst 
                                for inst in top_instituciones.index], fontsize=10)
            ax.set_xlabel('Matrícula Total', fontsize=12, fontweight='bold')
            ax.set_title(f'Top {top_n} Instituciones por Matrícula Total', fontsize=14, fontweight='bold')
            ax.invert_yaxis()
            plt.tight_layout()

            # Guardar figura usando el objeto `fig` para evitar condiciones de carrera
            fig.savefig('top_instituciones_matricula.png', dpi=300, bbox_inches='tight')
            self.figuras.append('top_instituciones_matricula.png')
            print("✓ Gráfica guardada: top_instituciones_matricula.png")

        plt.close()

    def crear_grafica_programas(self):
        """Crea gráfica de programas académicos"""
        print("Agente de Visualización: Creando gráfica de programas académicos...")

        fig, ax = plt.subplots(figsize=(10, 6))

        tendencia = self.tendencias.get('programas')
        if tendencia is not None and len(tendencia) > 0:
            colors = sns.color_palette("Set2", len(tendencia))
            ax.bar(range(len(tendencia)), tendencia.values, color=colors)
            ax.set_xticks(range(len(tendencia)))
            ax.set_xticklabels([prog[:30] + '...' if len(prog) > 30 else prog 
                                for prog in tendencia.index], rotation=45, ha='right', fontsize=9)
            ax.set_ylabel('Matrícula Total', fontsize=12, fontweight='bold')
            ax.set_title('Distribución de Matrícula por Programa Académico', fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3, axis='y')
            plt.tight_layout()

            # Guardar figura usando el objeto `fig` para evitar condiciones de carrera
            fig.savefig('distribucion_programas.png', dpi=300, bbox_inches='tight')
            self.figuras.append('distribucion_programas.png')
            print("✓ Gráfica guardada: distribucion_programas.png")

        plt.close()

    def crear_grafica_sectores(self):
        """Crea gráfica de distribución por sectores"""
        print("Agente de Visualización: Creando gráfica de sectores...")

        fig, ax = plt.subplots(figsize=(10, 8))

        tendencia = self.tendencias.get('sectores')
        if tendencia is not None and len(tendencia) > 0:
            colors = ['#ff9999', '#66b3ff']
            explode = [0.05] * len(tendencia)

            ax.pie(tendencia.values, labels=tendencia.index, autopct='%1.1f%%',
                   startangle=90, colors=colors, explode=explode,
                   textprops={'fontsize': 12, 'fontweight': 'bold'})
            ax.set_title('Distribución de Matrícula por Sector (Público vs Privado)', 
                        fontsize=14, fontweight='bold', pad=20)
            plt.tight_layout()

            # Guardar figura usando el objeto `fig` para evitar condiciones de carrera
            fig.savefig('distribucion_sectores.png', dpi=300, bbox_inches='tight')
            self.figuras.append('distribucion_sectores.png')
            print("✓ Gráfica guardada: distribucion_sectores.png")

        plt.close()

    def crear_grafica_areas_conocimiento(self):
        """Crea gráfica de áreas de conocimiento"""
        print("Agente de Visualización: Creando gráfica de áreas de conocimiento...")

        fig, ax = plt.subplots(figsize=(10, 6))

        tendencia = self.tendencias.get('areas')
        if tendencia is not None and len(tendencia) > 0:
            colors = sns.color_palette("coolwarm", len(tendencia))
            bars = ax.bar(range(len(tendencia)), tendencia.values, color=colors)
            ax.set_xticks(range(len(tendencia)))
            ax.set_xticklabels([area[:40] + '...' if len(area) > 40 else area 
                                for area in tendencia.index], rotation=45, ha='right', fontsize=10)
            ax.set_ylabel('Matrícula Total', fontsize=12, fontweight='bold')
            ax.set_title('Distribución de Matrícula por Área de Conocimiento', 
                        fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3, axis='y')

            # Añadir valores en las barras
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{int(height):,}',
                       ha='center', va='bottom', fontsize=9)

            plt.tight_layout()

            # Guardar figura usando el objeto `fig` para evitar condiciones de carrera
            fig.savefig('distribucion_areas_conocimiento.png', dpi=300, bbox_inches='tight')
            self.figuras.append('distribucion_areas_conocimiento.png')
            print("✓ Gráfica guardada: distribucion_areas_conocimiento.png")

        plt.close()

    def crear_dashboard_completo(self):
        """Crea un dashboard con múltiples gráficas y lo guarda."""
        print("Agente de Visualización: Creando dashboard completo...")

        fig = plt.figure(figsize=(16, 12))
        gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

        # Gráfica 1: Tendencia temporal
        ax1 = fig.add_subplot(gs[0, :])
        tendencia = self.tendencias.get('temporal')
        if tendencia is not None and len(tendencia) > 0:
            ax1.plot(tendencia.index, tendencia.values, marker='o', linewidth=2, markersize=6, color='#2E86AB')
            ax1.set_xlabel('Período', fontsize=10, fontweight='bold')
            ax1.set_ylabel('Matrícula Total', fontsize=10, fontweight='bold')
            ax1.set_title('Evolución Temporal de Matrícula', fontsize=12, fontweight='bold')
            ax1.grid(True, alpha=0.3)
            plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')

        # Gráfica 2: Top 5 instituciones
        ax2 = fig.add_subplot(gs[1, 0])
        tendencia_inst = self.tendencias.get('institucional')
        if tendencia_inst is not None and len(tendencia_inst) > 0:
            top5_inst = tendencia_inst.head(5)
            colors = sns.color_palette("viridis", 5)
            ax2.barh(range(len(top5_inst)), top5_inst.values, color=colors)
            ax2.set_yticks(range(len(top5_inst)))
            ax2.set_yticklabels([inst[:30] for inst in top5_inst.index], fontsize=8)
            ax2.set_xlabel('Matrícula', fontsize=10, fontweight='bold')
            ax2.set_title('Top 5 Instituciones', fontsize=12, fontweight='bold')
            ax2.invert_yaxis()

        # Gráfica 3: Sectores
        ax3 = fig.add_subplot(gs[1, 1])
        tendencia_sect = self.tendencias.get('sectores')
        if tendencia_sect is not None and len(tendencia_sect) > 0:
            colors = ['#ff9999', '#66b3ff']
            ax3.pie(tendencia_sect.values, labels=tendencia_sect.index, autopct='%1.1f%%',
                   startangle=90, colors=colors, textprops={'fontsize': 9})
            ax3.set_title('Distribución por Sector', fontsize=12, fontweight='bold')

        # Gráfica 4: Programas
        ax4 = fig.add_subplot(gs[2, 0])
        tendencia_prog = self.tendencias.get('programas')
        if tendencia_prog is not None and len(tendencia_prog) > 0:
            colors = sns.color_palette("Set2", len(tendencia_prog))
            ax4.bar(range(len(tendencia_prog)), tendencia_prog.values, color=colors)
            ax4.set_xticks(range(len(tendencia_prog)))
            ax4.set_xticklabels([prog[:15] for prog in tendencia_prog.index], rotation=45, ha='right', fontsize=7)
            ax4.set_ylabel('Matrícula', fontsize=10, fontweight='bold')
            ax4.set_title('Programas Académicos', fontsize=12, fontweight='bold')
            ax4.grid(True, alpha=0.3, axis='y')

        # Gráfica 5: Áreas de conocimiento
        ax5 = fig.add_subplot(gs[2, 1])
        tendencia_areas = self.tendencias.get('areas')
        if tendencia_areas is not None and len(tendencia_areas) > 0:
            colors = sns.color_palette("coolwarm", len(tendencia_areas))
            ax5.bar(range(len(tendencia_areas)), tendencia_areas.values, color=colors)
            ax5.set_xticks(range(len(tendencia_areas)))
            ax5.set_xticklabels([area[:20] for area in tendencia_areas.index], rotation=45, ha='right', fontsize=7)
            ax5.set_ylabel('Matrícula', fontsize=10, fontweight='bold')
            ax5.set_title('Áreas de Conocimiento', fontsize=12, fontweight='bold')
            ax5.grid(True, alpha=0.3, axis='y')

        plt.suptitle('Dashboard de Análisis de Tendencias de Mercado Académico', fontsize=16, fontweight='bold', y=0.995)

        # Guardar dashboard usando el objeto `fig`
        fig.savefig('dashboard_completo.png', dpi=300, bbox_inches='tight')
        self.figuras.append('dashboard_completo.png')
        print("Dashboard guardado: dashboard_completo.png")
        plt.close()

    async def crear_todas_graficas(self, top_n: int = 10) -> None:
        tareas = [
            asyncio.to_thread(self.crear_grafica_tendencia_temporal),
            asyncio.to_thread(self.crear_grafica_top_instituciones, top_n),
            asyncio.to_thread(self.crear_grafica_programas),
            asyncio.to_thread(self.crear_grafica_sectores),
            asyncio.to_thread(self.crear_grafica_areas_conocimiento),
        ]
        await asyncio.gather(*tareas)
        await asyncio.to_thread(self.crear_dashboard_completo)
