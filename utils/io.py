import pandas as pd
import matplotlib.pyplot as plt
from typing import Iterable, List


def load_excel(path: str, **kwargs) -> pd.DataFrame:
    """Carga un Excel usando pandas (envuelve pd.read_excel)."""
    return pd.read_excel(path, **kwargs)


def save_figure(filename: str, dpi: int = 300, bbox_inches: str = 'tight') -> None:
    """Guarda la figura activa de matplotlib en `filename` con configuración estándar."""
    plt.savefig(filename, dpi=dpi, bbox_inches=bbox_inches)


def write_report(path: str, lines: Iterable[str]) -> None:
    """Guarda una lista/iterable de líneas en un archivo de texto (UTF-8)."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
