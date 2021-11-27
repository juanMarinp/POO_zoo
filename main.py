import SQLconnection

cursor = SQLconnection.db.cursor()

registro_especie = False
registro_zoo = False
registro_animal = False
ver_animal = False
ver_zoo = False
seguir = True

while seguir:
    print('1 = Ingresar especie\n2 = Ingresar animal\n3 = Ingresar zoologico')
    print('4 = Ver animales\n5 = Ver zoologicos\n9 = Salir')
    pregunta = int(input('Que desea realizar?: '))

    if pregunta == 1:
        registro_especie = True
    if pregunta == 2:
        registro_animal = True
    if pregunta == 3:
        registro_zoo = True
    if pregunta == 4:
        ver_animal = True
    if pregunta == 5:
        ver_zoo = True
    if pregunta == 9:
        seguir = False

    while registro_especie:

        sql = "INSERT INTO especie (nombre_vulgar, nombre_cientifico, codigo_ext, codigo_familia) values (%s, %s, %s, %s);"

        nom_vul = input('Ingrese nombre vulgar: ')

        nom_cient = input('Ingrese nombre cientifico: ')

        print('ID | SIGLA | ESTADO')

        cursor.execute('SELECT * FROM uicn')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)

        cod_ext = int(input('Ingrese codigo UICN: '))

        print('ID | NOMBRE')

        cursor.execute('SELECT * FROM familia')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)

        cod_fam = int(input('Ingrese codigo de familia: '))

        val = (nom_vul, nom_cient, cod_ext, cod_ext)

        cursor.execute(sql, val)

        SQLconnection.db.commit()

        pregunta = input('Desea Ingresar otra especie?[S/n]: ')
        if pregunta.upper() == 'S':
            registro_especie = True
        else:
            registro_especie = False
    # ----------------REGISTRO ANIMAL-----------------
    while registro_animal:

        sql = 'INSERT INTO animal(nombre, nacimiento, fk_sexo, fk_especie, fk_zoo, fk_pais) VALUES(%s, %s, %s, %s, %s, %s)'

        nombre = input('Ingrese nombre: ')

        print('Ingrese fecha de nacimiento: ')

        dia = int(input('Ingrese dia[dd]: '))

        if dia <= 0 or dia > 31:
            print('<Error, Ingrese valores entre 1 y 31...>')
            dia = int(input('Ingrese dia[dd]: '))

        mes = int(input('Ingrese mes[mm]: '))

        if mes <= 0 or mes > 12:
            print('<...Error, Ingrese valores entre 1 y 12...>')
            mes = int(input('Ingrese mes[mm]: '))

        anio = int(input('Ingrese año[aaaa]: '))

        if anio < 1000 or anio > 9999:
            print('<...Ingrese cuatro digitos...>')
            anio = int(input('Ingrese año[aaaa]: '))

        nacimiento = str(dia) + '/' + str(mes) + '/' + str(anio)

        print('ID | SEXO')

        cursor.execute('SELECT * FROM sexo')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)

        sexo = int(input('Ingrese codigo de su sexo:'))

        print('ID | NOMB_VULGAR | NOMB_CIENT')

        cursor.execute('SELECT id, nombre_vulgar, nombre_cientifico FROM especie')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)

        especie = int(input('Ingrese codigo de especie:'))

        print('ID | NOMBRE')

        cursor.execute('SELECT id, nombre FROM zoologico')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)

        zoo = int(input('Ingrese codigo de zoologico: '))

        cursor.execute('SELECT id, nombre FROM pais ')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)

        pais = int(input('Ingrese codigo de pais de origen: '))

        val = (nombre, nacimiento, sexo, especie, zoo, pais)

        cursor.execute(sql, val)

        SQLconnection.db.commit()

        pregunta = input('Desea Ingresar otro animal?[S/n]: ')
        if pregunta.upper() == 'S':
            registro_animal = True
        else:
            registro_animal = False

    while registro_zoo:

        sql = 'INSERT INTO zoologico(nombre, presupuesto, tamanio, fk_ciudad) values (%s, %s, %s, %s);'

        nombre = input('Ingrese nombre: ')

        presupuesto = int(input('Ingrese presupuesto: '))

        tamano = input('Ingrese tamaño de zoologico en HA: ')

        cursor.execute('SELECT id, nombre FROM ciudad')

        resultados = cursor.fetchall()

        for x in resultados:
            print(x)

        ciudad = int(input('Ingrese codigo de ciudad donde se ubica: '))

        val = (nombre, presupuesto, tamano, ciudad)

        cursor.execute(sql, val)

        SQLconnection.db.commit()

        pregunta = input('Desea Ingresar otro zoologico?[S/n]: ')
        if pregunta.upper() == 'S':
            registro_zoo = True
        else:
            registro_zoo = False

    if ver_animal:
        cursor.execute('SELECT id, nombre FROM animal')

        resultado = cursor.fetchall()

        print('ID | NOMBRE')

        for x in resultado:
            print(x)
        ver_animal = False

        continuar = input('Presione Enter para continuar...')

    if ver_zoo:
        cursor.execute('SELECT id, nombre FROM zoologico')

        resultado = cursor.fetchall()

        print('ID | NOMBRE')

        for x in resultado:
            print(x)

        continuar = input('Presione Enter para continuar...')

        ver_zoo = False
