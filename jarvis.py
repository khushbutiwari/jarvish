import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import smtplib
import os

engine = pyttsx3.init('sapi5')# windows ek api deti  hai jo audio ko leti hai
voices=engine.getProperty('voices')
#print(voices[1].id) show two vioces male and female(1 and zero represt the vioce male vioce anf female voice)

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
        
    speak("i am jarivs sir.please tell me how mai i help u")
    
    
def takecommand(): #tell what function can done
      #it tale audio as input and give out put to user
    
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1#seconds before non-speaking audio to consider complte
        audio = r.listen(source) # audio sungega  sr ke through
    
    try:
         print("recognizing.....")   
         query=r.recognize_google(audio,language='en-in')# vioce ko recognize kare(ek audio microphone se le raha or use rturn kar rha hai)
         print(f"user said: {query}\n")
         
    except Exception as e:
        #print(e)
        
        print("say that again  please")
        return"none"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gamail.com',587)
    server.ehlo()
    server.starttls()
    server.login("khushbutiwari160@bbdu.ac.in",'your-password')  
    server.sendmail("email",to,content)
    server.close()
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
    
       #logic for executing task based on query
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query=query.replace('wkipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
    
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        # elif 'play music' in query:
            #music_dir=mpath of dir 
            #songs = os.listdir(music_dir)
            #print(songs)
            #os.startfile(os.path.join(music_dir,song[0]))"""
        
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is{strtime}")
            
    
        elif 'open code' in query:
            codepath="C:\\Users\\khush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif 'email to khushbu' in query:
            try:
                speak("what should i say")
                content=takecommand()
                to="khushbutiwari160@bbdu.ac.in"
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                speak("sorry i unable to send this email at this moment")   