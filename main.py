from fractions import Fraction
import random

if __name__ == '__main__':

    # short version
    # P_A = Fraction(1, 3)
    # P_B = Fraction(1, 4)
    # P_B_A = Fraction(1, 5)
    #
    # P_A_B = P_B_A * P_A / P_B

    # long version

    a = random.randint(2, 5)
    b = random.randint(2, 5)
    print("Bayson riddle generator!")
    print("There are {a} chests in the dungeon".format(a=a))
    P_A = Fraction(1, a)
    P_B = 1 - Fraction(1, a)

    print("The master chest only contains gold")
    P_G_A = 1

    print("the skeleton chests contain {b} materials of which one is gold".format(b=b))
    P_G_B = Fraction(1, b)
    P_G = P_A * P_G_A + P_B * P_G_B
    P_A_G = P_A * P_G_A / P_G

    print("what is the chance the gold came from the master chest?")
    # print("bayes trainer")
    answer = Fraction(input(">"))
    review = P_A_G == answer
    print(f"Your answer is {review} the chance is {P_A_G}")
    print(f"    {P_A} * {P_G_A} ")
    print("------------------- ")
    print(f"{P_A} * {P_G_A} + {P_B} * {P_G_B}")