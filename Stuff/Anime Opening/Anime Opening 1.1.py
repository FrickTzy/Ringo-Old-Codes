from pygame import mixer as m
import random

m.init()
Music = ["Assassination Classroom.mp3", "Tokyo Ghoul.mp3"]
MusicDic = {
    "Assassination Classroom.mp3": 'Assassination Classroom',
    "Tokyo Ghoul.mp3": 'Tokyo Ghoul',
}

he = 0
timesofplay = 1
score = 0

print("Welcome to Anime Opening Guessing Game!")
print("Guess The Anime in which the music came from")
while True:
    print('')
    heh = input("Type 'Start' to start the Game: ")
    hez = heh.lower()
    if hez == 'start':
        print(f"Opening {timesofplay}. ")
        pro = random.choice(Music)
        hep = MusicDic.get(pro, '')
        m.music.load(pro)
        m.music.play()
        print('')
        lol = input('What Anime is this opening from? ')
        lolz = lol.title()
        m.music.stop()
        if lolz == hep:
            print("Correct")
            score += 1
            timesofplay += 1
            print(f"Opening {timesofplay}. ")
            pro = random.choice(Music)
            hep = MusicDic.get(pro, '')
            m.music.load(pro)
            m.music.play()
            print('')
            lol.replace('', '')
            lol += input('What Anime is this opening from? ')
            m.music.stop()
        elif timesofplay == 3:
            print("Thanks for playing!")
            print(f"Your score is {score}")
            quit()
        else:
            print("Wrong")
            timesofplay += 1
            print(f"Opening {timesofplay}. ")
            pro = random.choice(Music)
            hep = MusicDic.get(pro, '')
            m.music.load(pro)
            m.music.play()
            print('')
            lol.replace('', '')
            lol += input('What Anime is this opening from? ')
    else:
        continue


