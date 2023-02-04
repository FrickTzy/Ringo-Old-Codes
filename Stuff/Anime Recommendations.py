import random

Isekai = ['Re: Zero', 'Tensura', 'The Devil Is A Part Timer', 'Konosuba', 'Sword Art Online', 'Rising Of The Shield Hero', 'Beast Tamer']
Shonen = ['One Piece', 'Naruto', 'Bleach', 'Dragon Ball', 'Chainsaw Man', 'Hunter X Hunter']
Romcom = ["Komi Can't Communicate", 'Horimiya', 'Love Is War', 'Kaguya Sama: Love is war', 'Tomo-chan Wa Onna No Ko']
ShoRom = ['Chainsaw Man', 'Spy x Family', 'Kaguya Sama: Love is war']
ShoKai = ['Bleach', 'Hunter x Hunter', 'One Piece']
IseRom = ['Sword Art Online', 'The Devil Is A Part Timer', 'Konosuba']


IsePoints = 0
ShoPoints = 0
RCPoints = 0

print('Welcome to Anime Recommendations')
print('Type /help for the rules')
print(' ')

Genre = ''
while Genre != '/Quit':
    Genrez = input('What is your favorite Genre? ')
    Genre = Genrez.title()


    if Genre == '/Help':
        print('')
        print("Rules: ")
        print(" 1. You may do sentences ")
        print(" 2. Type /switch to switch language translation ")
        print(" 3. Type '/Quit' to Quit ")
        print(" ")
        continue

    if Genre == '/Quit':
        print('See you next time!')
        break

    Animez = input('What is your favorite Anime? ')
    Anime = Animez.title()
    he = Anime.split(',')

    if Anime == '/Quit':
        print('See you next time!')
        break

    if Genre == 'Shonen':
        ShoPoints += 1
    elif Genre == 'Romcom':
        RCPoints += 1
    elif Genre == 'Isekai':
        IsePoints += 1

    if Anime in Shonen:
        ShoPoints += 1
    elif Anime in Romcom:
        RCPoints += 1
    elif Anime in Isekai:
        IsePoints += 1

    if ShoPoints > RCPoints and ShoPoints > IsePoints:
        print(random.choice(Shonen))
        print('')
    elif ShoPoints < RCPoints and IsePoints < RCPoints:
        print(random.choice(Romcom))
        print('')
    elif ShoPoints == RCPoints and ShoPoints != 0:
        print(random.choice(ShoRom))
        print('')
    elif ShoPoints < IsePoints and RCPoints < IsePoints:
        print(random.choice(Isekai))
        print('')
    elif ShoPoints == IsePoints and ShoPoints != 0:
        print(random.choice(ShoKai))
        print('')
    elif RCPoints == IsePoints and RCPoints != 0:
        print(random.choice(IseRom))
        print('')
