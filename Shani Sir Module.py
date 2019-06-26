#THE SHANI SIR MODULE --- 12-B

reminder = "ALWAYS REMEMBER: THIS IS TO CELEBRATE THE LEGEND, NOT TO MOCK HIM."
print(reminder)

changelog = """The first version with a version number\n -Added NLP to our program. This makes the converter smarter
 -Added more voices to soundboard.
 -Fixed computer speaking word by word when his voice is not available! (also changed rate consequently!)
 -Slightly improved NLP"""

print("\nVersion 0.999 Beta")
print(f"Changelog: {changelog}")

#Full class 1 - https://1drv.ms/u/s!Aq6CKo0noHNiuEYPaIZD5mP90zGM
#Full class 2A - https://drive.google.com/open?id=1EO_woePO7WlxgnPbzBoVXGLbelekrPZR
#Full class 2B - https://drive.google.com/open?id=1pr834BjzA8g4iPpDnJar8XC0dfAIvhHC
#link to clips- https://drive.google.com/open?id=1ACR-zfYcIXVQa6G7lfn8k8bdv_L7wOrP (updated daily)
#Full link to good morning (1:09)- https://onedrive.live.com/?authkey=%21ALjEdhW122%5FJZso&cid=6273A0278D2A82AE&id=6273A0278D2A82AE%217239&parId=root&o=OneUp
#ALL NECCESARY MODULES MUST BE INSTALLED BEFORE RUNNING THIS SCRIPT - pyttsx3, playsound, TextBlob
#Also run in cmd: python -m textblob.download_corpora

import random as r
import pyttsx3
import tkinter
from playsound import playsound
from textblob import TextBlob

phrases = ["like you say", "like you speak", "like you do", "not to trouble you",
           "not troubling you", "okay, fine?", "decide a date", "it will be good for you",
           "it will be beneficial", "not hard,", "i don't want to talk like that", ",*draws perfect circle*", 
           "*scratches nose*", "*laughs*", "hahahahahaha", "tarjit", 
           "jokey", "so sowry", "embarrassing", "knocking",
           "it will be fruitful"] # 4 PER LINE ONLY PLEASE

actualvoice=["good mourning","so sowry","embarrassing",
             "like you say","knocking", "like this", "not clear", "water", "worksheet"]	#Make sure phrases, actualvoice, and file name have the same name or his voice won't play

#For converting normal text to shani text:
b_determiners=['like you say','like you speak','like you do']
adjectives=['like you say','it is not to trouble you',"not hard,"]
mood=["*laughs*", "hahahahahaha"]
neutral=["okay, fine?", "decide a date"]

#CLIPS
#ADJUST THE FOLLOWING CODE ACCORDING TO YOUR SYSTEM

location = "C:\\Users\\SAMIR.M_TMS\\Downloads\\Shanisirmodule-master\\Shanisirmodule-master\\clips"

def embarrassing():
    playsound('embarrassing.mp3') #make sure to put correct file path in your system before running

def like_you_say():
    playsound(f'{location}like you say.mp3')

def knocking():
    playsound(f'{location}knocking.mp3')

def so_sowry():
    playsound(f'{location}so sowry.mp3')
    
def good_mourning():
    playsound(f'{location}good mourning.mp3') #will be replaced when better quality is available.
    
def like_this():
    playsound(f'{location}like this.mp3')

def not_clear():
    playsound(f'{location}not clear.mp3')

def water():
    playsound(f'{location}water.mp3')

def worksheet():
    playsound(f'{location}worksheet.mp3')  

#TEXT TO SPEECH
#LEARN NATURAL LANGUAGE PROCESSING: http://www.nltk.org/book/ch00.html
#Also: https://textblob.readthedocs.io/en/dev/quickstart.html#create-a-textblob
#All parts of speech tags(POS)- https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

def shaniTTS(eng):

    """Takes a string and converts it to Shani Sir language, like you speak."""
    
#USING NATURAL LANGUAGE PROCESSING-

    blob=TextBlob(eng)

    cleaned=blob.words		#Returns list with no punctutation marks

    for word,tag in blob.tags:		#blob.tags is a list of pairs of tuples which tells the POS
        index=cleaned.index(word)

        if tag=='DT' and word=='a' or word=='this':
            cleaned.insert(index,r.choice(b_determiners))

        elif tag=='JJ':
            cleaned.insert(index+1,r.choice(adjectives))

        elif (blob.sentiment.polarity<0 and tag=='PRP'):			#sentiment tells if string is positive, neutral or negative
            if 'it is embarrassing to me like basically' not in cleaned:
                cleaned.append('it is embarrassing to me like basically')
            cleaned.insert(index+1,'so sorry')

        elif (blob.sentiment.polarity>0.5 and tag=='PRP'):
            cleaned.insert(index,r.choice(mood))

    #More parameters to come...
    cleaned.insert(0,'good morning')
    shanitext=' '.join(cleaned)

    #VOICE
    shanivoice = pyttsx3.init()
    rate = shanivoice.getProperty('rate')
    shanivoice.setProperty('rate',rate-58)
    
    temp=''
    
    for i in cleaned:
        if i in actualvoice:
            shanivoice.say(temp)
            shanivoice.runAndWait()
            playsound('C:\\Users\\aarti\\Downloads\\'+i+'.mp3')     #plays in his voice if present
            temp=''

        else:
            temp+=i+' '

    if temp!='':
        shanivoice.say(temp)
        shanivoice.runAndWait()

    return shanitext

