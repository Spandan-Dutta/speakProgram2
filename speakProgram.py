import pyttsx3
import os
import webbrowser
import speech_recognition as sr
pyttsx3.speak("Welcome to my tools,sir!!!! I hope you are healthy. What can I do for you?")
while True:
    print("Enter your choice: ", end=' ')
    #p = input()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        audio = r.listen(source)
        print("Completed")
    p = r.recognize_google(audio)
    if (("run" in p) or ("launch" in p) or ("execute" in p)) and (("chrome" in p) or ("browser" in p)):
        pyttsx3.speak("Opening chrome for you sir")
        os.system("chrome")
    elif ("run" in p  or ("launch" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
        pyttsx3.speak("Opening notepad for you sir")
        os.system("notepad")
    elif (("run" in p)  or ("launch" in p) or ("execute" in p)) and (("vlc" in p) or ("music" in p)):
        pyttsx3.speak("Opening vlc for you sir")
        os.system("vlc")
    elif (("run" in p)  or ("launch" in p) or ("execute" in p)) and (("media" in p) or ("player" in p)):
        pyttsx3.speak("Opening Windows Media Player for you sir")
        os.system("wmplayer")
    elif (("run" in p)  or ("launch" in p) or ("execute" in p)) and ("camera" in p):
        pyttsx3.speak("Opening camera for you sir")
        os.system("start microsoft.windows.camera:")
    elif (("run" in p)  or ("launch" in p) or ("execute" in p)) and ("calculator" in p):
        pyttsx3.speak("Opening calculator for you sir")
        os.system("start calculator:")
    elif (("run" in p)  or ("launch" in p) or ("execute" in p)) and (("gmail" in p) or ("mail" in p)):
        pyttsx3.speak("Opening gmail for you sir")
        webbrowser.open("https://www.gmail.com")
    elif (("run" in p)  or ("launch" in p) or ("execute" in p)) and (("whatsapp" in p) or ("web" in p)):
        pyttsx3.speak("Opening what's app for you sir")
        webbrowser.open("https://web.whatsapp.com/")
    elif (("run" in p)  or ("launch" in p) or ("execute" in p)) and (("youtube" in p) or ("entertainment" in p)):
        pyttsx3.speak("Opening youtube for you sir")
        webbrowser.open("https://www.youtube.com/")
    elif (("run" in p)  or ("launch" in p) or ("execute" in p)) and (("linkedin" in p) or ("feed" in p)):
        pyttsx3.speak("Opening your LinkedIn for you sir")
        webbrowser.open("https://www.linkedin.com/feed/")
    elif ("exit" in p) or ("quit" in  p):
        pyttsx3.speak("Signing off")
        break
    else:
        pyttsx3.speak("Wrong input")
