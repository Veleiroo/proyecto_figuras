from lib import cuadrado, triangulo, rectangulo, circunferencia
print("\n- Proyecto Figuras\n")

# Para el cuadrado
lado = 4
print(f"{cuadrado.get_identificador()}:")
print(f"El área de un {cuadrado.get_identificador()} de lado {lado} es {cuadrado.get_area(lado)}"
      f" y el perímetro es {cuadrado.get_perimetro(lado)}\n")

# Para el triángulo 
lado1, lado2, lado3 = 3, 4, 3
altura = 3
print(f"{triangulo.get_identificador()}:")
print(f"El area de un {triangulo.get_identificador()} de base {lado1} y altura {altura}"
      f" es {triangulo.get_area(lado1, altura)} y el perimetro es {triangulo.get_perimetro(lado1, lado2, lado3)}\n")

# Para el rectángulo
base = 4
altura = 2
print(f"{rectangulo.get_identificador()}:")
print(f"El área de un {rectangulo.get_identificador()} de base {base} "
      f"y altura {altura} es {rectangulo.get_area(base, altura)}"
      f" y el perímetro es {rectangulo.get_perimetro(base, altura)}\n")

# Para el círculo
radio = 4
print(f"{circunferencia.get_identificador()}:")
print(f"El área de un {circunferencia.get_identificador()} de radio {radio} es {circunferencia.get_area(radio)}"
      f" y el perímetro es {circunferencia.get_perimetro(radio)}\n")
