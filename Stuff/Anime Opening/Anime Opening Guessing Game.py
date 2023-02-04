from pygame import mixer as m
import random

m.init()
Music = ["Assassination Classroom.mp3", "Tokyo Ghoul.mp3", "Hunter x Hunter.mp3", "Black Clover.mp3", "Black Clover 2.mp3",
         "Bleach.mp3", "Your Name.mp3", "Chainsaw Man.mp3", "One Piece.mp3", "Jujutsu Kaisen.mp3"]
MusicDic = {
    "Assassination Classroom.mp3": 'Assassination Classroom',
    "Tokyo Ghoul.mp3": 'Tokyo Ghoul',
    "Hunter x Hunter.mp3": 'Hunter X Hunter',
    "Black Clover.mp3": 'Black Clover',
    "Black Clover 2.mp3": 'Black Clover',
    "Bleach.mp3": 'Bleach',
    "Your Name.mp3": 'Your Name',
    "Chainsaw Man.mp3": 'Chainsaw Man',
    "One Piece.mp3": 'One Piece',
    "Jujutsu Kaisen.mp3": 'Jujutsu Kaisen'
}


def starting_screen():
    print("Welcome to Anime Opening Guessing Game!")
    print("Guess The Anime in which the music came from")
    while True:
        print('')
        heh = input("Type 'Start' to start the Game: ")
        hez = heh.lower()
        if hez == 'start':
            break
        else:
            continue


def music_play():
    timesofplay = 1
    score = 0
    while True:
        print(f"Opening {timesofplay}. ")
        pro = random.choice(Music)
        hep = MusicDic.get(pro, '')
        m.music.load(pro)
        m.music.play()
        rem = Music.index(pro)
        Music.pop(rem)
        print('')
        lol = input('What Anime is this opening from? ')
        lolz = lol.title()
        m.music.stop()
        if lolz == hep:
            print("Correct")
            score += 1
            timesofplay += 1
        else:
            print("Wrong")
            timesofplay += 1
        if timesofplay == 11:
            print("Thanks for playing!")
            print(f"Your score is {score}")
            quit()


starting_screen()
music_play()
