game_area = [
            ["*", "*", "*"],
            ["*", "*", "*"],
            ["*", "*", "*"]
            ]

def setup(game_area):
        print(game_area[0] + " | " + game_area[1] + " | " + game_area[2])
        print(game_area[3] + " | " + game_area[4] + " | " + game_area[5])
        print(game_area[6] + " | " + game_area[7] + " | " + game_area[8])

def user_input(game_area):
        place_area = int(input("Enter the place number"))
        if game_area[place_area - 1] != "*":
                print("Uh oh! That spot is already taken!")
                return user_input(game_area)
        else: 
                return place_area

main_player = "X"
def current_player():
        if main_player == "X":
                main_player = "O"
        else:
                main_player = "X"

champion = "n/a"
def winner(game_area):

        if game_area[0] == game_area[1] == game_area[2] != "*":
                champion = game_area[1]
                return True
        if game_area[3] == game_area[4] == game_area[5] != "*":
                champion = game_area[3]
                return True
        if game_area[6] == game_area[7] == game_area[8] != "*":
                champion = game_area[8]
                return True
        if game_area[0] == game_area[4] == game_area[8] != "*":
                champion = game_area[4]
                return True
        if game_area[2] == game_area[4] == game_area[6] != "*":
                champion = game_area[6]
                return True
        if game_area[0] == game_area[3] == game_area[6] != "*":
                champion = game_area[0]
                return True
        if game_area[1] == game_area[4] == game_area[7] != "*":
                champion = game_area[7]
                return True
        if game_area[2] == game_area[5] == game_area[8] != "*":
                champion = game_area[5]
                return True
        return False

def tie_check(game_area):
        if "*" not in game_area:
                print("get good lol")

def game_over(game_area)
        if winner(game_area):
                setup(game_area)
                print(champion, " is the victor!")


setup(game_area)
user_input(game_area)
current_player()
winner(game_area)
tie_check(game_area)
game_over(game_area)