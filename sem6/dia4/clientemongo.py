from pymongo import MongoClient

cliente = MongoClient('mongodb://127.0.0.1:27017')

db = cliente['cursos']

colAlumnos = db['alumnos']

dicNuevoAlumno = {
    "nombre":"Pedor Fernandez",
    "email":"pedrito@gmail.com",
    "nota":7,
}

NuevoAlumnoId = colAlumnos.insert_one(dicNuevoAlumno)

print("Nuevo Alumno: "+str(NuevoAlumnoId))

for alumno in colAlumnos.find():
    print(alumno["nombre"] + " - "+alumno["email"]+" - "+str(alumno["nota"]))