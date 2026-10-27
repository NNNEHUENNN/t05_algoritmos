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
    # Ejercicios 5.11 - 5.16 del Tema 5

    ## Ejercicio 5.11: Invariante de la suma de los primeros $n$ enteros

    Considera el siguiente bucle que calcula $S = \sum_{k=1}^{n} k$:

    ```python
    def suma_hasta(n: int) -> int:
        acumulado = 0
        for k in range(1, n + 1):
            acumulado += k
        return acumulado
    ```

    El invariante de este bucle es: *al inicio de la iteración con valor `k`, la variable `acumulado` contiene $\sum_{i=1}^{k-1} i$.*

    **Parte A:** Copia el bucle y añade un `assert` dentro del cuerpo que verifique el invariante en cada iteración. Usa la fórmula de Gauss $\sum_{i=1}^{m} i = m(m+1)/2$ para el valor esperado.

    **Parte B:** Verifica con `assert` la **postcondición** justo antes del `return`: `acumulado == n * (n + 1) // 2`.

    **Parte C:** Ejecuta `suma_hasta_verificada(10)` y `suma_hasta_verificada(100)` y comprueba que ningún `assert` falla.
    """)
    return


@app.cell
def _():
    # Ejercicio 5.11: Invariante de la suma de los primeros n enteros

    def suma_hasta_verificada(n: int) -> int:
        acumulado = 0
        for k in range(1, n + 1):
            # Parte A: assert del invariante aquí
            acumulado += k
        # Parte B: assert de la postcondición aquí
        return acumulado

    print(suma_hasta_verificada(10))   # 55
    print(suma_hasta_verificada(100))  # 5050
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5.12: Primer test con `pytest` — `media_aritmetica`

    La función `media_aritmetica` definida abajo calcula la media aritmética de una lista. Escribe las siguientes funciones de prueba en las celdas de código (en un proyecto real irían en `test_estadistica.py`):

    1. `test_media_normal()` — lista de 4 elementos con resultado conocido.
    2. `test_media_un_elemento()` — caso límite: lista de un solo elemento.
    3. `test_media_negativos()` — lista con negativos; la media puede ser negativa.
    4. `test_media_lista_vacia()` — la función debe retornar `None` (no lanzar excepción).
    5. `test_media_flotantes()` — verificar con `abs(resultado - esperado) < 1e-12`.

    Ejecuta cada función de prueba directamente en Marimo (llámala al final de la celda) y verifica que ninguna falla.
    """)
    return


@app.cell
def _():
    # Ejercicio 5.12: Tests para media_aritmetica

    def media_aritmetica(datos: list[float]) -> float | None:
        """Media aritmética. Retorna None si la lista está vacía."""
        if not datos:
            return None
        return sum(datos) / len(datos)

    # Escribe aquí las funciones test_* y ejecútalas

    def test_media_normal():
        assert media_aritmetica([1.0, 2.0, 3.0, 4.0]) == 2.5

    def test_media_un_elemento():
        pass   # completa

    def test_media_negativos():
        pass   # completa

    def test_media_lista_vacia():
        pass   # completa

    def test_media_flotantes():
        pass   # completa

    # Ejecutar los tests
    test_media_normal()
    test_media_un_elemento()
    test_media_negativos()
    test_media_lista_vacia()
    test_media_flotantes()
    print("Todos los tests pasaron.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5.13: `pytest.approx` — tests para `desviacion_estandar`

    La comparación estricta `==` entre flotantes es problemática en las pruebas. `pytest.approx` usa una tolerancia relativa de $10^{-6}$ por defecto. En Marimo podemos simularla con `abs(a - b) < 1e-10`.

    Dada la función `desviacion_estandar` que se basa en la `varianza` del ejercicio 5.9, escribe los siguientes tests:

    1. `test_desv_conocida()` — lista `[2,4,4,4,5,5,7,9]`: la desviación estándar es exactamente `2.0`.
    2. `test_desv_constante()` — lista de elementos iguales: la desviación estándar es `0.0`.
    3. `test_desv_dos_elementos()` — `[0.0, 10.0]`: la desviación estándar es `5.0`.
    4. `test_desv_un_elemento()` — caso límite: `[42.0]` → `0.0`.

    Para cada test, usa `abs(resultado - esperado) < 1e-10` en lugar de `==`.
    """)
    return


@app.cell
def _():
    # Ejercicio 5.13: pytest.approx — tests para desviacion_estandar
    import math

    def varianza(datos: list[float]) -> float:
        """Varianza poblacional."""
        n = len(datos)
        media = sum(datos) / n
        return sum((x - media) ** 2 for x in datos) / n

    def desviacion_estandar(datos: list[float]) -> float | None:
        """Desviación estándar poblacional. Retorna None si la lista está vacía."""
        if not datos:
            return None
        return math.sqrt(varianza(datos))

    # Escribe aquí los tests usando abs(resultado - esperado) < 1e-10

    def test_desv_conocida():
        resultado = desviacion_estandar([2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0])
        assert abs(resultado - 2.0) < 1e-10

    def test_desv_constante():
        pass   # completa

    def test_desv_dos_elementos():
        pass   # completa

    def test_desv_un_elemento():
        pass   # completa

    test_desv_conocida()
    test_desv_constante()
    test_desv_dos_elementos()
    test_desv_un_elemento()
    print("Todos los tests de desviacion_estandar pasaron.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5.14: Conteo — moda de una lista

    La **moda** de una lista es el valor (o valores) que aparece con mayor frecuencia. Si hay varios con la misma frecuencia máxima, se retornan todos en orden creciente.

    Implementa `moda(datos)` usando el patrón de conteo con un diccionario:

    1. Construye `freq: dict[float, int]` recorriendo `datos` una vez.
    2. Determina la frecuencia máxima con una acumulación sobre el diccionario.
    3. Filtra las claves con frecuencia máxima y retorna la lista ordenada.

    Precondición: `datos` no está vacío.

    Verifica con:

    - `moda([1.0, 2.0, 2.0, 3.0, 3.0, 4.0])` → `[2.0, 3.0]`
    - `moda([5.0, 5.0, 5.0])` → `[5.0]`
    - `moda([1.0, 2.0, 3.0])` → `[1.0, 2.0, 3.0]` (todos con freq = 1)
    - `moda([7.0])` → `[7.0]`
    """)
    return


