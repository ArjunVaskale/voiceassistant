import speech_recognition as sr 
import pyttsx3
import pywhatkit
from datetime import datetime
import wikipedia


listener = sr.Recognizer()

engine = pyttsx3.init() # object creation

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 165) 

voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[11].id)

for voice in voices:

  print("Gender: %s" % voice.gender)


engine.say("Hello Gajendra rathore")
engine.say('what can I do for you ?' )
engine.runAndWait()
engine.stop()


print('Hello Vini Assistant')




def take_command():
    try :
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey' in command:
                print(command)


    except:
        pass
    return command

def run_assist():
    command = take_command()
    if 'play' in command:
        command = command.replace('alexa' , '')
        command = command.replace('play'  , '')
        engine.say(command)
        engine.runAndWait()
        print('playing...' + command)
        pywhatkit.playonyt(command)
    elif 'time' in command:
            now = datetime.now()
            current_time = now.strftime("%I %M")
            print("Current Time =", current_time)
            engine.say('current time is ' + current_time)
            engine.runAndWait()
    elif 'search about' in command:
            command = command.replace('search about' ,'')
            print('searching...')
            command = wikipedia.summary(command, 2)
            print(command)
            engine.say('here is this what i found')
            engine.say(command)
            engine.runAndWait()

    
            

run_assist()