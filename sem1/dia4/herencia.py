class Persona:
    def __init__(self, name, email):
        self.name=name
        self.email=email
    def mostrar(self):
        print ("Nombre: " + self.name + " Email: " + self.email)

class Alumno(Persona):
    pass


    
    
class Profesor(Persona):
    def __init__(self, name, email, module):
        super().__init__(name, email)
        self.module = module

    def mostrar(self):
        super().mostrar()
        print("Dicata el modulo de: " + self.module)


alum1 = Alumno("aldo", "aldo@gmail.com")
alum1.mostrar()

prof = Profesor("pro1", "prof@gmail.com", "back")
prof.mostrar()
