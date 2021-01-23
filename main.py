from source.fibonacci import TestFibonacci
from source.pingpong import PingPong
if __name__ == '__main__':
    execute = int(input('1. Para ejecutar el fibonacci TestFibonacci \n'
                        '2. Para ejecutar el pinpong test \n', ))
    while execute > 0:
        if execute == 1:
            n = int(input('ingrese el número fn para saber su k',))
            tfibo = TestFibonacci(n)
            print("-------------------")
            tfibo.fk()
            break
        elif execute == 2:
            juegos = {'Ana': 17, 'José': 15, 'Juan': 10}
            objpingpong=PingPong(**juegos)
            print("-------------------")
            objpingpong.segundopartido()
            break
        else:
            print('No ha seleccionado ninguna opción')
            execute = 0
