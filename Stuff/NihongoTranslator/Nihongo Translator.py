import speech_recognition as sr
import pykakasi
import random
from pygame import mixer as m
from time import sleep

m.init()
Music = ["Black Catcher.mp3", "Departure.mp3"]
r = sr.Recognizer()

def translate_jap(x):
    he = pykakasi.Kakasi()
    pro = he.convert(x)
    for item in pro:
        hehz = ("{} ".format(item['hepburn'].lower()))
        return hehz

def voice():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print('listening...')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            return text


        except:
            heh = print('Please Try Again!')
            return heh

def hatranslator(x):
    z = x.split('は')
    return z

def wotranslator(x):
    z = x.split('を')
    return z

def haindex(x):
    y = x.split('ha')
    zoz = " ".join(y)
    prozwr = zoz.split("")
    n = prozwr.index('')
    zo = n + 1
    return zo


def space(x):
    y = x.split(' ')
    hepp = "".join(y)
    return hepp

def music_play():
    while True:
        pro = random.choice(Music)
        m.music.load(pro)
        m.music.play()
        sleep(10000)
        m.music.stop()


def voicej():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print('listening...')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='ja-JP')
            return text


        except:
            heh = print('Please Try Again!')
            return heh

def template(x, y):
    if a in dict.keys(x):
        y += x.get(a, '')
    if b in dict.keys(x):
        y += x.get(b, '')
    if c in dict.keys(x):
        y += x.get(c, '')
    if d in dict.keys(x):
        y += x.get(d, '')
    if e in dict.keys(x):
        y += x.get(e, '')
    if f in dict.keys(x):
        y += x.get(f, '')
    if g in dict.keys(x):
        y += x.get(g, '')
    if h in dict.keys(x):
        y += x.get(h, '')
    return y

def templatez(x, y):
    bro = ''
    if c in dict.keys(x):
        bro += x.get(c, '')
    if d in dict.keys(x):
        bro += x.get(c, '')
    if e in dict.keys(x):
        bro += x.get(c, '')
    if a in dict.keys(x):
        y += x.get(a, '')
    if b in dict.keys(x):
        y += x.get(b, '')
    if y != ""''"" and bro != ""''"":
        y += ' '
    if c in dict.keys(x):
        y += x.get(c, '')
    if d in dict.keys(x):
        y += x.get(d, '')
    if e in dict.keys(x):
        y += x.get(e, '')
    return y

def tempz(x, y):
    noun2 = ''
    pro = ''
    if c in dict.keys(x):
        pro += x.get(c, '')
    if d in dict.keys(x):
        pro += x.get(d, '')
    if e in dict.keys(x):
        pro += x.get(e, '')
    if a in dict.keys(x):
        y += x.get(a, '')
    if b in dict.keys(x):
        y += x.get(b, '')
    if y != ""''"" and pro != ""''"":
        if c in dict.keys(x):
            noun2 += x.get(c, '')
        if d in dict.keys(x):
            noun2 += x.get(d, '')
        if e in dict.keys(x):
            noun2 += x.get(e, '')
    return noun2

def tempzz(x, y):
    noun2 = ''
    y1 = ''
    if a in dict.keys(x):
        y += x.get(a, '')
    if b in dict.keys(x):
        y += x.get(b, '')
    if c in dict.keys(x):
        y1 += x.get(c, '')
    if d in dict.keys(x):
        y1 += x.get(d, '')
    if e in dict.keys(x):
        y1 += x.get(e, '')
    if y1 == ""''"":
        return y
    if y1 != ""''"":
        y += x.get(a, '')
        return y

nihongo_words = {
    'Foodz': {
        'Apple': 'ringo',
        'Chicken': 'tori-niku',
        'Fried Chicken': 'karaage',
        'Strawberry': 'ichigo',
        'Water': 'mizu',
        'Egg': 'tamago',
        'Vegetables': 'yasai',
    },
}

pro = random.choice(Music)
m.music.load(pro)
m.music.play()

print('Welcome to Nihongo Translator')
print('Type /help for the rules')
print(' ')
print('English to Japanese [Eng]')
Langz = input('or Japanese to English [Jap]: ')
Lang = Langz.lower()
print(' ')


