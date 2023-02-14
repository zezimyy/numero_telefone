import phonenumbers
from phonenumbers import geocoder, carrier
loop = True

while loop == True:
  print()
  numero = input("Digite seu numero: ")
  numero = phonenumbers.parse(numero)

  print(geocoder.description_for_number(numero, "pt-br"))
  print(carrier.name_for_number(numero, "pt-br"))
  print()
  loop = input("Deseja parar o loop? [s/n]   ")
  if loop == "s":
    break
  else:
    loop = True