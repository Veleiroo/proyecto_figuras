from lib import cuadrado, triangulo, rectangulo
print("Proyecto Figuras")

# Para el cuadrado
lado = 4
print(cuadrado.get_identificador())
print(f"El área de un cuadrado de lado {lado} es: {cuadrado.get_area(lado)}"
      "y el perímetro es: {cuadrado.get_perimetro(lado)}")

# Para el triángulo
base = 4
altura = 2
print(triangulo.get_identificador())
print(f"El area de un triangulo {triangulo.get_identificador()} de base {base} y altura {altura} 
      es: {triangulo.get_area(base, altura)} y el perimetro es: {triangulo.get_perimetro(base, altura)}")

# Para el rectángulo
base = 4
altura = 2
print(rectangulo.get_identificador())
print(f"El área de un {rectangulo.get_identificador()} de base {base} "
      f"y altura {altura} es: {rectangulo.get_area(base, altura)}"
      f"y el perímetro es: {rectangulo.get_perimetro(base, altura)}")