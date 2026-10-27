# Guía del repositorio plantilla

Este documento describe la arquitectura del repositorio plantilla utilizado para crear todos repositorios de ejercicios por tema de la asignatura.

---

# Objetivos

El template persigue los siguientes objetivos:

- minimizar la configuración requerida para generar nuevos repositorios;
- proporcionar un entorno reproducible;
- utilizar herramientas modernas del ecosistema Python.

---

# Principios de diseño

## Un único gestor de proyectos

Todo el proyecto gira alrededor de **uv**.

No se utilizan:

* requirements.txt
* pip install
* python -m venv

Toda la configuración reside en:

```text
pyproject.toml
```

---

## Un único formateador

Se utiliza exclusivamente **Ruff**.

No se emplea:

* Black
* isort

Ruff se encarga de:

* formateo;
* organización de imports;
* análisis estático.

---

## Un único sistema de pruebas

Se utiliza:

* pytest

Toda su configuración reside en:

```text
pyproject.toml
```

---

# Organización del repositorio

```text
src/
```

Código fuente: **solo** el paquete instalable (con `__init__.py`), pensado
para ser importado (por `main.py`, por otros módulos, por los tests).

Si un ejercicio es un script independiente que nadie importa, no va aquí:
ver `ejercicios_simples/` más abajo. Meter scripts sueltos con `input()` en
`src/` es problemático porque, si alguna vez se importan desde `__init__.py`
(como sugiere su propio comentario de ejemplo), el `input()` se dispara al
importar y rompe cualquier cosa que importe el paquete — incluido el propio
chequeo de `conftest.py`.

---

```text
tests/
```

Pruebas automáticas.

---

```text
notebooks/
```

Notebooks Marimo.

No deben mezclarse con el código fuente.

