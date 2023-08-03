import random

def play():
    user = input("Enter 'r' for rock ,'p' for paper and 's' for scissor. \n")
    computer = random.choice(['r','p','s'])
    print("AI :",computer)

    if user == computer:
        return "It's a tie."

    if is_win(user,computer):
        return "You win the game."

    return "You loss.Try again next time."

def is_win(player,opponent):

    #r>s , s>p , p>r return ture

    if (player =='r' and opponent == 's') or (player =='s' and opponent == 'p')  \
           or (player =='p' and opponent == 'r'):
            return True
print(play())