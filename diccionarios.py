#Diccionario

#crear diccionario -
# estructura dic={"clave1": valor1, "clave2", valor2, ...}

deudaPepe = {"septiembre" : 680,
"octubre": 200,
"noviembre" : 100, #no puede repetir dos claves 
 "diciembre" :100 # podemos repetir valores
}

print (deudaPepe)

deudaLuis = {"septiembre" : 680,
"octubre": 1200,
"noviembre" : 3100, #no puede repetir dos claves 
 "diciembre" :2100 # podemos repetir valores
}

print (deudaLuis)

#consultar los metodos de los diccionarios

#for par in deudaLuis:
#    print(par)

montoDeuda = 0
for clave in deudaLuis.keys(): # trae los ids
    print(clave)

for valor in deudaLuis.values(): #trae los valores
    montoDeuda +=valor
    print(valor)

print (" Luis pagame lo que me debes, hasta ahora me debes : ",montoDeuda)

for c, v in deudaLuis.items(): #devuelve las claves y valores(elementos) c(id), v(dato)
    print("Luis del mes ", c , " me debes ", v , " pesos " )


#agregar valor al diccionario

deudaLuis["enero"] = 1500
print(deudaLuis)

deudaLuis["enero"] = 2500
print (deudaLuis)

deudaLuis.update(febrero=3500, marzo=4500) #añadimos mas 1 par clave=valor
print (deudaLuis)