#USER INTERFACES

#{"yellow" : "#FFFF00", "red" : "#E50000", "blue" : "#0C6FFF", "green" : "#58E900", "orange" : "#F38800", "black" : "#000000", "white" : "#FFFFFF"}
#For more colours, visit https://htmlcolorcodes.com/
colours = ["#FFFF00", "#E50000", "#0C6FFF", "#58E900", "#F38800"] #chucking black and white here

def toggleFullscreen(window):

    """Toggles fullscreen mode on and off using buttons"""

    if window.attributes("-fullscreen"):
        window.attributes("-fullscreen", False)
    else:
        window.attributes("-fullscreen", True)

def configureGrid(window, rows, columns):

    """Configures a window to appropriate size and divides it into a grid of rows and columns"""

    window.attributes("-fullscreen", True)

    #Gets the current screen resolution
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    window.geometry(f"{width}x{height}")
    
    for i in range(rows):
        window.rowconfigure(i, weight = 1)
    for j in range(columns):
        window.columnconfigure(j, weight = 1)



def returnConverted(window, entry):

    print(entry.get())
    converted = tkinter.Label(window, text = f"{shaniTTS(entry.get())}").grid(row = 4, column = 2)


def create_shaniUI():

    """The Shani Sir User Interface"""

    shaniUI = tkinter.Tk()
    configureGrid(shaniUI, 6, 6)
    shaniUI.title("shaniUI")

    #BUTTONS
    exitButton       = tkinter.Button(shaniUI, text = "EXIT", bg = "#000000", fg = "#FFFFFF", command = shaniUI.destroy).grid(row = 0, column = 5)
    fullscreenButton = tkinter.Button(shaniUI, text = "TOGGLE FULLSCREEN", bg = "#000000", fg = "#FFFFFF", command = lambda : toggleFullscreen(shaniUI)).grid(row = 0, column = 0)
    soundboardButton = tkinter.Button(shaniUI, text = "SOUNDBOARD", bg = r.choice(colours), command = create_soundboard).grid(row = 1, column = 0)
    shaniTTSButton   = tkinter.Button(shaniUI, text = "TEXT TO SPEECH", bg = r.choice(colours), command = shaniTTS).grid(row = 1, column = 5)
    label            = tkinter.Label(shaniUI, text = "What do you want to convert to Shani Sir language? ", bg = r.choice(colours)).grid(row = 1, column = 2)
    shaniTTSEntry    = tkinter.Entry(shaniUI)
    shaniTTSEntry.grid(row = 2, column = 2)
    takeInput        = tkinter.Button(shaniUI, text = "Convert", bg = "#000000", fg = "#FFFFFF", command = lambda : returnConverted(shaniUI, shaniTTSEntry)).grid(row = 3, column = 2)
    
def create_soundboard():

    """The Shani Sir Soundboard"""

    soundboard = tkinter.Tk()
    configureGrid(soundboard, 7, 7)
    soundboard.title("Soundboard")
    
    label = tkinter.Label(soundboard, text = "WELCOME TO THE SHANI SIR SOUNDBOARD!", bg = r.choice(colours)).grid(row = 0, column = 3)
    #Creates the "coming soon" labels
    for i in range(3, 7):
        for j in range(1, 6):
            labelo = tkinter.Label(soundboard, text = "COMING SOON", bg = r.choice(colours)).grid(row = i, column = j)
    
    #BUTTONS
    exitButton         = tkinter.Button(soundboard, text = "EXIT", bg = "#000000", fg = "#FFFFFF", command = soundboard.destroy).grid(row = 0, column = 6)
    fullscreenButton   = tkinter.Button(soundboard, text = "TOGGLE FULLSCREEN", bg = "#000000", fg = "#FFFFFF", command = lambda : toggleFullscreen(soundboard)).grid(row = 0, column = 0)
    embarrassingButton = tkinter.Button(soundboard, text = "Embarrassing", bg = r.choice(colours), command = embarrassing).grid(row = 1, column = 1)
    like_you_sayButton = tkinter.Button(soundboard, text = "Like you say", bg = r.choice(colours), command = like_you_say).grid(row = 1, column = 2)
    knockingButton     = tkinter.Button(soundboard, text = "KNOCKNKNOCKKNCOK", bg = r.choice(colours), command = knocking).grid(row = 1, column = 3)
    so_sowryButton     = tkinter.Button(soundboard, text = "Sowry", bg = r.choice(colours), command = so_sowry).grid(row = 1, column = 4)
    good_mourningButton= tkinter.Button(soundboard, text = "Good mourning", bg = r.choice(colours), command = good_mourning).grid(row = 1, column = 5)
    like_thisButton    = tkinter.Button(soundboard, text = "Like this", bg = r.choice(colours), command = like_this).grid(row = 2, column = 1)
    not_clearButton    = tkinter.Button(soundboard, text = "Not clear?", bg = r.choice(colours), command = not_clear).grid(row = 2, column = 2)
    waterButton        = tkinter.Button(soundboard, text = "Water", bg = r.choice(colours), command = water).grid(row = 2, column = 3)
    worksheetButton    = tkinter.Button(soundboard, text = "Worksheet", bg = r.choice(colours), command = worksheet).grid(row = 2, column = 4)
    
create_shaniUI()