@app.function
# Ejercicio 5.14: Conteo — moda de una lista

def moda(datos: list[float]) -> list[float]:
    """
    Retorna la lista de valores modales en orden creciente.
    Precondición: datos no está vacío.
    """
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5.15: Decodificador Morse

    Estás recibiendo un mensaje (de una única oración) codificado utilizando el **código Morse internacional**.

    Cada letra o dígito se representa mediante una secuencia de puntos (.) y rayas (-). Los símbolos Morse correspondientes a caracteres consecutivos de una misma palabra están separados por un espacio simple. Las palabras consecutivas están separadas por la cadena / .

    Tu tarea consiste en decodificar el mensaje y mostrar el texto original utilizando letras mayúsculas y dígitos. Para ello escribe una función con signatura `morse_decode(mensaje: str) -> str:` que realice la decodificación.

    Ejemplos:

    - `morse_decode('.... --- .-.. .- / -- ..- -. -.. ---')  # HOLA MUNDO`
    - `morse_decode('.--. -.-- - .... --- -. / ...--')  # PYTHON 3`
    - `morse_decode('-.-. --- -.. .. --. --- / -- --- .-. ... .')  # CODIGO MORSE`

    Para facilitar el trabajo se te proporciona un diccionario con el código Morse internacional (26 letras del alfabeto inglés además de la `Ñ` y los dígitos del `0` al `9` )
    """)
    return


@app.cell
def _():
    # Ejercicio 5.15: Decodificador Morse

    morse_to_char = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
        "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
        "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "--.--": "Ñ",
        "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", 
        "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X", 
        "-.--": "Y", "--..": "Z", "-----": "0", ".----": "1", "..---": "2",
        "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", 
        "---..": "8", "----.": "9"
    }

    def morse_decode(mensaje: str) -> str:
        pass


    mensajes_morse = [
        ".- .-.. .--. .... .- / --...",
        ".- - . -. -.-. .. --- -.",
        "--- .--. . .-. .- -.-. .. --- -. / .-. . .. -. ---",
        "-.-. .. - .- / .--. .- .-. .. ...",
        "-- .- .-. - . ... / ----- ----. ----- -----",
        ".-.. .-.. . ...- .- .-. / .--. .- .-. .- --. ..- .- ... / .- --.. ..- .-..",
        "... --- .-.. .. -.-. .. - .- / -.-. --- -. ..-. .. .-. -- .- -.-. .. --- -.",
        "..-. .. -. / -.. . / - .-. .- -. ... -- .. ... .. --- -."
    ]

    # decodificación
    # mensajes_char = ["ALPHA 7", "ATENCION", "OPERACION REINO", "CITA PARIS", "MARTES 0900",
    #                  "LLEVAR PARAGUAS AZUL", "SOLICITA CONFIRMACION", "FIN DE TRANSMISION"]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5.16: Codificador Morse

    Escribe una función `morse_encode()` que realiza el proceso inverso al de la función `morse_decode()` del ejercicio 5.15. Para ello genera primeramente el diccionario `char_to_morse` convirtiendo las llaves de `morse_to_char` en valores y viceversa (trata de usar comprensión de diccionarios).

    Comprueba tu función con las listas `mensajes_morse` y `mensajes_char` del ejercicio 5.15.
    """)
    return


@app.cell
def _():
    # Ejercicio 5.16: Codificador Morse

    char_to_morse = {}

    def morse_encode(mensaje: str) -> str:
        pass


    mensajes_char = ["ALPHA 7", "ATENCION", "OPERACION REINO", "CITA PARIS", "MARTES 0900",
                     "LLEVAR PARAGUAS AZUL", "SOLICITA CONFIRMACION", "FIN DE TRANSMISION"]
    return


if __name__ == "__main__":
    app.run()