if Lang == '/help':
    print("Rules: ")
    print(" 1. You may do sentences ")
    print(" 2. Type /switch to switch language translation ")
    print(" 3. Type '/quit' to quit ")
    print(" ")
    print('English to Japanese [Eng]')
    Langz.replace('', '')
    Lang.replace('', '')
    Langz = input('or Japanese to English [Jap]: ')
    print(' ')

Wordz = ' '
heh = ''
name = ''

Phrases = {
    'i love you': 'Aishiteiru',
    'good night': 'Oyasumi',
    'good grief': 'Yare Yare',
    'good luck': 'Ganbatte',
    'you are already dead': 'Omae wa mō shinde iru',
    'good morning': 'Ohayo Gozaimasu',
    'the world': 'Sekai',
    'my name is': 'Ore no namae wa',
    "can't communicate": 'Komyushou desu'
}

PhrasesJ = {
    'yare yare': 'Good Grief',
    'yare yare daze': 'Good Grief',
    'ai shite iru': 'I love You',
    'ai shite imasu': 'I love You',
    'ohayo gozaimasu': 'Good Morning',
    'za warudo': 'The World',
    'onna no ko': 'is a Girl',
    'ore no namae': 'My name is',
    'otoko no ko': 'is a Boy',
    'ore wa onna no ko': "I am a girl",
    'ohayougozaimasu': 'Good Morning'


}

Names = {
    'san': 'san',
    'sama': 'sama',
    'chan': 'chan',
    'kun': 'kun',
}

NamesToJap = {
    'mr.': '-san',
    'ms.': '-san',
}

NamesEng = {
    'mr.': 'mr.',
    'ms.': 'ms.'
}

NameDic = ['-san', '-sama', '-chan', '-kun']

Namez1 = {
    'ore': 'I am',
    'boku': 'I am',
    'watashi': 'I am',
    'washi': 'I am'
}

NamesEx = {
    'komi': 'komi',
    'kurt': 'kurt',
    'kuriko': 'kuriko',
}




