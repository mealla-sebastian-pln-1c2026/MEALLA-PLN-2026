oracion="Hola, ¿cómo estás?"
valor= 6
interesante= True

print(type(oracion))
print(type(valor))
print(type(interesante))

palabra1="procesamiento"
palabra2="lenguaje"
frase= palabra1 + "diego" + palabra2
print(frase)

print (palabra1," de " , palabra2)

palabra3 = "natural"
palabra1 == palabra3

numero1=1
numero2=2
print("¿Los números son iguales?")
print(numero1==numero2)

vocabulario=["belleza", "inteligencia", "elegancia"]
print("'belleza'es lo primero que pense cuando te vi","belleza" in vocabulario )
print("¿'amabilidad' está en el vocabulario?","amabilidad" in vocabulario)
print("'ejlegancia'pienso cuando te veo","elegancia" in vocabulario)

oracion4="Que manera de bailar anoche"
print("'manera' está en la oración?", "manera" in oracion4)
print("'zapaterar' está en la oración?", "zapaterar" in oracion4)
4

numero_usuario= int(input("Ingresa un numero del 1 al 10:"))
type(numero_usuario)2


#Bucles FOR
TEXTO="El ejercito Argentino de la patria"
print ("Palabras mas largas")
for palabra in TEXTO.split():
    if len (palabra ) > 4:
        print (F"{palabra} ({len(palabra)}letras)") #F es para formatear (palabra) 