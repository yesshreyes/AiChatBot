import urllib.request
import requests
from pydub import AudioSegment
from pydub.utils import which

AudioSegment.converter = which("ffmpeg")

import tempfile
import os
from pydub import AudioSegment
from pydub.playback import play


from pydub.playback import play
import calendar
import json
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
#import winshell
import pyjokes
#import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
#from clint.textui import progress
#from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import winsound
from translate import Translator
from tkinter import *

current_player = "x"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

engine1 = pyttsx3.init('sapi5')
voices1 = engine1.getProperty('voices')
engine1.setProperty('voice',voices1[0].id)


def diffvoice(audio):
    engine1.say(audio)
    engine1.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
password = "2003"
def wishMe():
    global password
    print("---------------------------------------------------------------------------------------------------")
    print(
        "|                                      𝐃𝐢𝐚𝐧𝐚 \U0001F464                                                    |")
    print("---------------------------------------------------------------------------------------------------")
    diffvoice("Password please")
    password1 = input("Password: ")
    if password1 == password:
        main()
    else:
        diffvoice("Access Denied.")
        password1 = input("Password: ")
        if password1 == password:
            main()
        else:
            diffvoice("Access Denied.")
            password1 = input("Password: ")
            if password1 == password:
                main()
            else:
                diffvoice("Access Denied.")
                diffvoice("I am sure you are not Mr.Shreyas.")
                diffvoice("Good Bye.")

def takeComand():
    #takes micro phone input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("𝐋𝐢𝐬𝐭𝐞𝐧𝐢𝐧𝐠\U0001F442...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)
    try:
        print("𝐑𝐞𝐜𝐨𝐠𝐧𝐢𝐳𝐢𝐧𝐠\U0001F9E0...")
        query = r.recognize_google(audio, language='en-in')
        print()
        print(f"User: {query}\n")
    except Exception as e:
        #print(e)
        print()
        print("Umm what?")
        print()
        return  "None"
    return query

def sendEmail(to,conent):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shrecr7@gmail.com','password')
    server.sendmail('shrecr7@gmail.com',to,conent)
    server.close()


