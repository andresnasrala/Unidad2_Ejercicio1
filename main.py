from claseEmail import Email

if __name__ == '__main__' :

    idcuenta = input("\n Ingrese el id de la cuenta: ")
    dominio = input ("\n Ingrese el dominio: ")
    tipodominio = input("\n Ingrese el tipo de dominio: ")
    contra = input("\n Ingrese la contraseña: ")

    objeto = Email(idcuenta,dominio,tipodominio,contra)


    print("\n"+objeto.retornaEmail())
    print("\n" + objeto.getDominio())

    direccion = input("Ingrese la dirección de correo: ")


    print("\n" + objeto.crearCuenta(direccion))

    