Los ficheros se nombran con el sufijo `_mo.py` (p. ej. `ejemplo_mo.py`).
Es una convención no oficial pero real de la extensión de Marimo para
VS Code y de `marimo-jupyter-extension`, confirmada por un mantenedor de
marimo en [marimo-team/marimo#8688](https://github.com/marimo-team/marimo/discussions/8688)
y propuesta formalmente (aún sin cerrar) en
[marimo-team/meps#10](https://github.com/marimo-team/meps/pull/10).
No aparece en el manifiesto declarativo de la extensión (`package.json`,
que sigue usando un selector genérico `*.py`), así que no está garantizada
a largo plazo, pero hoy facilita que VS Code identifique el fichero como
notebook sin depender solo de inspeccionar su contenido.

Excluidos de Ruff (`[tool.ruff] extend-exclude`) porque contienen prosa pedagógica
(enunciados largos en `mo.md()`) y variables intencionalmente "sin usar"
(valores a inspeccionar en la celda, no código de producción) — reglas
como E501 y F841 no aplican ahí igual que en `src/`.

---

```text
ejercicios_simples/
```

Ejercicios expresados como scripts independientes (no como notebook),
típicamente con `input()`. Ninguno se importa ni es importado — por eso no
llevan `__init__.py` ni viven bajo `src/`.

Excluidos de Ruff por el mismo motivo que `notebooks/`: enunciados largos
como comentarios y código de un solo uso, no código de producción.

Un tema puede tener `ejercicios_simples/`, `src/<paquete>/` (si además hay
código realmente importable, como en el ejemplo de `t03_ejemplo`), ambos, o
ninguno — depende de la naturaleza de sus ejercicios.

---

```text
docs/
```

Documentación adicional.

---

```text
.devcontainer/
```

Configuración del entorno de desarrollo.

Su única responsabilidad es describir el contenedor.

Incluye:

- imagen base;
- Features;
- variables de entorno;
- comandos de inicialización;
- puertos.

No contiene configuración del editor, excepto la selección del intérprete
de Python (ver `## devcontainer.json` más abajo).

---

```text
.vscode/
```

Configuración compartida de Visual Studio Code.

Contiene:

* settings.json
* launch.json

---

# Responsabilidades de cada archivo

## devcontainer.json

Debe contener únicamente:

- imagen Docker;
- Features;
- lista de extensiones para VS Code;
- postCreateCommand;
- updateContentCommand;
- variables de entorno;
- puertos;
- usuario remoto;
- selección del intérprete de Python (`customizations.vscode.settings`).

Esta última es la única excepción a "no contiene configuración del editor":
la ruta del intérprete (`.venv/bin/python` dentro del contenedor) solo tiene
sentido dentro del propio devcontainer, así que vive aquí y no en
`.vscode/settings.json` (que es independiente del entorno de ejecución).
Actualmente:

- `python.defaultInterpreterPath`, usado por la extensión de Python;
- `marimo.pythonPath`, usado por la extensión de Marimo.

---

## settings.json

Debe contener únicamente preferencias del editor independientes del
entorno de ejecución (no la selección del intérprete: ver
`## devcontainer.json`).

Ejemplos:

- formatter;
- formatOnSave;
- Copilot;
- inlay hints.

---

## pyproject.toml

Es el centro de la configuración del proyecto.

Contiene:

- dependencias;
- grupos de dependencias;
- Ruff;
- pytest;
- cobertura;
- empaquetado;
- configuración del proyecto.

---

## Empaquetado

El paquete bajo `src/` se instala en modo editable automáticamente al
ejecutar `uv sync` (gracias a `[build-system]` + `[tool.setuptools.packages.find]`
en `pyproject.toml`).

La detección del paquete es dinámica: no depende de que su nombre coincida
con `[project.name]`, así que renombrar `prg23200` a `prg23200_tX` en un
nuevo tema no requiere tocar `pyproject.toml`.

Sin esto, `import prg23200` falla con `ModuleNotFoundError` al ejecutar
`main.py` directamente (con el botón ▷ de VS Code, por ejemplo), aunque
los tests funcionen correctamente gracias a `pythonpath = ["src"]` en
`[tool.pytest.ini_options]`.

---

# Grupos de dependencias

El template utiliza grupos de uv para instalar únicamente las herramientas necesarias.

## dev

Herramientas comunes de desarrollo.

- pytest
- pytest-cov
- ruff

---

## scientific

Bibliotecas del ecosistema científico de Python.

- NumPy
- Pandas
- Matplotlib
- SymPy
- SciPy

---

# Integración continua (CI)

```text
.github/workflows/ci.yml
```

Se ejecuta en cada `push` y en cada Pull Request. Instala el proyecto con
`uv sync --group dev` y corre `ruff check .` y `pytest`.

No requiere ninguna acción por parte del estudiante: se dispara solo. Es
la forma en la que los repositorios generados a partir del template dan
feedback automático (✅/❌ en la pestaña "Actions" de GitHub) sin depender
de una revisión manual.

Al crear un nuevo repositorio a partir del template, este workflow se
hereda tal cual — no requiere ningún ajuste salvo que cambien las
herramientas de `dev` en `pyproject.toml` (ver más abajo).

---

# Actualización del template

Cuando sea necesario incorporar una nueva herramienta:

1. añadir la dependencia al grupo correspondiente en `pyproject.toml`;
2. ejecutar:

```bash
uv lock
```

3. comprobar el funcionamiento en Codespaces;
4. verificar que `.github/workflows/ci.yml` sigue pasando (pestaña "Actions");
5. crear una nueva versión del template.

---

# Creación de nuevos repositorios

Para un nuevo tema:

1. crear el repositorio a partir del Template Repository;
2. modificar nombre del directorio bajo source de `prg23200` a `prg23200_tX`;
3. decidir, por cada ejercicio, si va en `src/prg23200_tX/` (código
   realmente importable) o en `ejercicios_simples/` / `notebooks/` (scripts
   o notebooks independientes) — ver `## Organización del repositorio`;
4. si es necesario, ajustar el grupo de dependencias sincronizado por el `postCreateCommand`;
5. no modificar la infraestructura salvo que exista una razón justificada.
