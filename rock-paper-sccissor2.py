import random
print('Welcome to rock paper scceior game . Please Select the input upon your choice:')
print('1 is for Rock ✊') 
print('2 is for Paper 🤚')
print('3 is for Scissors ✌️')

while True:
    start = input(' do you want to start the game? (y/n)').lower()
    if start == 'y':
        player = int(input('You Choice: '))
        CPU = random.randint(1,3)
        print('CPU Choice: ', CPU)

        if player in range(1,4):
            if (player == 1 and CPU == 1) or (player == 2 and CPU == 2) or (player == 3 and CPU == 3):
                print('It is tie!')
            elif player == 1 and CPU == 3:
                print("You Won!")
            elif player == 2 and CPU == 1:
                print('You Won!')
            elif player == 3 and CPU == 2:
                print('You Won!')
            else:
                print('CPU Won')
        else:
            print('Invalid number please type from 1-3 ')
    elif start == 'n':
        print('Thanks for visiting')
        break
    else:
        print('Invalid input type y/n')

 