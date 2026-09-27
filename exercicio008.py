print("Conversor de Medidas")
dist = float(input("Digite a distância em metros: "))
km = dist / 1000
hm = dist / 100
dam = dist / 10
dm = dist * 10
cm = dist * 100
mm = dist * 1000
print(f"A distância de {dist}m corresponde a {km}km")
print(f"A distância de {dist}m corresponde a {hm}hm")
print(f"A distância de {dist}m corresponde a {dam}dam")
print(f"A distância de {dist}m corresponde a {dm}dm")
print(f"A distância de {dist}m corresponde a {cm}cm")
print(f"A distância de {dist}m corresponde a {mm}mm")