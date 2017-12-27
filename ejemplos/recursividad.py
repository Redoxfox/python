"""4.3. Llamadas recursivas
Se denomina llamada recursiva (o recursividad), a aquellas funciones que en su
algoritmo, hacen referencia sí misma.
Las llamadas recursivas suelen ser muy útiles en casos muy puntuales, pero
debido a su gran factibilidad de caer en iteraciones infinitas, deben
extremarse
las medidas preventivas adecuadas y, solo utilizarse cuando sea estrictamente
necesario y no exista una forma alternativa viable, que resuelva el problema
evitando la recursividad. Python admite las llamadas recursivas, permitiendo a
una función, llamarse a sí misma, de igual forma que lo hace cuando llama a
otra función."""


def jugar(intento=1):
    respuesta = input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print ("\nFallaste! Inténtalo de nuevo")
            intento += 1
            jugar(intento)  # Llamada recursiva
        else:
            print ("\nPerdiste!")
    else:
        print ("\nGanaste!")


jugar()
