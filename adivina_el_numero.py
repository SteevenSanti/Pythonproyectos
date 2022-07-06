import random
def run():
    number_random = random.randint(1, 100)
    number_user = int(input("elige un número del 1 al 100: "))
    while number_random != number_user:
        if number_user < number_random:
            print("Ingresa un valor mayor: ")
        else: 
            print("Ingresa un valor menor: ")
        number_user = int(input())
    print("Adivinaste el número es: " + str(number_random))

    pass
if __name__ == "__main__":
    run()