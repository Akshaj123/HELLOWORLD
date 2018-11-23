import pyttsx
from datetime import datetime
now = datetime.now()
year = now.year
engine = pyttsx.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
while True:
    speak("HELLO WHATS YOUR NAME?")
    name = raw_input("Hello,what's your name?\n")
    speak("Hello "+name)
    print("Hello "+name)

    if str(len(name)) == str(0):
        continue
    elif name.isdigit():
        speak("ohh your name contains numbers")
        print("ohh your name contains numbers\n")
        break
    elif name.isalpha():
        break
while True:
    speak("how old are you?")
    age = raw_input("how old are you?\n")
    if age.isdigit():
        break
    else:
        continue
while True:
    speak("Is your birthday in "+str(year)+" over,Type yes or no")
    over = raw_input("Is your birthday in "+str(year)+"over,Type yes or no\n")
    if over == "yes":
        born = year - int(age)
        break
    elif over == "no":
        born = year - int(age)-int(1)
        break
    else:
        continue
speak("your are born in the year "+str(born))
print("your are born in the year "+str(born)+"\n")




