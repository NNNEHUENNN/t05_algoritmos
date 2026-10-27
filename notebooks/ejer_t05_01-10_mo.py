import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell
def _():
    # Importamos la librería marimo como 'mo'.
    # Esto es obligatorio para que funcionen los elementos interactivos
    # (sliders, botones), el texto con formato (markdown) y las
    # referencias entre celdas.
    # NO CAMBIAR NI ELIMINAR
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Ejercicios 5.1 - 5.10 del Tema 5: Patrones algorítmicos

    ## Ejercicio 5.1: Máximo de un flujo con varios acumuladores

    Escribe una función `resumen_flujo(flujo)` que recorra el flujo **una sola vez** y retorne una tupla `(maximo, minimo, suma, contador)` calculando las cuatro estadísticas simultáneamente.

    Pruébala con el generador `sensor_temperatura()` definido abajo, que simula un sensor con valores máximo y mínimo de temperatura predefinidos. Después calcula la media a partir del resultado: `suma / contador`. Debes tener en cuenta que el generador es infinito por lo cual la función `resumen_flujo` tiene el parámetro con valor `capacidad=100` que limita la cantidad de datos a leer del stream.

    Esta es la esencia del patrón de *una sola pasada*: en lugar de hacer cuatro recorridos separados, se mantienen cuatro acumuladores en paralelo.
    """)
    return


@app.cell
def _():
    # Ejercicio 5.1: Máximo de un flujo con varios acumuladores
    import random
    from typing import Iterator

    def sensor_temperatura() -> Iterator[float]:
        """
        Generador infinito que simula un flujo de temperaturas.

        Las temperaturas están en el intervalo (-10.0, 50.0).
        """
        mi_generador = random.Random(42)
        while True:
            # uniform() genera números de coma flotante
            yield mi_generador.uniform(-10.0, 50.0)


    def resumen_flujo(flujo: Iterator[float], capacidad: int = 100) -> tuple[float, float, float, int]:
        """
        Recorre el flujo una sola vez y retorna (maximo, minimo, suma, contador).
        """
        temperatura = sensor_temperatura()
        pass


    maximo, minimo, suma, contador = resumen_flujo(sensor_temperatura())
    print(f"Máximo:    {maximo}")
    print(f"Mínimo:    {minimo}")
    print(f"Media:     {suma / contador:.4f}")
    print(f"Elementos: {contador}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5.2: Una sola pasada — media, mínimo y máximo

    Escribe una función `estadisticas(datos)` que reciba una `list[float]` **no vacía** y retorne una tupla `(media, minimo, maximo)`, calculando los tres valores en **una sola pasada** (un único bucle `for`).

    No se permite usar las funciones built-in `sum()`, `min()`, `max()`, `len()` sobre la lista completa. Cada valor debe calcularse con un acumulador propio.

    Comprueba el resultado con:

    - `estadisticas([4.0, 7.0, 2.0, 9.0, 1.0])` → `(4.6, 1.0, 9.0)`
    - `estadisticas([5.0])` → `(5.0, 5.0, 5.0)`
    - `estadisticas([-3.0, 0.0, 3.0])` → `(0.0, -3.0, 3.0)`
    """)
    return


@app.function
# Ejercicio 5.2: Una sola pasada — media, mínimo y máximo

def estadisticas(datos: list[float]) -> tuple[float, float, float]:
    """
    Retorna (media, minimo, maximo) en una sola pasada.
    Precondición: datos no está vacío.
    """
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5.3: Parada anticipada — primer descenso en una secuencia

    Escribe una función `primer_descenso(v)` que retorne el **índice $i$** (con $1 \le i \le n-1$) de la primera posición tal que `v[i] < v[i-1]`, es decir, el primer lugar donde la secuencia deja de ser creciente.

    Si la secuencia es completamente no decreciente (nunca baja), la función retorna $-1$.

    La función debe usar **parada anticipada**: en cuanto detecta el primer descenso, retorna inmediatamente sin examinar el resto de la lista.

    Ejemplos:

    - `primer_descenso([1, 3, 5, 4, 6])` → `3` (en `v[3]=4 < v[2]=5`)
    - `primer_descenso([1, 2, 3, 4, 5])` → `-1` (siempre creciente)
    - `primer_descenso([5, 3, 1])` → `1` (el primer par ya desciende)
    - `primer_descenso([2])` → `-1` (un solo elemento)
    """)
    return


@app.function
# Ejercicio 5.3: Parada anticipada — primer descenso

def primer_descenso(v: list[float]) -> int:
    """
    Retorna el índice del primer descenso en v, o -1 si no hay ninguno.
    """
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5.4: Recorrido — filtrar y transformar

    Escribe una función `cuadrados_positivos(v)` que reciba una lista de números reales y retorne una **nueva lista** con los cuadrados de los elementos estrictamente positivos, en el mismo orden. Los elementos negativos o cero se omiten.

    Implementa la función de dos maneras distintas y verifica que dan el mismo resultado:

    1. **Con bucle `for`** y un acumulador `resultado = []` con `.append()`.
    2. **Con comprensión de lista**: `[x**2 for x in v if x > 0]`.

    Comprueba con:

    - `cuadrados_positivos([3.0, -1.0, 0.0, 2.0, -4.0, 5.0])` → `[9.0, 4.0, 25.0]`
    - `cuadrados_positivos([-1.0, -2.0])` → `[]`
    - `cuadrados_positivos([])` → `[]`
    """)
    return


