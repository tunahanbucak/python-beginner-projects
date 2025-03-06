import random

number = random.randint(1, 100)

while True:
    try:
        guess = int(input("1 ile 100 arasında bir sayı tahmin edin: "))

        if guess < number:
            print("Çok uzak!")
        elif guess > number:
            print("Çok yakın!")
        else:
            print("Tebrikler! Sayıyı bildiniz.")
            break
    except ValueError:
        print("Lütfen geçerli bir sayı girin")
