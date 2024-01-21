print('welcome to the calculator')
var_1 = input("what's your name: ")
print(f'hello {var_1}' )
var_2 = input('what do you want to do')
var_2.lower()
if var_2 == 'multiplica' or 'multiplicacion' or 'multiplicación' or 'multiplicar':
    print(f'como elegiste {var_2}')
    try:
        var_3 = int(input(f'dime un número {var_1}: '))
        var_4 = int(input(f'bien {var_1} dime otro numero: '))
    except:
        var_3 = -1
        var_4= -1
    print(f'la mtiplicación de {var_3} y {var_4} es: {var_3 * var_4}')
if var_2 == 'dividir' or 'division' or 'divide' or 'división':
    print(f'como elegidte {var_2}')
    try:
        var_5 = int(input(f'dime un número {var_1}: '))
        var_6 = int(input(f'bien {var_1} dime otro número'))
    except:
        var_5 = -1
        var_6 = -1
    print(f'la división de {var_5} entre {var_6} es {var_5 / var_6}')
if var_2 == 'sumar' or 'suma':
    print(f'como dijiste {var_2}')
