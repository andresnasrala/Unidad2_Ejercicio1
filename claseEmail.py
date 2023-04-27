class Email : 
    __idcuenta = ''
    __dominio = ''
    __tipodominio = ''
    __contra = ''


    def __init__(self ,idcuenta,dominio,tipodominio,contra):

        self.__idcuenta = idcuenta 
        self.__dominio = dominio 
        self.__tipodominio = tipodominio 
        self.__contra = contra 


    def retornaEmail (self):

        return self.__idcuenta + "@"+self.__dominio+"."+self.__tipodominio

    
    def getDominio(self): 

        return self.__dominio

    
    def crearCuenta(self,direccion): 

        if direccion.find('@' and '.'):

            return "Correo Válido"
        
        else: 

            return "ERROR, Correo inválido"
     