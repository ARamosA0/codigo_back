# f = open('alumnos.txt','w')
# f.write('Aldo Ramos')



f = open('alumnos.txt','r')
alumnos = f.read()

listaAlumnos = alumnos.splitlines()
print(listaAlumnos)

listaResultado=[]

for dicAlumnos in listaAlumnos:
    listaDicAlumnos = dicAlumnos.split(',')
    print(listaDicAlumnos)
    dicAlumnos = {
        'nombre':listaDicAlumnos[0],
        'email':listaDicAlumnos[1],
        'celular':listaDicAlumnos[2]
    }
    listaResultado.append(dicAlumnos)
print(listaResultado)
f.close