import random

game_area = [
            ["*", "*", "*"],
            ["*", "*", "*"],
            ["*", "*", "*"]
            ]



def setup(game_area):
  print(game_area[0][0] + " | " + game_area[0][1] + " | " + game_area[0][2])
  print(game_area[1][0] + " | " + game_area[1][1] + " | " + game_area[1][2])
  print(game_area[2][0] + " | " + game_area[2][1] + " | " + game_area[2][2] + "\n")

def user_input(game_area,main_player):
  if main_player == "O":
    number1 = int(input("Enter row number"))
    number2 = int(input("Enter column number"))
  #print(number1)
  #print(number2)
  #print(game_area[number1])
  #if number1 <= 2 and game_area[number1][number2] == "*": print("Adi")
  if(main_player == "O" and number1 <= 2 and game_area[number1][number2] == "*"): 
    if (main_player == "O" and number2 <= 2 and game_area[number1][number2] == "*"):
      game_area[number1][number2] = main_player
    else:
      print("That slot is taken! Please pick another slot.")
  
  
  

def current_player(main_player):
        #print("in current_player" + " " + main_player)
        if main_player == "X":
                main_player = "O"
                return(main_player)
                #print("in current_player after if" + " " + main_player)
                #print(main_player)
        else:
                #print("in current_player after else" + " " + main_player)
                main_player = "X"
                ai(game_area)
                #print(main_player)
                return(main_player)


def winner(game_area):
  if game_area[0][0] == game_area[0][1] and game_area[0][1] == game_area[0][2] and not game_area[0][0] == "*":
    champion = game_area[0][0]
    #print("in winner" + champion)
    return (champion)
  if game_area[1][0] == game_area[1][1] and game_area[1][1] == game_area[1][2] and not game_area[1][0] == "*":
    champion = game_area[1][0]
    return (champion)
  if game_area[2][0] == game_area[2][1] and game_area[2][1] == game_area[2][2] and not game_area[2][0] == "*":
    champion = game_area[2][0]
    return (champion)
  if game_area[0][0] == game_area [1][0] and game_area[1][0] == game_area[2][0] and not game_area[0][0] == "*":
    champion = game_area[0][0]
    return (champion)
  if game_area[0][1] == game_area[1][1] and game_area[1][1] == game_area[2][1] and not game_area[0][1] == "*":
    champion = game_area[0][1]
    return (champion)
  if game_area[0][2] == game_area[1][2] and game_area[1][2] == game_area[2][2] and not game_area[0][2] == "*":
    champion = game_area[0][2]
    return (champion)
  if game_area[0][0] == game_area[1][1] and game_area[1][1] == game_area[2][2] and not game_area[0][0] == "*":
    champion = game_area[0][0]
    return (champion)
  if game_area[0][2] == game_area[1][1] and game_area[1][1] == game_area[2][0] and not game_area[0][2] == "*":
    champion = game_area[0][2]
    return (champion)

  
  

def tie_check(game_area):
        if  game_area[0][0] != "*":
          if game_area[0][1] != "*":
            if game_area[0][2] != "*":
              if game_area[1][0] != "*":
                if game_area[1][1] != "*":
                  if game_area[1][2] != "*":
                    if game_area[2][0] != "*":
                      if game_area[2][1] != "*":
                        if game_area[2][2] != "*":
                          print("get good lol")
                          return("END")

def game_over(game_area):
        if winner(game_area):
                setup(game_area)
                print(champion, " is the victor!")

def ai(game_area):
  if main_player != "O":
    row_place = random.randint(0, 2)
    column_place = random.randint(0, 2)
    if game_area[row_place][column_place] != "*":
      ai(game_area)
      return
    game_area[row_place][column_place] = "X"
    current_player(main_player)
      
def main():
  global champion  
  champion = "n/a"
  global main_player  
  main_player = 'X'
  print(tie_check(game_area))
  while (winner(game_area) == None and tie_check(game_area) == None):
  #while (winner(game_area) == None):  
      
      #print("main" + main_player)
      setup(game_area)
      
      main_player = current_player(main_player)
      user_input(game_area,main_player)
      #print("main1")
      #print(main_player)
      ai(game_area)
      champion = winner(game_area)
      #print("out")
      #print(winner(game_area))
      #print(winner(game_area))
      #print(game_area)
      tie_check(game_area)
      #print(game_area[1][1])
      #setup(game_area)
      game_over(game_area)
      #main_player = "O"
       

main()