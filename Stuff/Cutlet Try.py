import pykakasi


def hatranslator(x):
    z = x.split('ha')
    print(z)

def translate_jap():
    he = pykakasi.Kakasi()
    pro = he.convert('りんごを食べた')
    for item in pro:
        heh = ("{} ".format(item['hepburn'].capitalize()))
        return heh

hep = translate_jap()
hatranslator(hep)

