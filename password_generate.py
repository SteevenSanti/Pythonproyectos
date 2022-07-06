import random
def generate_password():
    mayus = ("A", "B", "C", "D", "E", "F", "G", "H", "I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    minus = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
    nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    chars = ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"')
    data = [mayus, minus, nums, chars]
    random_chart = ""
    number_random = ""
    range_of_password = 15
    for i in range(range_of_password):
        new_data = data[random.randint(0,(len(data)-1))]
        random_chart = new_data[random.randint(1,(len(new_data)-1))]
        number_random = number_random + random_chart
    return number_random
def run():
    password = generate_password()
    print("Tu nueva Contraseña es: " + str(password))
    pass

if __name__ == "__main__":
    run()