@app.cell
def _():
    # Ejercicio 5.4: Recorrido — filtrar y transformar

    def cuadrados_positivos(v: list[float]) -> list[float]:
        """Con bucle for."""
        pass

    def cuadrados_positivos_comp(v: list[float]) -> list[float]:
        """Con comprensión de lista."""
        pass
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5.5: Búsqueda — primera posición de un carácter

    Escribe una función `buscar_caracter(s, c)` que retorne el **índice** de la primera aparición del carácter `c` en la cadena `s`, o $-1$ si no se encuentra. **No está permitido usar** los métodos `str.find`, `str.index` ni el operador `in`.

    La función debe usar parada anticipada: retorna en cuanto encuentra `c`, sin examinar el resto de `s`.

    Comprueba con:

    - `buscar_caracter("matematica", 'a')` → `1`
    - `buscar_caracter("matematica", 'z')` → `-1`
    - `buscar_caracter("\", 'a')` → `-1`
    - `buscar_caracter("x", 'x')` → `0`

    ¿Cómo se relaciona esta función con la búsqueda lineal sobre una lista? ¿Cuál es su complejidad en el peor caso?
    """)
    return


@app.function
# Ejercicio 5.5: Búsqueda — primera posición de un carácter

def buscar_caracter(s: str, c: str) -> int:
    """Retorna el índice de la primera aparición de c en s, o -1."""
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5.6: Acumulación — producto de los elementos positivos

    Escribe una función `producto_positivos(v)` que reciba una lista de números reales y retorne el **producto** de todos los elementos estrictamente positivos. Si no hay ningún elemento positivo, retorna `1.0` (el elemento neutro del producto).

    Identifica el **valor inicial** del acumulador: ¿por qué es `1.0` y no `0.0`?

    Comprueba con:

    - `producto_positivos([2.0, -3.0, 4.0, 0.0, 5.0])` → `40.0` (2 × 4 × 5)
    - `producto_positivos([-1.0, -2.0, 0.0])` → `1.0` (ningún positivo)
    - `producto_positivos([3.0])` → `3.0`
    - `producto_positivos([])` → `1.0`

    Escribe también la versión con comprensión generadora:
    ```python
    import math
    resultado = math.prod(x for x in v if x > 0)
    ```
    y verifica que coincide.
    """)
    return


@app.cell
def _():
    # Ejercicio 5.6: Acumulación — producto de los elementos positivos
    import math

    def producto_positivos(v: list[float]) -> float:
        """Producto de los elementos estrictamente positivos de v."""
        pass
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5.7: Conteo — frecuencia de vocales

    Escribe una función `frecuencia_vocales(texto)` que reciba una cadena de texto y retorne un **diccionario** `dict[str, int]` con la frecuencia de aparición de cada vocal (`a, e, i, o, u`) en `texto`, sin distinguir mayúsculas de minúsculas ni vocales acentuadas (solo las cinco vocales básicas). Las vocales con frecuencia cero no deben aparecer en el diccionario.

    Usa el patrón de conteo: `conteo[v] = conteo.get(v, 0) + 1`.

    Comprueba con:

    - `frecuencia_vocales("Matematica")` → `{'a': 4, 'e': 1, 'i': 1}`
    - `frecuencia_vocales("Python")` → `{'o': 1}`
    - `frecuencia_vocales("xyz")` → `{}`
    - `frecuencia_vocales("\")` → `{}`

    ¿Cuál es la vocal más frecuente en castellano? Comprueba tu hipótesis con un párrafo de texto largo de tu elección.
    """)
    return


@app.function
# Ejercicio 5.7: Conteo — frecuencia de vocales

def frecuencia_vocales(texto: str) -> dict[str, int]:
    """Frecuencia de las cinco vocales básicas en texto."""
    vocales = set("aeiou")
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5.8: Composición — varianza en dos pasadas

    La **varianza poblacional** de una lista de datos es:
    $$
    \sigma^2 = \frac{1}{n}\sum_{i=0}^{n-1}(x_i - \bar{x})^2
    $$

    Implementa `varianza(datos)` usando **dos acumulaciones separadas**:

    1. Primera pasada: acumula la suma de todos los elementos para calcular la media $\bar{x}$.
    2. Segunda pasada: acumula la suma de los cuadrados de las desviaciones $(x_i - \bar{x})^2$.

    Este es un ejemplo de **composición de patrones**: la segunda acumulación depende del resultado de la primera.

    Precondición: `datos` no está vacío. No se permite usar `statistics`, `numpy` ni `math`.

    Verifica con:

    - `varianza([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0])` → `4.0` (ejemplo del tema)
    - `varianza([1.0, 1.0, 1.0])` → `0.0`
    - `varianza([0.0, 10.0])` → `25.0`
    """)
    return