def main():

    print()
    #wishMe()
    diffvoice("Access Granted.")
    diffvoice("Waking up Diana.")
    welc = AudioSegment.from_wav("glitch.wav")
    play(welc)
    well = AudioSegment.from_wav("welcome.wav")
    play(welc)
    msg = AudioSegment.from_wav("msg.wav")
    engine.setProperty('voice', voices[1].id)
    hour = int(datetime.datetime.now().hour)
    print()
    if hour >= 0 and hour < 12:
        speak("Good Morning Shreyas!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Shreyas!")
    else:
        speak("Good Evening Shreyas!")
    speak("How may i help you?")
    yes = True
    while yes == True:
        query = takeComand().lower()
        #logic for execuiting task
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            play(welc)
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(""" " """,results,""" " """)
            speak(results)
            print()

        elif "say hi to" in query:
            query = query.replace("say hi to", " ")
            next = "Hello" + query
            speak(next)

        elif 'open youtube' in query:
            play(welc)
            webbrowser.open("https://www.youtube.com/?gl=IN&tab=r1")
        elif 'open google' in query:
            play(welc)
            webbrowser.open("https://www.google.co.in/")
        elif 'play music' in query:
            '''
            music_dir = 'addresss'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            '''
            webbrowser.open("https://www.youtube.com/watch?v=etDblzZq_BU&list=PLpmRK7x5znBWc4XmO_dq2p4ytJ4O0TSgI&index=54")
        elif 'time' in query:
            play(welc)
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Shreyas, the time is {strTime}")
        elif 'open python' in query:
            play(welc)
            codepath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe"
            os.startfile(codepath)
        elif 'email to shreyas' in query:
            try:
                speak("What should I write sir?")
                content = takeComand()
                to = "shrecr7@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I wasn't able to sent this email.")
        elif 'quit' in query:
            play(welc)
            speak("Good Bye Shreyas. Nice talking to you.")
            yes = False
        elif "how are you" in query:
            speak("I am good. You tell me.")
        elif"bye diana" in query:
            play(welc)
            speak("Good Bye Shreyas. Nice talking to you.")
            yes = False
        elif "what is up" in query:
            speak("Nothing much bro. You say")
        elif 'tell me the date' in query:
            local_time = datetime.date.today()
            speak(local_time)
        elif 'joke' in query:
            speak("Ok here's a joke")
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
            print()

        elif 'what is your name' in query:
            speak("My name is Diana, and I was made by Shreyas")
        elif 'who are you' in query:
            speak("My name is Diana, and I was made by Shreyas")
        elif 'namaste' in query:
            speak("Namas te")

        elif 'who is' in query:
            query = query.replace("who is", " ")
            results = wikipedia.summary(query, sentences=2)
            play(welc)
            speak("According to wikipedia")
            print(""" " """,results,""" " """)
            speak(results)
            print()
        elif 'toss a coin' in query:
            speak("Sure!")
            coin = AudioSegment.from_wav("coin.wav")
            play(coin)
            hort = ["heads","tails"]
            resultt = random.choice(hort)
            speak(resultt)

        elif 'check internet' in query:
            play(msg)
            yay = True
            try:
                urllib.request.urlopen('http://google.com')  # Python 3.x
                yay = True
            except:
                yay = False
            if yay == True:
                speak("Connected")
            else:
                speak("No internet")

        elif 'what is' in query:
            query = query.replace("who is", " ")
            results = wikipedia.summary(query, sentences=2)
            play(welc)
            speak("According to wikipedia")
            print(""" " """,results,""" " """)
            speak(results)
            print()

        elif 'when is your birthday' in query:
            speak("Mr.Shreyas made me on 14 january 2021.")

        elif query == 'ok':
            speak("Yeah bye.")
            play(welc)
            yes = False

        elif query == 'diana':
            speak("Yes Shreyas?")

        elif 'bye' in query:
            speak("Good Bye Shreyas. Nice talking to you.")
            play(welc)
            yes = False

        elif 'do you know who am i' in query:
            speak("You are my creator. Shreyas Deshmukh")

        elif 'good' in query:
            speak("Thank you, it makes my day to hear that.")

        elif 'what are you doing' in query:
            speak("Nothing much. Just chilling.")

        elif 'tell me about yourself' in query:
            speak("Oh I am just a voice assistant. I was created by Shreyas to help you all.")

        elif 'thank you' in query:
            speak("oh come on. It's my duty. Ok then. Bye")
            play(welc)
            yes = False
        elif 'what all languages you speak' in query:
            speak("I can only speak english but I am trying to learn more languages")

        elif query == 'exit':
            speak("Good Bye Shreyas. Nice talking to you.")
            play(welc)
            yes = False
        elif "i love you" in query:
            speak("Ishsha. I am glad you love your virtual friend.")

        elif "hello" in query:
            speak("Hi")
            speak("How are you?")

        elif "write a note" in query:
            play(welc)
            speak("What should i write, sir")
            note = takeComand()
            file = open('diana.txt', 'a+')
            speak("Sir, Should i include date and time")
            snfm = takeComand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write("  :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            play(welc)
            try:
                speak("Showing Notes")
                file = open("diana.txt", "r")
                print(file.read())
                speak(file.read(6))
            except Exception as e:
                print(e)
                speak("sorry no note available. Please create one.")
        elif "clear note" in query:
            play(msg)
            os.remove("diana.txt")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query :
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            play(welc)
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")

        elif "don't listen" in query or "stop listening" in query or 'stop' in query or 'sleep' in query:
            speak("for how many seconds you want to stop diana from listening commands")
            a = int(takeComand())
            play(msg)
            time.sleep(a)
            print(a)
            speak("I am awake")
        elif "who am i" in query:
            speak("If you talk then definately your human.")

        elif "why are you here" in query:
            speak("Thanks to Shreyas. further It's a secret")

        # elif "calculate" in query:
        #     app_id = "Wolframalpha api id"
        #     client = wolframalpha.Client(app_id)
        #     indx = query.lower().split().index('calculate')
        #     query = query.split()[indx + 1:]
        #     res = client.query(' '.join(query))
        #     answer = next(res.results).text
        #     print("The answer is " + answer)
        #     speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Shreyas.")


        elif "wow" in query:
            speak("what happend!!!")

        elif "oh my god" in query:
            speak("what happend!!!")

        elif "full name"  in query:
            speak("My full name is Diana 1 point o the voice assistant")

        elif "cool" in query:
            speak("yep")

        elif "will you be my friend" in query:
            speak("I am your friend. Hehe")

        elif "what does the fox say" in query:
            speak("Fra kaa kaa kaa kaa kaa kaa kaa cow.")

        elif "knock knock" in query:
            speak("whose there")
            speak("your underwear.")

        elif "laugh" in query:
            speak("heee heee, ho ho ho ho ho, haa haa haa")


        elif "cry" in query:
            speak("momyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
            speak("hoo hoo hoo hoo hoo")

        elif "shout" in query:
            speak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhh")

        elif "beatbox" in query:
            speak("sure")
            bbx = AudioSegment.from_mp3("bbx.mp3")
            play(bbx)

        elif "repeat" in query or "repeat after me" in query:
            speak("ok")
            no = True
            while no == True:
                query = takeComand()
                if query == "stop":
                    speak("ok")
                    no = False
                speak(query)

        elif "get out" in query or "shut up" in query:
            speak("ugh")
            speak("ok, don't be so rude.")
            yes = False

        elif "call my mum" in query:
            speak("I, Eek day yay")

        elif "call my dad" in query:
            speak("baba, Eek day yaa")

        elif "speak hindi" in query:
            speak("nahee, moojhe hindi nahee aati")

        # elif "open notepad" in query:
        #     notepad = "E:\\SHRE.YESS\\SHREYAS DOCUMENT\\python\\NOTEPAD 2.0\\dist"
        #     os.startfile(notepad)

        elif "sing" in query:
            speak("I don't know how to sing yet. But hopefully I will one day")

        elif "make a list" in query:
            file1 = open('diana_list.txt', 'a+')
            speak("Sir, Should i include date and time")
            snfm = takeComand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file1.write(strTime)
            else:
                pass
            speak("What should i write, sir")
            kk= True
            while kk == True:
                note = takeComand()
                if  "done" in note:
                    kk = False
                    break
                else:
                    pass
                file1.write(" :- ")
                file1.write(note)
                speak("and")



        elif "show list" in query:
            try:
                speak("Showing List")
                file1 = open("diana_list.txt", "r")
                print(file1.read())
                speak(file1.read(6))
            except Exception as e:
                print(e)
                speak("sorry no list available. Please create one.")
        elif "clear list" in query:
            os.remove("diana_list.txt")

        elif "alarm" in query:
            speak("OK")
            speak("Hour: ")
            alarm_hour = int(takeComand())
            speak("Minutes: ")
            alarm_minutes = int(takeComand())
            speak("a m or p m? ")
            am_pm = takeComand()
            print(f"Waiting for time: {alarm_hour}:{alarm_minutes} {am_pm}")
            if am_pm == 'pm' or am_pm == 'p m':
                alarm_hour += 12
            elif alarm_hour == 12 and am_pm == 'am' or am_pm == 'a m' :
                alarm_hour -= 12
            else:
                pass
            while True:
                   if alarm_hour == datetime.datetime.now().hour and alarm_minutes == datetime.datetime.now().minute:
                        print("\nIt's the time!")
                        winsound.Beep(1000, 1000)
                        break

        elif "i hate you" in query:
            speak("Never ever use me again")

        elif "remember this" in query:
            speak("Yes tell me")
            file2 = open('diana_remember.txt', 'a+')
            remember = takeComand()
            strtimm = datetime.datetime.now().strftime("%H:%M:%S")
            file2.write(strtimm)
            file2.write("  :- ")
            file2.write(remember)

        elif "what did i tell you" in query:
            try:
                speak("You Told me that")
                file2 = open("diana_remember.txt", "r")
                print(file2.read())
                speak(file2.read(6))
                print()
            except Exception as e:
                print(e)
                speak("sorry you did not tell me anything")

        elif "rap" in query:
            speak("sure")
            rap = AudioSegment.from_mp3("rap.mp3")
            play(rap)



        elif "bark like a dog" in query:
            bark = AudioSegment.from_mp3("bark.mp3")
            play(bark)

        elif 'headlines' in query:
            news = AudioSegment.from_mp3("news.mp3")
            play(news)
            webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

        elif 'weather' in query:
            weather = AudioSegment.from_mp3("weather.mp3")
            play(weather)
            webbrowser.open("https://www.google.com/search?q=weather&rlz=1C1CHZN_enIN932IN932&oq=weather&aqs=chrome..69i57j35i39j0i67i131i395i433j0i67i395l2j0i67i395i457j0i67i395j0i67i395i433j0i67i395j0i395.2408j1j7&sourceid=chrome&ie=UTF-8")

        elif "translate" in query:
            speak("ok, Which language?")
            lang = takeComand()
            translator = Translator(to_lang=f"{lang}")
            speak("what do you want me to translate")
            msg = takeComand()
            translation = translator.translate(msg)
            print("TRANSLATION: ",translation)
            print()
            speak(translation)

        # elif "show games" in query:
        #     print("1.cross and zero\n2.Text Cricket\n3.Rock Paper Scissor\n4.Valorant\n5.Guess the Number\n6.Hangman\n7.Name Place Animal Thing")
        #
        # #TODO: Check if game over
        # elif "cross and zero" in query:
        #     tictac()
        # #TODO: Check if game over
        # elif "text cricket" in query:
        #     textcrick()
        #
        # elif "rock paper" in query:
        #     Rockpaper()
        # elif "valorant" in query:
        #     valo()
        # #elif "guess the number" in query:
        # #     guessnumber()
        #
        # elif "hangman" in query:
        #      hangman()
        # elif "name place" in query:
        #     nameplace()
        #
        # elif "calculation practice" in query:
        #     Calculation()
        #
        # elif "open notepad" in query:
        #     notepad()
        #
        # elif "calendar" in query:
        #     calender()
        #
        # elif "calculator" in query:
        #     calculator()
        #
        # elif "dice" in query:
        #     dice()

wishMe()


        # else:
        #     speak("Sorry I didn't get this. Should I google this?")
        #     ans = takeComand()
        #     if ans == "yes":
        #         results = wikipedia.summary(query, sentences=2)
        #         speak("According to wikipedia")
        #         print(""" " """, results, """ " """)
        #         speak(results)
        #     else:
        #         speak("Alright")


