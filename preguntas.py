"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""



def pregunta_01():

    total = 0
    with open('data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.split('\t')
            total += int(values[1])
    return total

def pregunta_02():
    contador = {}
    
    with open('data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.split('\t')

            letra = values[0]
            contador[letra] = contador.get(letra, 0) + 1
            
    result = sorted(contador.items())
    return result

def pregunta_03():
    suma = {}
    
    with open('data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.split('\t')

            letra = values[0]
            numero = int(values[1])
            suma[letra] = suma.get(letra, 0) + numero
            
    result = sorted(suma.items())
    return result

def pregunta_04():
    meses = {}

    with open('data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.split('\t')
            mes = values[2][5:7]
            meses[mes] = meses.get(mes, 0) + 1

    result = sorted(meses.items())
    return result

def pregunta_05():
    maxmin = {}

    with open('data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.split('\t')
            letra = values[0]
            numero = int(values[1])

            if letra not in maxmin:
                maxmin[letra] = [numero, numero]
            else:
                maxmin[letra][0] = max(maxmin[letra][0], numero)
                maxmin[letra][1] = min(maxmin[letra][1], numero)

    result = [(letra, maxmin[letra][0], maxmin[letra][1]) for letra in sorted(maxmin)]
        
    return result

def pregunta_06():

    maxmin = {}
    with open('data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.split('\t')
            dicc = values[4].split(',')
            for i in dicc:
                combs = i.split(':')
                if combs[0] not in maxmin:
                    maxmin[combs[0]] = [int(combs[1]), int(combs[1])]
                else:
                    maxmin[combs[0]][0] = min(maxmin[combs[0]][0], int(combs[1]))
                    maxmin[combs[0]][1] = max(maxmin[combs[0]][1], int(combs[1]))

    result = [(comb, maxmin[comb][0], maxmin[comb][1]) for comb in sorted(maxmin)]

    return result

def pregunta_07():
    
    posible = {}
    with open('data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.split('\t')
            numero = int(values[1])
            letra = values[0]

            if numero not in posible:
                posible[numero] = [letra]
            else:
                posible[numero].append(letra)

    result = [(numero, posible[numero]) for numero in sorted(posible)]
    return result

def pregunta_08():

    posible = {}
    with open('data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.split('\t')
            numero = int(values[1])
            letra = values[0]

            if numero not in posible:
                posible[numero] = [letra]
            else:
                if letra in posible[numero]:
                    pass
                else:
                    posible[numero].append(letra)
                    posible[numero].sort()

    result = [(numero, posible[numero]) for numero in sorted(posible)]
    return result

def pregunta_09():

    registro = {}
    with open('data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.split('\t')
            dicc = values[4].split(',')
            for i in dicc:
                combs = i.split(':')
                registro[combs[0]] = registro.get(combs[0], 0) + 1

    result = sorted(registro.items())
    registro_ordenado = {}

    for reg in result:
        registro_ordenado[reg[0]] = reg[1]

    return registro_ordenado

def pregunta_10():

    comb = []
    with open('data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.split('\t')
            letra = values[0]
            dicc = values[4].split(',')
            lets = values[3].split(',')
            x = []
            x.append(letra)
            x.append(len(lets))
            x.append(len(dicc))
            comb.append((x[0],x[1],x[2]))

    return comb

def pregunta_11():

    dicc = {}
    with open('data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.split('\t')
            numero = int(values[1])
            lets = values[3].split(',')
            for letra in lets:
                if letra not in dicc:
                    dicc[letra] = numero
                else:
                    dicc[letra] += numero

    result = sorted(dicc.items())                
    dicc_ordenado = {}
    for reg in result:
        dicc_ordenado[reg[0]] = reg[1]
    return dicc_ordenado

def pregunta_12():

    sum = {}
    with open('data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.split('\t')
            letra = values[0]
            if letra not in sum:
                    sum[letra] = 0
            dicc = values[4].split(',')
            for i in dicc:
                combs = i.split(':')
                sum[letra] += int(combs[1])

    result = sorted(sum.items())                
    sum_ordenado = {}
    for reg in result:
        sum_ordenado[reg[0]] = reg[1]
    return sum_ordenado
                