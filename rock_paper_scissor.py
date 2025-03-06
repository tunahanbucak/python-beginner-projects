import random

TAŞ = "t"
MAKAS = "m"
KAĞIT = "k"
emojis = {TAŞ: "🪨", MAKAS: "✂️", KAĞIT: "📃"}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input("TAŞ, KAĞIT,  MAKAS? (t/k/m): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Geçersiz seçim")


def display_choices(user_choice, computer_choice):
    print(f"Senin seçimin {emojis[user_choice]}")
    print(f"Bilgisayarın seçimi {emojis[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Beraberlik!")
    elif (
        (user_choice == TAŞ and computer_choice == MAKAS)
        or (user_choice == MAKAS and computer_choice == KAĞIT)
        or (user_choice == KAĞIT and computer_choice == TAŞ)
    ):
        print("Kazandın")
    else:
        print("Kaybettin")


def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input("Devam etmek ister misiniz? (e/h): ").lower()
        if should_continue == "h":
            print("Teşekkürler")
            break


play_game()
