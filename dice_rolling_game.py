import random

while True:
    choice = input("Zar atmak ister misin? (e/h): ").lower()
    if choice == "e":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif choice == "h":
        print("Oynadığınız için teşekkürler!")
        break
    else:
        print("Geçersiz seçim!")
