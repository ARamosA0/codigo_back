#clase para administrar los usuarios de un sisitema 
class Usuario:
    def __init__(self, nom, pwd):
        self.nom = nom
        self.pwd = pwd

    def iniciar(self):
        if (self.nom == 'admin' and self.pwd == '12345'):
            print("Bienvenido "+ self.nom)
        else:
            print("Error")


#Creacion de Usuarios
usuario1 = Usuario('admin', 'admin')
usuario1.iniciar()


usuario2 = Usuario('admin', '12345')
usuario2.iniciar()