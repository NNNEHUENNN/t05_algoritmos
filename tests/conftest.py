"""
Configuración compartida para pytest.

Este archivo se carga automáticamente antes de cualquier test.
Aquí puedes definir fixtures reutilizables, opciones personalizadas
y hooks de sesión.

La detección del paquete principal (el que está dentro de src/)
es dinámica: no necesitas cambiar ningún nombre al crear un tema nuevo.
"""

from pathlib import Path

# import pytest


# ─── Detección dinámica del paquete ────────────────────────────────
def _find_package():
    """
    Busca dentro de src/ el primer directorio que contenga __init__.py
    y devuelve su nombre. Si no encuentra ninguno, devuelve None.
    """
    src_dir = Path(__file__).resolve().parents[1] / "src"
    if not src_dir.is_dir():
        return None
    for item in src_dir.iterdir():
        if item.is_dir() and (item / "__init__.py").exists():
            return item.name
    return None


PACKAGE_NAME = _find_package()


# ─── Verificación inicial del paquete ─────────────────────────────
def pytest_sessionstart(session):
    """Se ejecuta al comienzo de la sesión de tests."""
    if PACKAGE_NAME is None:
        print(
            "⚠️  No se encontró ningún paquete en src/."
            " Asegúrate de que existe una carpeta con __init__.py dentro de src/"
        )
    else:
        try:
            __import__(PACKAGE_NAME)
            print(f"✅ Paquete '{PACKAGE_NAME}' importado correctamente.")
        except ImportError:
            print(
                f"⚠️  No se pudo importar '{PACKAGE_NAME}'."
                " Ejecuta 'uv sync' para instalar el proyecto en modo editable."
            )


# ─── Ejemplo de fixture reutilizable ──────────────────────────────
# Descomenta y adapta este fixture según las necesidades del tema.
# Debes descomentar import pytests al inicio
#
# @pytest.fixture
# def datos_ejemplo():
#     """Proporciona un conjunto de datos de prueba común."""
#     return [1, 2, 3, 5, 8, 13]


# ─── Ajuste de PYTHONPATH (solo si NO usas instalación editable) ──
# Si prefieres no depender de 'uv sync' o 'pip install -e .',
# descomenta las líneas siguientes para que Python encuentre el paquete.
#
# sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


# ─── Opciones de línea de comandos ─────────────────────────────────
def pytest_addoption(parser):
    parser.addoption(
        "--modo-verbose",
        action="store_true",
        default=False,
        help="Ejecuta los tests en modo detallado",
    )


def pytest_configure(config):
    if config.getoption("--modo-verbose"):
        print("🔍 Modo verbose activado")


# ─── Limpieza (opcional) ──────────────────────────────────────────
# def pytest_sessionfinish(session, exitstatus):
#     """Se ejecuta al finalizar la sesión de tests."""
#     pass
