import SQLconnection

cursor = SQLconnection.db.cursor()

registro_especie = False
registro_zoo = False
registro_animal = False
ver_animal = False
ver_zoo = False
seguir = True
total_id = 0

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
            total_id += 1

        cod_ext = int(input('Ingrese codigo UICN: '))

        while cod_ext <= 0 or cod_ext > total_id:
            print('<...Codigo invalido...>')
            cod_ext = int(input('Ingrese codigo UICN: '))
        total_id = 0

        print('ID | NOMBRE')

        cursor.execute('SELECT * FROM familia')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)
            total_id += 1

        cod_fam = int(input('Ingrese codigo de familia: '))
        while cod_fam <= 0 or cod_fam > total_id:
            print('<...Codigo invalido...>')
            cod_fam = int(input('Ingrese codigo de familia: '))
        total_id = 0

        val = (nom_vul, nom_cient, cod_ext, cod_fam)

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

        nombre = str(input('Ingrese nombre: '))

        print('Ingrese fecha de nacimiento: ')

        dia = int(input('Ingrese dia[dd]: '))

        while dia <= 0 or dia > 31:
            print('<Error, Ingrese valores entre 1 y 31...>')
            dia = int(input('Ingrese dia[dd]: '))

        mes = int(input('Ingrese mes[mm]: '))

        while mes <= 0 or mes > 12:
            print('<...Error, Ingrese valores entre 1 y 12...>')
            mes = int(input('Ingrese mes[mm]: '))

        anio = int(input('Ingrese año[aaaa]: '))

        while anio < 1000 or anio > 9999:
            print('<...Ingrese cuatro digitos...>')
            anio = int(input('Ingrese año[aaaa]: '))

        nacimiento = str(dia) + '/' + str(mes) + '/' + str(anio)

        print('ID | SEXO')

        cursor.execute('SELECT * FROM sexo')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)
            total_id += 1

        sexo = int(input('Ingrese codigo de su sexo:'))

        while sexo <= 0 or sexo > total_id:
            print('<...Codigo invalido...>')
            sexo = int(input('Ingrese codigo de su sexo:'))
        total_id = 0

        print('ID | NOMB_VULGAR | NOMB_CIENT')

        cursor.execute('SELECT id, nombre_vulgar, nombre_cientifico FROM especie')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)
            total_id += 1

        especie = int(input('Ingrese codigo de especie: '))

        while especie <= 0 or especie > total_id:
            print('<...Codigo invalido...>')
            especie = int(input('Ingrese codigo de especie: '))
        total_id = 0

        print('ID | NOMBRE')

        cursor.execute('SELECT id, nombre FROM zoologico')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)
            total_id += 1

        zoo = int(input('Ingrese codigo de zoologico: '))

        while zoo <= 0 or zoo > total_id:
            print('<...Codigo invalido...>')
            zoo = int(input('Ingrese codigo de zoologico: '))
        total_id = 0

        cursor.execute('SELECT id, nombre FROM pais ')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)
            total_id += 1

        pais = int(input('Ingrese codigo de pais de origen: '))

        while pais <= 0 or pais > total_id:
            print('<...Codigo invalido...>')
            pais = int(input('Ingrese codigo de pais de origen: '))
        total_id = 0

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

        tamano = str(input('Ingrese tamaño de zoologico en HA: '))

        cursor.execute('SELECT id, nombre FROM ciudad')

        resultados = cursor.fetchall()

        for x in resultados:
            print(x)
            total_id += 1

        ciudad = int(input('Ingrese codigo de ciudad donde se ubica: '))

        while ciudad <= 0 or ciudad > total_id:
            print('<...Codigo invalido...>')
            ciudad = int(input('Ingrese codigo de ciudad donde se ubica: '))
        total_id = 0

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

print('<...Hasta pronto!...>')
