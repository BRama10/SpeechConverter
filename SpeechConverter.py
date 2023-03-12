import speech_recognition as sr
from deep_translator import GoogleTranslator
import random
import os
from gtts import gTTS
import time
from datetime import datetime
import os.path


if not(os.path.isfile('records.txt')):
    with open("records.txt", "w+") as file:
        temp_var = 'DUMMY'+'CONDITION'


r = sr.Recognizer()
now = datetime.now()

now_str = now.strftime("%m/%d/%Y %H:%M:%S")

def record_audio(microphone=None):
    with microphone as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Audio Starting ........")
        print("Start Speaking Now")
        audio = r.listen(source)
        for x in range(0, random.randint(2, 100)):
            print('........')
        print("Speaking Time Ended")
    return audio


def speech_to_text(speech, engine = 'google+standard', alternate=False):
    if(engine == 'google+standard'):
        return r.recognize_google(speech, show_all=False)
    elif(engine == 'wit.ai+standard'):
        if not alternate:
            return r.recognize_wit(audio_data=speech, show_all=False, key='WSZRTAK5LBEEXNFPXZYBDY5V7Z7KXECN')
        else:
            return r.recognize_wit(audio_data=speech, show_all=True, key='WSZRTAK5LBEEXNFPXZYBDY5V7Z7KXECN')

def translate_text(pre=None, text=None):
    return GoogleTranslator(source='auto', target=pre).translate(text)


print("####################################################################################")
time.sleep(2)
print("DYNAMIC SPEECH TO SPEECH LANGUAGE TRANSLATION TOOL")
print("Author : Balaji Rama")
time.sleep(2)
#printc("For detailed instructions on how to use, see the docs")
print('\n \n')
print('Choose [m] if you want to record message directly using your computer\'s microphone or choose [r] if you already have a recorded clip you want converted')
print('Alternatively, you can also choose [t] if you want to directly type in text to be converted & spoken')
print('\n')

input_type = input('Choice:')

if input_type == 'm':
    valid = 'n'

    print('\n \n'+'By default, the computer will use your default microphone for this program.')
    time.sleep(1)
    print("If you wish to change the microphone, you can do one of two things - \n"+"1. Manually change the default microphone from your computer settings. \n"+"2. Choose the microphone name directly in the program.")
    time.sleep(2.5)
    print("In terms of complexity, both are relatively easy, but Option 2 requires you to know the exact name of the microphone (which can sometimes be tricky since multiple mics can have really similar names).")
    #print("Meanwhile if you are using Option 1, you'll need to restart the program to apply the changes")
    time.sleep(3)
    print("If you are fine with your default microphone (this is probably what you use everywhere so don't sweat it too much) then enter [d]. If you are going with Option 2, then enter [2]. Finally if you are going with Option 1, then simply restart the program then continue with the default step.")
    print('\n \n')
    choice_mic = input('Choice: ')
    print('\n \n')
    
    if choice_mic == 'd':
        mic = sr.Microphone()
    else:
        mic_vals = sr.Microphone.list_microphone_names()
        #print(mic_vals)
        for x,y in enumerate(mic_vals):
            print('[' + str(x) + ']' + '  :  ' + y)

        time.sleep(0.8)
        mic_num = input("\n"+"Enter the number that exactly corresponds with your desired microphone \n \n"+"Choice: ")

        mic = sr.Microphone(device_index=int(mic_num))
    


    while not(valid == 'y' or valid == 'Y'):
        captured_audio = record_audio(microphone = mic)    

        actual_text = speech_to_text(speech = captured_audio, engine = 'wit.ai+standard')

        for x in range(4):
            print(' ')


        print("TEXT:", actual_text)

        for x in range(4):
            print(' ')


        print("Is this an accurate representation of your words? Enter [y] for Yes & [n] for No.")
        time.sleep(1)
        print("If no, you'll be asked to rerecord your message, you can keep doing this infinitely, but obviously some words the computer will not be able to understand. I honestly suggest you try 3 or 4 times using the tips given at the starting, if the message isn't coming, then you'll need to rephrase / use synonyms / try using the manual text option.")
        time.sleep(1)
              
        valid = input('\n'+'Choice:')
