import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# use the microphone as source for input
with sr.Microphone() as source:
    print("Speak now. You have 10 seconds to speak.")
    audio = r.listen(source, phrase_time_limit=10)
 
# recognize the audio
try:
    text = r.recognize_google(audio)
    print("You said: " + text)

    # save the text to a file
    with open("output.txt", "w") as f:
        f.write(text)

except sr.UnknownValueError:
    print("Could not understand audio.")
except sr.RequestError as e:
    print("Error connecting to Google API: {0}".format(e))