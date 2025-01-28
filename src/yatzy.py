from src.pips import Pips

class Yatzy:

    @staticmethod
    def chance(*dice):
        return sum(dice)
    '''Unificamos las variables con el * para hacerlo mas sostenible y simplificamos 
    el codigo utilizando sum para sumar todos los resultados a la vez'''

    @staticmethod
    def yatzy(*dice):
        if len(set(dice)) == 1:
            return 50
        return 0
    '''Refactorizamos toda la función eliminando todos los valores repetidos con set'''
        
    @staticmethod
    def ones(*dice):
        return dice.count(1) * 1

    @staticmethod
    def twos(*dice):
        return dice.count(2) * 2
    
    @staticmethod
    def threes(*dice):
        return dice.count(3) * 3

    def fours(*dice):
        return dice.count(4) * 4

    def fives(*dice):
       return dice.count(5) * 5

    def sixes(*dice):
        return dice.count(6) * 6
    '''Simplificamos las seis funciones de números repetidos de los unos hasta los seises con count'''

    def score_pair(*dice):
        pair=[]
        for num in range (1,7):
            die = dice.count(num)
            if die >= 2:
               pair.append(num)
        if pair:
            return max(pair) * 2
        else:
            return 0

    @staticmethod
    def two_pair(*dice):
        pair=[]
        for num in range (1,7):
            die = dice.count(num)
            if die >= 2:
               pair.append(num)
        if len(pair) == 2:
            return sum(pair) * 2
        else:
            return 0
    @staticmethod
    def four_of_a_kind(*dice):
        veces_contadas= [0] * 6 
        for die in dice:
            veces_contadas[die -1] += 1
        for num in range(6):
            if veces_contadas [num] >= 4:
                return (num +1) * 4
        return 0
    
    @staticmethod
    def three_of_a_kind (*dice):
        veces_contadas= [0] * 6 
        for die in dice:
            veces_contadas[die -1] += 1
        for num in range(6):
            if veces_contadas[num] >= 3:
                return (num +1) * 3
        return 0
    '''Refactorizamos las funciones de pares y tríos para que sean más sostenibles'''

    @staticmethod
    def smallStraight(*dice):
        if sorted(dice) == [1, 2, 3, 4, 5] or sorted(dice) == [2, 3, 4, 5, 1]:
            return 15
        else:
            return 0

    @staticmethod
    def largeStraight(*dice):
        if sorted(dice) == [2, 3, 4, 5, 6] or sorted(dice) == [6, 2, 3, 4, 5]:
            return 20
        else:
            return 0

    @staticmethod
    def fullHouse(*dice):
        counts = [dice.count(num) for num in range(1, 7)]
        if 2 in counts and 3 in counts:
            return (counts.index(2) + 1) * 2 + (counts.index(3) + 1) * 3
        return 0