#https://www.analyticsvidhya.com/blog/2022/01/speech-to-text-conversion-in-python-a-step-by-step-tutorial/
#import library
import speech_recognition as sr

def transform(filename):
    #Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
    r = sr.Recognizer()
    # Reading Audio file as source
    #  listening  the  аudiо  file  аnd  stоre  in  аudiо_text  vаriаble
    with sr.AudioFile(filename) as source:
        audio_text = r.listen(source)
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            return text
        except:
            print('Sorry.. run again...')

    