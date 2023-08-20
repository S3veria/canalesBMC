class canal:
    """
    Un canal, dentro del contexto del lienzo de modelo de negocio (Business Model Canvas),
    es la manera en la que la empresa realiza la entrega de su propuesta de valor a sus clientes,
    es decir, es el método que se utiliza para hacer llegar el producto/servicio de la empresa a los clientes.
    """
    def __init__(self, tipoDeCanal=""):

        self.stateIndex=0
        self.states=["Conciencia", "Evaluacion","Compra","Entrega","Post-Compra"]
        self.tipo=tipoDeCanal
        self.referencias=["Jagie&amp;#322;ka, K. (2021, April 29). Business model canvas: Value, channel and User. Divante. https://www.divante.com/blog/value-channel-user-business-model-canvas",
                          "Traynor, M. (2023, April 29). Choosing the right channels for your business model canvas. SCORE. https://www.score.org/sanluisobispo/resource/blog-post/choosing-right-channels-your-business-model-canvas",
                          "Channels. Business Model Canvas. (2014, August 7). https://bmcintroduction.wordpress.com/channels/ "]

    def cambioDeEstado(self):
        """
        Los canales dentro del business model canvas tienen distintos estados o fases por las que se pasa
        para poder entregarle la propuesta de valor al cliente. Este metodo nos permite camviar entre ellas.
        """
        if self.stateIndex==4:
            self.stateIndex=0
            print(f"Ya se ha pasado por todas las fases de los canales, entonces regresamos a la fase 1: {self.states[self.stateIndex]}")

        else:
            self.stateIndex+=1
            print(f"El estado del canal ha pasado de {self.states[self.stateIndex-1]} to {self.states[self.stateIndex]}")

    def crearConciencia(self):
        """
        Esta función de los canales se encarga de crear conciencia en
         los clientes o en el mercado sobre los producto y servicios 
         que la empresa ofrece
        """
        print("La empresa ha concietizado al cliente sobre los producto/servicios que ofrecen")

    def evaluarPropuestaDeValor(self):
        """
        Esta función de los canales ayuda a que los clientes puedan
         evaluar la propuesta de valor de la empresa
        """
        print("El cliente ha evaluado la propusta de valor de la empresa")
    def compraDeCliente(self, producto=""):
        """
        Esta función de los canales ayuda, como lo siguiere el nombre,
         a que los clientes pueda realizar la compra de un producto
         o la contrataci'on de algún servicio
        """
        if not producto:
            print("Se ha realizado la compra de tu producto/servicio exitosamente")
        else:
            print(f"Se ha realizado la compra de {producto} exitosamente")
    def entregarValorAClientes(self):
        """
        Esta función de los canales se encarga de entregar la
         propuesta de valor que la empresa ofrece
        """
        print("Tu producto/servicio ha sido entregado")
    def apoyoAClientes(self):
        """
        Esta función de los canales se toma en conisderación una
         vez que el producto o servicio ha sido entregado a los clientes;
         esta se encarga de resolver fallas/dudas/quejas que los clientes puedan
         tener después de la entrega de valor.
        """
        #producto=input("Ingresa el nombre del producto con el que requieres ayuda: ")
        print(f"Para obtener ayuda con el producto/servicio marque a la linea de apoyo")

    def setTipoDeCanal(self, tipoDeCanal):
        """
        Este metodo nos permite cambiar el tipo de canal 
        """
        self.tipo=tipoDeCanal
    
    def getTipoDeCanal(self):
        """
        Con este metodo podemos obtener el tipo de canal que se definio al inicializar la clase
        """
        return self.tipo
    
    def printReferencias(self):
        """
        Este metodo lo podemos utilizar para obtener la referencias utilizadas en esta actividad
        """
        for i in self.referencias:
            print(i)

    def realizaEstado(self):
        """
        Este metodo nos ayuda a realizar la accion ligada con el estado actual del canal,
        en otras palabras nos ayuda a realizar las distintas funciones del canal.
        """
        match self.stateIndex:
            case 0:
                self.crearConciencia()
            case 1:
                self.evaluarPropuestaDeValor()
            case 2:
                self.compraDeCliente()
            case 3:
                self.entregarValorAClientes()
            case 4:
                self.apoyoAClientes()

    def darEjemploDeEstado(self):
        """
        Este metodo nos ayuda a ejemplificar los distintos estados del canal
        """
        match self.stateIndex:
            case 0:
                print("Ej: Anuncios en la tele, en redes o en el periodico")
            case 1:
                print("Ej: Letreros o anuncios en el supermercado")
            case 2:
                print("Ej: Compra de un Pan Bimbo")
            case 3:
                print("Ej: Entrega del Pan Bimbo")
            case 4:
                print("Ej: Ventas directas, lealtad de clientes, etc.")     

help(canal)

for i in range(3):
    print()

canalBimbo=canal()
for j in range(5):
    canalBimbo.realizaEstado()
    canalBimbo.darEjemploDeEstado()
    canalBimbo.cambioDeEstado()

print()
print("Referencias:")
canalBimbo.printReferencias()
