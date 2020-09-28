""" A=[{"valor1":888110, "valor2":194883},
{"valor1":407781, "valor2":590886},
{"valor1":845133, "valor2":89558},
{"valor1":967746, "valor2":828683},
{"valor1":573329, "valor2":828405},
{"valor1":67428 , "valor2":917308},
{"valor1":380572, "valor2":936018},
{"valor1":241247, "valor2":962671},
{"valor1":550278, "valor2":866113},
{"valor1":313949, "valor2":973526},
{"valor1":173363, "valor2":166216},
{"valor1":345152, "valor2":189064},
{"valor1":64178 , "valor2":32585}]


def sum_array(tam, array):
    cont = 0
    sum_items = []

    while cont < tam:
        sum_items=array[cont]["valor1"] + array[cont]["valor2"]
        cont += 1
        print (sum_items)
    
    

sum_array(13,A) """


A=[[2275421,   -1146571],
[8177823,    -1912164],
[-2503392,   9189753],
[7862686,   9020412],
[9194819,   4801924],
[-9111834,  5368733],
[-8901110, 3573146],
[5572171, -698433],
[9876997, 3112607],
[369609, 3245817],
[-8258360, -1312741],
[-4354945, -1993829],
[-6826072, 4568366],
[3962891, 1577041],
[-6381871, -6257652],
[1655644, 5893549],
[2595776, -166533],
[-6018615, -9907615],
[-976779, -8155928],
[9112796, -1781960]]

def sum_array(tam, array):
    cont = 0
    while cont < tam:
        if array[cont][0] < array[cont][1]:
            print(array[cont][0])
        else:
            print(array[cont][1])
    
        cont += 1

    
    

sum_array(20,A)