while Wordz != '/quit':
    Word = input("What's the word? ")
    Wordz = Word.lower()
    if Lang == 'eng':
        if Wordz == '/voicerec':
            Wordz.replace('', '')
            heh = voice()
            Wordz = heh
            if heh is None:
                print('')
                continue
    if Lang == 'jap':
        if Wordz == '/voicerec':
            proz = ''
            Wordz.replace('', '')
            hexa = voicej()
            heh = space(hexa)
            zo = hatranslator(heh)
            zop = wotranslator(heh)
            if len(zo) > 1:
                try:
                    proz += translate_jap(zo[0])
                    proz += translate_jap(zo[1])
                except:
                    print(heh)
                    print(len(zo))
                    print(proz)
                    print(zo)
                    continue

            if len(zop) > 1:
                if len(zo) > 1:
                    try:
                        proz += translate_jap(zop[1])
                    except:
                        print(heh)
                        print(len(zo))
                        print(proz)
                        print(zo)
                        continue
                if len(zo) == 1:
                    try:
                        proz += translate_jap(zop[0])
                        proz += translate_jap(zop[1])
                    except:
                        print(heh)
                        print(len(zo))
                        print(proz)
                        print(zo)
                        continue

            print(heh)
            print(len(zo))
            print(proz)
            print(zo)
            Wordz = proz
            if Wordz in dict.keys(PhrasesJ):
                    heh = PhrasesJ.get(Wordz, '')
                    print(heh)
                    print('')
                    continue
            if heh is None:
                print('')
                continue

    if Wordz in dict.keys(PhrasesJ):
        if Lang == 'jap':
            heh = PhrasesJ.get(Wordz, '')
            print(heh)
            print('')
            continue

    if Wordz in dict.keys(Phrases):
        if Lang == 'eng':
            heh = Phrases.get(Wordz, '')
            print(heh)
            print('')
            continue

    try:
        hehez = Wordz.split(' wa ')
    except:
        continue
    phrases = ''
    phrases2 = ''
    integer = 0
    for n in hehez:
        if n in dict.keys(Phrases):
            if Lang == 'eng':
                heh = Phrases.get(n, '')
                integer += hehez.index(heh)
                phrases = heh
                heh.replace('', '')

        if n in dict.keys(PhrasesJ):
            if Lang == 'jap':
                heh = PhrasesJ.get(n, '')
                integer += hehez.index(n)
                if integer == 0:
                    phrases2 = heh
                if integer >= 1:
                    phrases = heh

    nam = Wordz.split()
    h = '-'.join(nam)
    pro = h.split('-')
    zo = ''
    Finalword = ''
    NameFin = ''
    NameFinal = ''
    NameC = ''
    for n in pro:
        if Lang == 'jap':
            if n in dict.keys(Names):
                zo = Names.get(n, '')
                wow = 0
                wow += pro.index(zo)
                n = wow - 1
                NameFin += pro[n]
                NameFinal += NameFin.title()

    EngName = ''
    PosEng = ''
    EngPhrases = ''
    PhrasesEng = ''
    Namez = ''
    for n in nam:
        if Lang == 'eng':
            if n in NamesToJap:
                EngName += NamesToJap.get(n, '')
                PosEng += NamesEng.get(n, '')
                woah = 0
                woah += nam.index(PosEng)
                hehew = woah + 1
                NameFin += nam[hehew]
                NameFinal += NameFin.title() + EngName
                nam.extend('')
                nam.extend('')
                PopIndex = nam.index(NameFin)
                if PopIndex <=1:
                    try:
                        EngPhrases += nam.pop(PopIndex + 1)
                        EngPhrases += ' '
                        EngPhrases += nam.pop(PopIndex + 1)
                        if EngPhrases in Phrases:
                            PhrasesEng = Phrases.get(EngPhrases, '')
                    except:
                        continue
                if PopIndex > 1:
                    try:
                        EngPhrases += nam.pop(PopIndex + 1)
                        EngPhrases += ' '
                        EngPhrases += nam.pop(PopIndex + 1)
                        if EngPhrases in Phrases:
                            PhrasesEng = Phrases.get(EngPhrases, '')
                    except:
                        continue

            if EngName != '-san':
                if n in NamesEx:
                    Namez += NamesEx.get(n, '')
                    NameFinal += Namez
                    NameFinal += '-san'
                    PopIndex = nam.index(Namez)
                    nam.extend('')
                    nam.extend('')
                    if PopIndex == 0:
                        try:
                            EngPhrases += nam.pop(PopIndex + 1)
                            EngPhrases += ' '
                            EngPhrases += nam.pop(PopIndex + 1)
                            if EngPhrases in Phrases:
                                PhrasesEng = Phrases.get(EngPhrases, '')
                        except:
                            continue
                    if PopIndex >= 1:
                        try:
                            EngPhrases += nam.pop(PopIndex - 1)
                            EngPhrases += ' '
                            EngPhrases += nam.pop(PopIndex - 1)
                            if EngPhrases in Phrases:
                                PhrasesEng = Phrases.get(EngPhrases, '')
                        except:
                            continue



    if phrases != ""''"":
        if NameFinal != ""''"":
            print(NameFinal + ' ' + phrases)
            print('')
            continue
    if phrases2 != ""''"":
        if NameFinal != ""''"":
            print(phrases2 + ' ' + NameFinal)
            print('')
            continue

    for n in hehez:
        if n in dict.keys(Namez1):
            NameC += Namez1.get(n, '')

    if NameC != ""''"":
        if NameFinal != ""''"":
            print(NameC + ' ' + NameFinal)
            print('')
            continue



    z = Wordz.split()
    z.append(' ')
    z.append(' ')
    z.append(' ')
    z.append(' ')
    z.append(' ')
    z.append(' ')
    z.append(' ')
    z.append(' ')
    a = z[0]
    b = z[1]
    c = z[2]
    d = z[3]
    e = z[4]
    f = z[5]
    g = z[6]
    h = z[7]

    Greetings = {
        'hi': 'Konnichiwa',
        'hello': 'Konnichiwa',
        'goodbye': 'Sayonara',
        'bye': 'Sayonara',
    }

    GreetingsE = {
        'konnichiwa': 'Hi',
        'sayonara': 'Goodbye',
        'ohayo': 'Good Morning',
        'ohayougozaimasu': 'Good Morning'
    }

    Others = {
        'name': 'Namae',
    }
    OthersJ = {
        'namae': 'Name',
    }

    Numbers = {
        'one': 'Ichi',
        'two': 'Ni',
        'three': 'San',
        'four': 'Yon',
        'five': 'Go',
        'six': 'Roku',
        'seven': 'Nana',
        'eight': 'Hachi',
        'nine': 'Kyu',
        'ten': 'Ju',
    }

    NumbersE = {
        'ichi': 'One',
        'ni': 'Two',
        'san': 'Three',
        'yon': 'Four',
        'go': 'Five',
        'roku': 'Six',
        'nana': 'Seven',
        'hachi': 'Eight',
        'kyu': 'Nine',
        'ju': 'Ten',
    }

    Food = {
        'apple': 'Ringo',
        'apples': 'Ringo',
        'chicken': 'Tori-Niku',
        'fried chicken': 'Karaage',
        'strawberry': 'Ichigo',
        'water': 'Mizu',
        'egg': 'Tamago',
        'vegetables': 'Yasai',
        'vegetable': 'Yasai',
        'eggs': 'Tamago',
    }

    Foodz = {
        'Apple': 'ringo',
        'Chicken': 'tori-niku',
        'Fried Chicken': 'karaage',
        'Strawberry': 'ichigo',
        'Water': 'mizu',
        'Egg': 'tamago',
        'Vegetables': 'yasai',
    }
    FoodEng = dict((v, k) for k, v in Foodz.items())

    Verb = {
        'ate': 'Tabeta',
        'eat': 'Taberu',
        'eating': 'Tabeteiru',
        'eaten': 'Tabeta',
        'drank': 'Nomita',
        'drink': 'Nomiru',
        'drinking': 'Nomiteiru',
    }

    VerbE = {
        'ate': 'tabeta',
        'eat': 'taberu',
        'eating': 'tabeteiru',
        'drank': 'nomita',
        'drink': 'nomiru',
        'drinking': 'nomiteiru',
    }
    VerbENG = dict((v, k) for k, v in VerbE.items())

    Filler = {
        'an': 'o'
        ''
    }

    FillerE = {
        'o': 'an',
        'wa': '',
        'ga': ''
    }

    Adjective = {
        'more': 'motto',
    }

    AdjectiveE = {
        'motto': 'more',
    }

    Request = {
        'please': 'Kudasai',

    }

    RequestE = {
        'kudasai': 'Please',
    }


    Noun = {
        'i': 'Ore wa',
        'you': 'kimi',
    }

    Noun2 = {
        'you': 'Kimi wa',
    }

    NounE = {
        'ore': 'I',
        'kimi': 'You',
        'anata': 'You',
        'kare': 'Him',
        'omae': 'You',
        'watashi': 'I'
    }

    Objects = {
        'books': 'Hon',
        'chairs': 'isu',
    }

    ObjectsE = {
        'hon': 'Books',
        'isu': 'Chairs',
    }

    Place = {
        'school': 'Gakkou',
        'house': 'Ie',
        'home': 'Ie',
    }

    PlaceE = {
        'gakkou': 'School',
        'ie': 'House',
    }

    Feelings = {
        'like': 'ga suki',
        'love': 'ga daisuki',
        'want': 'ga hoshii',
    }

    FeelingsE = {
        'suki': 'like',
        'daisuki': 'love',
        'aishiteimasu': 'I love You',
        'aishiteiru': 'I love You',
        'hoshii': 'want',
    }


    Quit = {
        '/quit': 'See you next time!',

    }

    food = ''
    if Lang == 'eng':
       food += template(Food, food)

    if Lang == 'jap':
        food += template(FoodEng, food)

    others = ''
    if Lang == 'eng':
        others += template(Others, others)

    if Lang == 'jap':
        others += template(OthersJ, others)

    verb = ''
    if Lang == 'eng':
        verb += template(Verb, verb)

    if Lang == 'jap':
        verb += template(VerbENG, verb)

    filler = ''
    if Lang == 'eng':
        filler += template(Filler, filler)

    if Lang == 'jap':
        filler += template(FillerE, filler)

    adjectives = ''
    if Lang == 'eng':
        adjectives += template(Adjective, adjectives)

    if Lang == 'jap':
        adjectives += template(AdjectiveE, adjectives)


    noun = ''
    if Lang == 'eng':
        noun += templatez(Noun, noun)

    noun2 = ''
    if Lang == 'jap':
        y = ''
        y1 = ''
        if a in dict.keys(NounE):
            y += NounE.get(a, '')
        if b in dict.keys(NounE):
            y += NounE.get(b, '')
        if c in dict.keys(NounE):
            y1 += NounE.get(c, '')
        if d in dict.keys(NounE):
            y1 += NounE.get(d, '')
        if e in dict.keys(NounE):
            y1 += NounE.get(e, '')
        if y1 == ""''"":
            noun += y
        if y1 != ""''"":
            noun += y
            noun2 += y1


    feeling = ''
    if Lang == 'eng':
        feeling = template(Feelings, feeling)

    if Lang == 'jap':
        feeling = template(FeelingsE, feeling)

    numbers = ''
    if Lang == 'eng':
        numbers += template(Numbers, numbers)

    if Lang == 'jap':
        numbers += template(NumbersE, numbers)

    greetings = ''
    if Lang == 'eng':
        greetings += template(Greetings, greetings)

    if Lang == 'jap':
        greetings += template(GreetingsE, greetings)

    quit = ''
    quit += template(Quit, quit)

    FillerWa = ''
    if Lang == 'eng':
        if NameFinal != ""''"":
            if greetings != ""''"" or noun != ""''"" or food != ""''"" or PhrasesEng != ""''"":
                FillerWa += 'wa'





    Total = ''
    if Lang == 'eng':
        if numbers != ""''"":
            Total += numbers
            Total += ' '
        if greetings != ""''"":
            Total += greetings
            Total += ' '
        if NameFinal != ""''"":
            Total += NameFinal
            Total += ' '
        if FillerWa != ""''"":
            Total += FillerWa
            Total += ' '
        if PhrasesEng != ""''"":
            Total += PhrasesEng
            Total += ' '
        if noun != ""''"":
            Total += noun
            Total += ' '
        if adjectives != ""''"":
            Total += adjectives
            Total += ' '
        if food != ""''"":
            Total += food
            Total += ' '
        if filler != ""''"":
            Total += filler
            Total += ' '
        if verb != ""''"":
            Total += verb
            Total += ' '
        if feeling != ""''"":
            Total += feeling
            Total += ' '
        if quit != "''":
            Total += quit
        if a == '/help':
            Total += ' '
        if a == '/switch':
            Total += ' '
        if Total == ""''"":
            print('The Word is Unknown')

    if Lang == 'jap':
        if numbers != ""''"":
            Total += numbers
            Total += ' '
        if phrases2 != ""''"":
            Total += phrases2
            Total += ' '
        if greetings != ""''"":
            Total += greetings
            Total += ' '
        if NameFinal != ""''"":
            Total += NameFinal
            Total += ' '
        if noun != ""''"":
            Total += noun
            Total += ' '
        if verb != ""''"":
            Total += verb
            Total += ' '
        if name != ""''"":
            Total += name
            Total += ' '
        if feeling != ""''"":
            Total += feeling
            Total += ' '
        if filler != ""''"":
            Total += filler
            Total += ' '
        if phrases != ""''"":
            Total += phrases
            Total += ' '
        if noun2 != ""''"":
            Total += noun2
            Total += ' '
        if adjectives != ""''"":
            Total += adjectives
            Total += ' '
        if food != ""''"":
            Total += food
            Total += ' '
        if quit != "''":
            Total += quit
        if a == '/help':
            Total += ' '
        if a == '/switch':
            Total += ' '
        if Total == ""''"":
            print('The Word is Unknown')

    print(Total)
    print(' ')


    if Wordz == '/help':
        print("Rules: ")
        print(" 1. You may do sentences ")
        print(" 2. Type /switch to switch language translation ")
        print(" 3. Type '/quit' to quit ")
        print(" ")

    if Wordz == '/switch':
        Langz.replace('', '')
        Lang.replace('', '')
        print('English to Japanese [Eng]')
        Lang = input('or Japanese to English [Jap]: ')
        print('')

    if Wordz == '/quit':
        m.music.stop()





