from random import randint  # Built-in module used to generate random numbers

def fun1(n):

    def fun():
        print("fun")

    if n == 1:

        def fun():
            print("\n🎯 WELCOME TO THE NUMBER GUESSING GAME 🎯")
            print("--------------------------------------------------")
            print("I have selected a random number between 1 and 100.")
            print("Each player must try to guess the number.")
            print("The player who guesses the number in the fewest attempts wins.")
            print("--------------------------------------------------\n")

            # Take number of players
            total_players = int(input("Enter the number of players: "))
            print()

            # Store player names
            players = []

            for i in range(1, total_players + 1):
                name = input(f"Enter the name of Player {i}: ")
                players.append(name)

            # Dictionary to store player scores (number of attempts)
            scores = {}

            # Game starts for each player
            for player in players:
                print(f"\n{player}'s turn to play!")
                print("----------------------------")

                random_number = randint(1, 100)
                guess = -1
                attempts = 0

                while guess != random_number:
                    attempts += 1
                    guess = int(input("Guess a number between 1 and 100: "))

                    if guess > random_number:
                        print("The random number is smaller than your guess.\n")
                    elif guess < random_number:
                        print("The random number is greater than your guess.\n")

                print(f"Correct! The random number was {random_number}.")
                print(f"{player} guessed the number in {attempts} attempts.\n")

                scores[player] = attempts

            # Determine winner
            minimum_attempts = min(scores.values())

            winners = []

            for name, score in scores.items():
                if score == minimum_attempts:
                    winners.append(name)

            print("==============================================")

            if len(winners) == 1:
                print(f"🏆 {winners[0].upper()} WINS!")
                print(f"They guessed the number in {minimum_attempts} attempts.")
            else:
                print("🤝 It's a DRAW between:", ", ".join(winners))
                print(f"Each player guessed the number in {minimum_attempts} attempts.")

            print("==============================================")

            n1 = int(input(
                "If you want to play again, type 1. "
                "If you do not want to play, type 0: "
            ))

            return fun1(n1)

        return fun()

    else:
        return 0


n = int(input(
    "If you want to play the game, type 1. "
    "If you do not want to play, type 0: "
))

fun1(n)