elif input_type == 'r':
    print("Follow the following steps (repetitive smh).")
    time.sleep(1)
    print('YOU ARE using recorded clip, so make sure it is in the compressed WAV format, you can easily convert mp4/mp3 to WAV online if clip isn\'t in desired format.')
    time.sleep(1)
    print('Otherwise the program won\'t work and I\'m too lazy to create a video converter at the moment unfortunately.')
    time.sleep(1)
    print("A great site is https:\\cloudconvert.com/mp4-to-wav for mp4 and https:\\cloudconvert.com/mp3-to-wav for mp3.")
    time.sleep(1)
    print("There is also a dynamic file type changer on the first website so you don't need to keep switching URL's.")
    time.sleep(1)
    print("Move the recording (clip) file into the SpeechConverter folder, HOPEFULLY YOU KNOW HOW TO DO THIS!!!!!")
    time.sleep(1)

    valid = 'n'

    while not(valid == 'y' or valid == 'Y'):
    
        file_name = input("\n \n"+"What is the name of the file, for example harvard.wav or ihavenobrains.wav \n"+"File Name:")
        audio_file = sr.AudioFile(file_name)
    
        with audio_file as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            captured_audio = r.record(source)

        print("<=========================CONSOLE OUTPUT=========================>")
        actual_text = speech_to_text(speech = captured_audio, engine = 'google+standard')
        print("<=========================CONSOLE END=========================>")
        
        for x in range(4):
            print(' ')


        print("TEXT:", actual_text)

        for x in range(4):
            print(' ')


        print("Is this an accurate representation of your words? Enter [y] for Yes & [n] for No.")
        print("If no, then you should rerecord, resave the file, ensure the correct file types, etc.....and then reenter the file name. I honestly suggest you try 3 or 4 times using the tips given at the starting, if the message isn't coming, then you'll need to rephrase / use synonyms / try using the manual text option")
        valid = input('\n'+'Choice:')
elif input_type == 't':
    print('Enter your desired text below :) \n \n')
    actual_text = input('Start Typing:')


with open("records.txt", "a") as file:
    file.write('\n'+'###############################################################')
    file.write('\n'+'Time => '+ now_str)
    file.write('\n'+'Text (English) => '+ actual_text)

print("<=========================TRANSLATION=========================>")
print("<==================================================>")

list_of_langs = list(enumerate([('German', 'de'), ('Spanish', 'es'), ('French', 'fr'), ('Simplified Chinese', 'zh-CN'), ('Traditional Chinese', 'zh-TW'), ('Japanese', 'ja'), ('Korean', 'ko'), ('Arabic', 'ar'), ('Hebrew', 'iw'), ('Hindi', 'hi'), ('Urdu', 'ur')]))

for x,y in list_of_langs:
    print('[' + str(x) + ']' + '  :  ' + y[0])

print('\n')

choice = int(input("Choose the language you want translated to. Make sure you use the exact number choice corresponding to the language of your choice.\n"+"For example, if you want to choose German, then enter 0 \n \n"+"Choice:"))

print('\n')

list_of_langs_dict = dict(list_of_langs)

prefix = list_of_langs_dict.get(choice)[1]

translated_text = translate_text(pre=prefix, text=actual_text)

print("<=========================TRANSLATING========================>")
for x in range(random.randint(0, 100)):
    print('.......')

for x in range(random.randint(0, 4)):
    print(' ')

print("TRANSLATED TEXT:", translated_text.encode('utf-8').decode('utf-8'))

with open("records.txt", "a") as file:
    file.write('\n'+'Translated Text => ')

with open("records.txt", "ab") as file:
    file.write(translated_text.encode('utf-8'))

print("\n NOTE : If translating to an Oriental-based language (Chinese, Japanese, etc), characters won't be rendered. Audio will still work as functioned.")

for x in range(random.randint(0, 4)):
    print(' ')

print('Program is paused in order to let you grasp the magic ^_^ will convert to audio within next 10 seconds. \n')
time.sleep(10)

print("<=========================TEXT TO SPEECH=========================>")
print("<==================================================>")

print('\n')

special, domain = False, None

if prefix == 'es':
    print('[0]  : ' + ' Spanish ( United States Accent )')
    print('[1]  : ' + ' Spanish ( Mexican Accent )')
    print('[2]  : ' + ' Spanish ( Spanish Accent )')
    special = True
elif prefix == 'fr':
    print('[0]  : ' + ' French ( Canadian Accent )')
    print('[1]  : ' + ' French ( French Accent )')
    special = True

if special:
    accent = int(input('Choose the specific accent you would like, remember to use specific numbers. \n'+'Choice:'))
    if prefix == 'es':
        if accent == 0:
            domain = 'com'
        elif accent == 1:
            domain = 'com.mx'
        elif accent == 2:
            domain = 'es'
    else:
        if accent == 0:
            domain = 'ca'
        elif accent == 1:
            domain = 'fr'
    

for x in range(random.randint(0, 50)):
    print('Converting.......')

print('before obj creation')
if domain is None:
    speechObj = gTTS(text=translated_text, lang=prefix)
else:
    speechObj = gTTS(text=translated_text, lang=prefix, tld=domain)
print('after obj creation')
time.sleep(0.3)
print('\n \n')
filename = input('Enter a filename for saving your audio file \n'+'\n'+'File Name:')

speechObj.save(filename+'.mp3')

print("Converted & Saved........Will begin playback in a few moments")

with open("records.txt", "a") as file:
    file.write('\n'+'Audio File Name => '+ filename+'.mp3')

os.system(filename+'.mp3')

time.sleep(3)
exit()






