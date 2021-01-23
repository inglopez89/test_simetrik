import json


class PingPong:
    """
    This class is for get the person who lose the second game
    and get the information about his games losed
    Params
    **partidos: is dictionary with the games
    return
    Print results who lose the second game and json with the game losed in order
    """
    def __init__(self, **partidos):
        self.partidos = partidos

    def __ppares(self, n_partidos):
        """
        This a private method is for validate the games
        :param n_partidos: is a number for minimal games playing
        :return ppares: is boolean value
        """
        try:

            if n_partidos % 2 == 0:
                p_pares = True
            else:
                p_pares = False
            return p_pares
        except Exception as e:
            print('An error has occurred for fn ppares: ', e)

    def __p_perdidos(self, p_pares, t_partidos):
        """
        This a private method is for create a list of games playing for depending of total games playing
        :param p_pares: is a boolean value for create the list
        :param t_partidos: is a number of total games
        :return p_perdidos: is a list with losing games
        """
        try:
            if p_pares:
                p_perdidos = [x for x in range(1, int(t_partidos)) if x % 2 == 0]
            else:
                p_perdidos = [x for x in range(1, int(t_partidos)) if x % 2 != 0]

            return p_perdidos
        except Exception as e:
            print('An error has occurred in fn p_perdidos: ', e)

    def segundopartido(self):
        """
        This public method print the player what lose the second game and json with game losed
        """
        # initial variables
        t_partidos = 0
        l_partidos = []
        # iter for get the values of dictionary
        for v in self.partidos.values():
            # save values in a list for get the less games played
            l_partidos.append(v)
            # sum of total of games for all players
            t_partidos += v
        # get the less game played
        min_partidos = min(l_partidos)
        # As the pinpong is game of two divide the value of 2 for get the total of games
        t_partidos = t_partidos/2
        # call the function for get if the less match playing, played in the first game o second.
        p_pares = self.__ppares(min_partidos)
        # Call function for get the list with the game lose
        p_perdidos = self.__p_perdidos(p_pares, t_partidos)
        # iter the value get the name of the player who lose the second game
        if 2 in p_perdidos:
            for k, v in self.partidos.items():
                if v == min_partidos:
                    perdedor = k
                    break
        # print results
        print(f'Who lose the second match is: {perdedor}')
        # create a dict whith the person who lose the second game with value list of all game losed
        jsonpartidos = {perdedor: p_perdidos}
        resultado = json.dumps(jsonpartidos)
        print(f'resultado: {resultado}')


if __name__ == '__main__':
    juegos = {'Ana': 17, 'José': 15, 'Juan': 10}
    partido = PingPong(**juegos)
    partido.segundopartido()
