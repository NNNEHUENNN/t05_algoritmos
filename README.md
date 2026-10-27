# t05-algoritmos

Repositorio con los ejercicios del tema 5 ["Algoritmos Básicos y Verificación"](https://uib-23200-programacion.github.io/website/es/contenido/tema5.html).

> [!WARNING]
> **Es OBLIGATORIO que lea [ejercicios del tema 5](https://uib-23200-programacion.github.io/website/es/ejercicios/tema5.html) para los enunciados**.

Este repositorio contiene: 

- notebooks de Marimo bajo `notebooks/`,
- el paquete `t05_paquete` bajo la carpeta `/src` que contendrá (los debes escribir) los módulos `estadistica`, `cadenas` y `busqueda` además de un script `main.py` que demuestra el uso de las funciones en los módulos.

> [!IMPORTANT]
> **Lee las secciones a continuación para que puedas resolver correctamente los ejercicios en tu propio repositorio y Codespace**. 

---

## 1. Crear tu propia copia del repositorio

Este repositorio es una **plantilla** ("Template repository") de GitHub. Eso significa que puedes crear tu propio repositorio, con tu propio historial y bajo tu propia cuenta, a partir de este, sin necesidad de hacer un fork.

1. En la página de este repositorio en GitHub, pulsa el botón verde **"Use this template"** (arriba a la derecha, junto a "Code").
2. Elige **"Create a new repository"**.
3. Selecciona tu cuenta personal como propietario ("Owner"), ponle un nombre a tu repositorio (**mantén t05-algoritmos preferiblemente**) y márcalo como **privado**.
4. Pulsa **"Create repository"**.

A partir de ahora tienes tu propio repositorio, independiente del original. Todos los cambios que hagas se guardan ahí, no en la plantilla original.

> No necesitas clonar nada en tu ordenador. Todo el trabajo se hace en un Codespace, como se explica a continuación.

---

## 2. Levantar un Codespace

Un Codespace es un entorno de desarrollo completo de [Visual Studio Code](https://code.visualstudio.com/docs/editing/getting-started/userinterface) (editor + terminal + Python + todas las dependencias) que se ejecuta en un contenedor en la nube. No requiere instalar nada en tu ordenador.

1. Entra en **tu** repositorio (el que has creado en el paso anterior), no en la plantilla original.
2. Pulsa el botón verde **"Code"**.
3. Ve a la pestaña **"Codespaces"**.
4. Pulsa **"Create codespace on main"**.

GitHub construirá el contenedor definido en [.devcontainer/devcontainer.json](.devcontainer/devcontainer.json) e instalará automáticamente todas las dependencias del proyecto (esto ejecuta `uv sync` por ti, definido como `postCreateCommand`). La primera vez puede tardar uno o dos minutos; las siguientes veces que reabras el mismo Codespace será prácticamente instantáneo.

Cuando termine, se abrirá un editor de VS Code en el navegador ya conectado a tu repositorio, con el intérprete de Python correcto seleccionado y las extensiones necesarias instaladas.

---

## 3. Ejecutar el código

### Ejercicios en notebooks (`notebooks/`)

Los notebooks de Marimo (`ejer_t05_01-10_mo.py` y `ejer_t05_11-16_mo.py` — el sufijo `_mo.py` es la convención que usa VS Code para reconocerlos como notebook) se abren y ejecutan con la extensión de Marimo — no como un script de Python normal. Ábrelos desde el explorador de archivos; la extensión los reconoce automáticamente y te deja ejecutar las celdas de forma interactiva. En caso que esto no ocurra ábrelos haciendo clic en el ícono "Open in Marimo" arriba a la izquierda.

### Ejercicios en módulos (`src/t05_paquete`)

Los enunciados de los ejercicios se pueden consultar en [https://uib-23200-programacion.github.io/website/es/ejercicios/tema5.html](https://uib-23200-programacion.github.io/website/es/ejercicios/tema5.html). Para comprobar las soluciones necesita ejecutar `main.py` (que debes escribir también) como se indica a continuación.

### Ejecutar `main.py`

Abre [src/t03_paquete/main.py](src/t03_paquete/main.py) y pulsa el botón ▷ ("Run") en la esquina superior derecha del editor, o pulsa `F5` para ejecutarlo con el depurador. Se debe abrir el menú interactivo en la terminal.

---

## 4. Guardar y subir tus cambios (`push`)

Cuando hayas hecho cambios (por ejemplo, completado un ejercicio), tienes que guardarlos en tu repositorio de GitHub. Desde VS Code, sin usar la terminal:

1. Abre la pestaña **"Source Control"** de la barra lateral (icono de rama con un punto).
2. Verás la lista de archivos que has modificado. Revisa los cambios si quieres (VS Code te muestra el diff).
3. Escribe un mensaje breve describiendo qué has hecho, en el campo de texto de arriba (por ejemplo: `Implementado es_primo y mcd`).
4. Pulsa **"Commit"** (el símbolo ✓) para guardar el cambio localmente en el Codespace.
5. Pulsa **"Sync Changes"** (o "Push") para subir el commit a tu repositorio en GitHub.

Si prefieres usar la terminal, el equivalente es:

```bash
git add .
git commit -m "Implementado es_primo y mcd"
git push
```

---

## 5. Terminar la ejecución del Codespace

**Esto es muy importante**: un Codespace que se deja abierto sigue consumiendo horas de cómputo aunque no estés trabajando en él. GitHub ofrece una cuota mensual gratuita limitada, y agotarla significa que el entorno dejará de estar disponible hasta el mes siguiente. Detener el Codespace cuando terminas garantiza que esas horas se conservan para cuando realmente las necesitas.

**Desde el Codespace (VSCode en el navegador):**

Abre la paleta de comandos con `F1` (o `Ctrl+Shift+P`) y escribe **"Stop Current Codespace"** → Enter. El Codespace se detiene y la pestaña se debe cerrar sola.

**Desde la página del repositorio en GitHub:**

Ve a la pestaña **Code** → sección **Codespaces** → haz clic en los tres puntos **⋯** junto al Codespace activo → **Stop Codespace**.
