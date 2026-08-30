import random
def play_game():
     lucky_num = random.randint(1, 20)

     while True:
                     user_num = int(input("Guess the lucky num"))

                     if user_num == lucky_num:
                       print("you won.  game over!!")

                       break
                     elif user_num < lucky_num:
                             print("Too Low")

                     else: 
                             print("Too High")

                     print("thank you for playing.")

play_game()



                     
                     

             
