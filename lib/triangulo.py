# Archivo: triangulo.py

def get_identificador() -> str:
    return "triángulo"

def get_area(base: int, altura: int) -> float:
    """
    Calcula el área de un triángulo usando la fórmula: (base * altura) / 2
    """
    return (base * altura) / 2

def get_perimetro(lado_a: int, lado_b: int, lado_c: int) -> int:
    """
    Calcula el perímetro sumando los tres lados del triángulo.
    """
    return lado_a + lado_b + lado_c
