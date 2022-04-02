from xml.dom import ValidationErr

print('ingrese su nombre y apellido separados por una "," :')
errorcel = False
while True:
    if errorcel == False:
        try:
            nomap = input()
            if "," in nomap:
                print("Ingrese su numero de telefono: ")
                try:
                    num = int(input())
                    break
                except ValueError:
                    print("Debe ingresar solo numeros! intente nuevamente: ")
                    errorcel = True
            else:
                raise ValidationErr('Debe separar su nombre y apellido con una "," intente nuevamente: ')
        except ValidationErr as e:
            print(e)
    else:
        try:
            num = int(input())
            break
        except ValueError:
            print("Debe ingresar solo numeros! intente nuevamente: ")