@app.function
# Ejercicio 5.8: Composición — varianza en dos pasadas

def varianza(datos: list[float]) -> float:
    """
    Varianza poblacional de datos usando dos pasadas.
    Precondición: datos no está vacío.
    """
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5.9: Batch — mediana de una lista

    La **mediana** de una lista ordenada de $n$ valores es:

    $$
    \text{mediana}(v) =
    \begin{cases}
    v_{\text{ord}}[n \mathbin{/\!/} 2] & \text{si } n \text{ es impar} \\[4pt]
    \dfrac{v_{\text{ord}}[n \mathbin{/\!/} 2 - 1] + v_{\text{ord}}[n \mathbin{/\!/} 2]}{2} & \text{si } n \text{ es par}
    \end{cases}
    $$

    Implementa `mediana(datos)` usando el algoritmo batch: ordena una **copia** de `datos` con `sorted()` y accede por índice. No modifiques la lista original. Precondición: `datos` no está vacío.

    Explica en un comentario por qué la mediana **no puede calcularse en una sola pasada** con memoria sublineal (a diferencia de la media).

    Verifica con:

    - `mediana([3.0, 1.0, 4.0, 1.0, 5.0])` → `3.0`
    - `mediana([1.0, 2.0, 3.0, 4.0])` → `2.5`
    - `mediana([7.0])` → `7.0`
    """)
    return


@app.function
# Ejercicio 5.9: Batch — mediana de una lista

def mediana(datos: list[float]) -> float:
    """
    Calcula la mediana de datos.
    Precondición: datos no está vacío.
    """
    # La mediana no puede calcularse en una sola pasada porque ...
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5.10: Batch — media móvil de ventana $k$

    La **media móvil** de ventana $k$ transforma una lista de $n$ valores en una lista de $n - k + 1$ valores, donde el $i$-ésimo es la media de `datos[i:i+k]`:
    $$
    \text{MM}_i = \frac{1}{k}\sum_{j=0}^{k-1} \text{datos}[i+j], \quad i = 0, 1, \ldots, n-k.
    $$

    Implementa `media_movil(datos, k)` de **dos formas** y verifica que dan el mismo resultado:

    **Versión A — ingenua** ($O(n \cdot k)$): para cada posición $i$, suma los $k$ elementos de la ventana desde cero.

    **Versión B — ventana deslizante** ($O(n)$): calcula la suma de la primera ventana una sola vez, y para cada ventana siguiente actualiza la suma restando el elemento que sale y sumando el que entra:
    $$
    \text{suma}_{i+1} = \text{suma}_i - \text{datos}[i] + \text{datos}[i+k]
    $$

    Precondiciones: `datos` no está vacío, $1 \le k \le \text{len}(datos)$.

    Verifica con:

    - `media_movil([1.0, 3.0, 5.0, 7.0, 9.0], 3)` → `[3.0, 5.0, 7.0]`
    - `media_movil([2.0, 4.0, 6.0, 8.0], 2)` → `[3.0, 5.0, 7.0]`
    - `media_movil([1.0, 2.0, 3.0], 3)` → `[2.0]`
    """)
    return


@app.cell
def _():
    # Ejercicio 5.10: Batch — media móvil de ventana k

    def media_movil_ingenua(datos: list[float], k: int) -> list[float]:
        """Versión O(n·k): recalcula la suma de cada ventana desde cero."""
        pass

    def media_movil(datos: list[float], k: int) -> list[float]:
        """Versión O(n): ventana deslizante."""
        pass
    return


if __name__ == "__main__":
    app.run()
