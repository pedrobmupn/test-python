item_precio = float(input("Ingrese el precio del item a elegir: "))
cantidad = int(input("Ingrese la cantidad de items a comprar: "))

valor_compra = cantidad * item_precio

# Dscto. del 5% si la cantidad es mayor a 10
if cantidad > 10:
    dscto = valor_compra * 0.5
else :
    dscto = 0
total = valor_compra - dscto

print(f"Total a pagar: S/{valor_compra}")
print(f"Descuento de S/{dscto}")
print(f"Toal con dscto: S/{total}")