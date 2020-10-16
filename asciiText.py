from bs4 import BeautifulSoup
import requests

Colors={
    "PURPLE" : '\033[95m',
    "BLUE" : '\033[94m',
    "CYAN" : '\033[36m',
    "GREEN" : '\033[92m',
    "YELLOW" : '\033[93m',
    "RED" : '\033[91m',
    "ENDC" : '\033[0m',
    "BOLD" : '\033[1m',
    "UNDERLINE" : '\033[4m',
    "All" : '\033[5;31;40m'
    }
colorsToUse = {0: '3-d', 2: '5lineoblique', 9: 'asc_____', 24: 'c_ascii_', 28: 'char2___', 36: 'charact6', 38: 'charset_',
               46: 'demo_1__', 56: 'f15_____', 67: 'fireing_', 115: 'npn_____', 122: 'panther_', 128: 'r2-d2___', 131: 'radical_',
               143: 'roman', 144: 'roman___', 145: 'script__', 175: 'twin_cob', 177: 'ucf_fan_', 189: 'acrobatic', 190: 'alligator',
               191: 'alligator2', 194: 'banner', 195: 'banner3-D', 196: 'banner3', 197: 'banner4', 198: 'barbwire', 199: 'basic', 200: '5x7',
               203: '6x9', 205: 'briteb', 210: 'clb6x10', 211: 'clb8x10', 212: 'clb8x8', 213: 'cli8x8', 221: 'clr7x10', 223: 'clr8x10',
               224: 'clr8x8', 245: 'utopiab', 260: 'xhelvbi', 267: 'xsbookb', 273: 'bell', 274: 'big', 277: 'block', 278: 'broadway',
               279: 'bubble', 281: 'calgphy2', 282: 'caligraphy', 285: 'coinstak', 286: 'colossal', 288: 'contrast', 289: 'cosmic', 292: 'cricket',
               300: 'doh', 302: 'dotmatrix', 313: 'epic', 316: 'fraktur', 320: 'graffiti', 324: 'isometric1', 325: 'isometric2', 326: 'isometric3',
               327: 'isometric4', 335: 'larry3d', 342: 'marquee', 351: 'nancyj-fancy', 356: 'nvscript', 371: 'rev', 378: 'sblood', 387: 'smisome1',
               397: 'starwars', 415: 'usaflag'
               }

def listFonts(exemple,text="TestText"):
    if exemple:
        for id in colorsToUse:
            print("ID : ",colorsToUse[id])
            print(getAscii(text,colorsToUse[id]))
    else:
        print(colorsToUse)

def getAscii(text="Text",font="broadway"):
        url = f'http://artii.herokuapp.com/make?text={text}&font={font}'
        data = requests.get(url)
        soup = BeautifulSoup(data.content, 'html.parser')
        print(soup)

def getAsciiColor(text="Text",font="broadway",color="cyan"):
    url = f'http://artii.herokuapp.com/make?text={text}&font={font}'
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    print(Colors[color.upper()]+soup.text+Colors["ENDC"])


print("\n\n")
getAsciiColor("JoeVenner","coinstak","green")



