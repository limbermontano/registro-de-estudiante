class RegistroMateria:
    def __init__(self):
        self.estudiante = ''
        self.apellido = ''
        self.carrera = ''
        self.materias = []
    def presentarse(self):
        print("****************Presentacion del Estudiante {} {}****************".format(self.estudiante, self.apellido))
        print('***MATERIAS***')
        if(self.materias):
            for i in self.materias:
                print('Materia= {} '.format(i))
        else:
            print("El estudiante todavia no registro materias")
        return "Soy el est: {} de la carrera de {}".format(self.estudiante, self.carrera)
    def registrarMateria(self):
        print("Gestión de registro de materias para Estudiantes")
        nombre=input('Dijite el Nombre:\n')
        apellido=input('Digite Apellido:\n')
        carrera=input('Digite Carrera:\n')
        materia = input('Digite la materia:\n')
        self.estudiante=nombre.upper()
        self.apellido=apellido.upper()
        self.carrera=carrera.upper()
        self.materias.append(materia)
        print( "Datos del Estudiante {} registrada exitosamente.!".format(nombre))
        adicional = input("Desea registrar una materia adicional?: y/n:\n ")
        if (adicional == 'y'or adicional == 'Y'):
            self.mater()
        else:
            return "Materias registradas exitosamente.!!"
    def mater(self):
        materia = input('Digite la materia:\n')
        self.materias.append(materia)
        return 'Registro exitoso'

    def menu(self):
        opciones = """
        Menu de la aplicación
           **Registros**
        
        1.- Registro de Estudiantes y Materias
        2.- Presentarse
                    """
        print(opciones)
        eleccion = int(input('Elija una opción:\n'))
        if(eleccion == 1):
            print(self.registrarMateria())
            print(self.menu())
        elif(eleccion == 2):
            print(self.presentarse())
            print(self.menu())
        else:
            print("Elija del opcion del menu")
            print(self.menu())

estudiante=RegistroMateria()
print(estudiante.menu())
# pedro = RegistroMateria("Pedro", "Perez", "Ingeniería de Sistemas")
# pablo = RegistroMateria("Pablo", "Mercado", "Ingeniería Comercial")
# print(pedro.menu())

