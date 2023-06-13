# Import the following module
import tkinter as tk  # install Tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image  # install pillow
from googletrans import Translator  # install googletrans==3.1.0a0 , newer versions may or may not work
from tkinter import messagebox
import pyperclip as pc # install paperclip for copy function
from gtts import gTTS  # install gTTS for text to speech, speech to text functionality
import os
import speech_recognition as spr # install speech recognition for speech to text functionality

# ---------------------------------------------------Language Translator--------------------------------------------------------------
''' This python file consist of all functionalities required for the language translator application to work  '''

# UI is developed using Tkinter library
root = tk.Tk()
root.title('Langauge Translator')
root.geometry('1060x660')
root.maxsize(1060, 660)
root.minsize(1060, 660)
# Tittle bar icon image used in Tkinter GUI
title_bar_icon = PhotoImage(file="resources/icons/translation.png")
root.iconphoto(False,title_bar_icon)
cl =''
output=''

# For Performing Main Translation Function
def translate():
    language_1 = t1.get("1.0", "end-1c")
    global cl
    cl = choose_langauge.get()

    if language_1 == '':
        messagebox.showerror('Language Translator', 'Please fill the Text Box for Translation')
    else:
         t2.delete(1.0, 'end')
         translator = Translator()
         global output
         output = translator.translate(language_1, dest=cl)
         output = output.text
         t2.insert('end', output)

# For Clearing Textbox Data
def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')

# For Copying Textbox Data after Translation
def copy():
    pc.copy(str(output))

# For Converting Translated Text to Speech
def texttospeech():
 global cl
 cl = choose_langauge.get()
 if os.path.exists("text_to_speech.mp3"):
  os.remove("text_to_speech.mp3")
 mytext =output
 language='en'
 if cl == 'English':
     language = 'en'
 elif cl == 'Afrikaans':
     language = 'af'
 elif cl == 'Albanian':
     language = 'sq'
 elif cl == 'Arabic':
     language = 'ar'
 elif cl == 'Armenian':
     language = 'hy'
 elif cl == 'Azerbaijani':
     language = 'az'
 elif cl == 'Basque':
     language = 'eu'
 elif cl == 'Belarusian':
     language = 'be'
 elif cl == 'Bengali':
     language = 'bn'
 elif cl == 'Bosnian':
     language = 'bs'
 elif cl == 'Bulgarian':
     language = 'bg'
 elif cl == 'Catalan':
     language = 'ca'
 elif cl == 'Cebuano':
     language = 'ceb'
 elif cl == 'Chinese':
     language = 'zh'
 elif cl == 'Corsican':
     language = 'co'
 elif cl == 'Croatian':
     language = 'hr'
 elif cl == 'Czech':
     language = 'cs'
 elif cl == 'Danish':
     language = 'da'
 elif cl == 'Dutch':
     language = 'nl'
 elif cl == 'English':
     language = 'en'
 elif cl == 'Esperanto':
     language = 'eo'
 elif cl == 'Estonian':
     language = 'et'
 elif cl == 'Finnish':
     language = 'fi'
 elif cl == 'French':
     language = 'fr'
 elif cl == 'Frisian':
     language = 'fy'
 elif cl == 'Galician':
     language = 'gl'
 elif cl == 'Georgian':
     language = 'ka'
 elif cl == 'German':
     language = 'de'
 elif cl == 'Greek':
     language = 'el'
 elif cl == 'Gujarati':
     language = 'gu'
 elif cl == 'Haitian Creole':
     language = 'ht'
 elif cl == 'Hausa':
     language = 'ha'
 elif cl == 'Hawaiian':
     language = 'haw'
 elif cl == 'Hebrew':
     language = 'he'
 elif cl == 'Hindi':
     language = 'hi'
 elif cl == 'Hmong':
     language = 'hmn'
 elif cl == 'Hungarian':
     language = 'hu'
 elif cl == 'Icelandic':
     language = 'is'
 elif cl == 'Igbo':
     language = 'ig'
 elif cl == 'Indonesian':
     language = 'id'
 elif cl == 'Irish':
     language = 'ga'
 elif cl == 'Italian':
     language = 'it'
 elif cl == 'Japanese':
     language = 'ja'
 elif cl == 'Javanese':
     language = 'jv'
 elif cl == 'Kannada':
     language = 'kn'
 elif cl == 'Kazakh':
     language = 'kk'
 elif cl == 'Khmer':
     language = 'km'
 elif cl == 'Kinyarwanda':
     language = 'rw'
 elif cl == 'Korean':
     language = 'ko'
 elif cl == 'Kurdish':
     language = 'ku'
 elif cl == 'Kyrgyz':
     language = 'ky'
 elif cl == 'Lao':
     language = 'lo'
 elif cl == 'Latin':
     language = 'la'
 elif cl == 'Latvian':
     language = 'lv'
 elif cl == 'Lithuanian':
     language = 'lt'
 elif cl == 'Luxembourgish':
     language = 'lb'
 elif cl == 'Macedonian':
     language = 'mk'
 elif cl == 'Malagasy':
     language = 'mg'
 elif cl == 'Malay':
     language = 'ms'
 elif cl == 'Malayalam':
     language = 'ml'
 elif cl == 'Maltese':
     language = 'mt'
 elif cl == 'Maori':
     language = 'mi'
 elif cl == 'Marathi':
     language = 'mr'
 elif cl == 'Mongolian':
     language = 'mn'
 elif cl == 'Myanmar':
     language = 'my'
 elif cl == 'Nepali':
     language = 'ne'
 elif cl == 'Norwegian':
     language = 'no'
 elif cl == 'Odia':
     language = 'or'
 elif cl == 'Pashto':
     language = 'ps'
 elif cl == 'Persian':
     language = 'fa'
 elif cl == 'Polish':
     language = 'pl'
 elif cl == 'Portuguese':
     language = 'pt'
 elif cl == 'Punjabi':
     language = 'pa'
 elif cl == 'Romanian':
     language = 'ro'
 elif cl == 'Russian':
     language = 'ru'
 elif cl == 'Samoan':
     language = 'sm'
 elif cl == 'Scots Gaelic':
     language = 'gd'
 elif cl == 'Serbian':
     language = 'sr'
 elif cl == 'Sesotho':
     language = 'st'
 elif cl == 'Shona':
     language = 'sn'
 elif cl == 'Sindhi':
     language = 'sd'
 elif cl == 'Sinhala':
     language = 'si'
 elif cl == 'Slovak':
     language = 'sk'
 elif cl == 'Slovenian':
     language = 'sl'
 elif cl == 'Somali':
     language = 'so'
 elif cl == 'Spanish':
     language = 'es'
 elif cl == 'Sundanese':
     language = 'su'
 elif cl == 'Swahili':
     language = 'sw'
 elif cl == 'Swedish':
     language = 'sv'
 elif cl == 'Tajik':
     language = 'tg'
 elif cl == 'Tamil':
     language = 'ta'
 elif cl == 'Tatar':
     language = 'tt'
 elif cl == 'Telugu':
     language = 'te'
 elif cl == 'Thai':
     language = 'th'
 elif cl == 'Turkish':
     language = 'tr'
 elif cl == 'Turkmen':
     language = 'tk'
 elif cl == 'Ukrainian':
     language = 'uk'
 elif cl == 'Urdu':
     language = 'ur'
 elif cl == 'Uyghur':
     language = 'ug'
 elif cl == 'Uzbek':
     language = 'uz'
 elif cl == 'Vietnamese':
     language = 'vi'
 elif cl == 'Welsh':
     language = 'cy'
 elif cl == 'Xhosa':
     language = 'xh'
 elif cl == 'Yiddish':
     language = 'yi'
 elif cl == 'Yoruba':
     language = 'yo'
 elif cl == 'Zulu':
     language = 'zu'
 else:
     language == 'en'
 try:
     myobj = gTTS(text=mytext, lang=language, slow=False)
     myobj.save("text_to_speech.mp3")
     os.system("text_to_speech.mp3")

 except ValueError as e:
     messagebox.showerror('Language Translator', cl+' is currently not supported for Read Aloud (Text to Speech)')
     print(f"An error occurred: {e}")
     # Handle the error or perform any necessary cleanup actions
 except AssertionError as e:
     # Handle the "No text to speak" error
     messagebox.showerror('Language Translator','Please enter the data to be translated before using Read Aloud')
     print("Error:", e)

# For converting Speech to Text [ Please Note : Only English is currently supported as from-language in Speech to Text Translation ]
def speechtotext():
   cl = choose_langauge.get()
   language = 'en'

   if cl == 'English':
       language = 'en'
   elif cl == 'Afrikaans':
       language = 'af'
   elif cl == 'Albanian':
       language = 'sq'
   elif cl == 'Arabic':
       language = 'ar'
   elif cl == 'Armenian':
       language = 'hy'
   elif cl == 'Azerbaijani':
       language = 'az'
   elif cl == 'Basque':
       language = 'eu'
   elif cl == 'Belarusian':
       language = 'be'
   elif cl == 'Bengali':
       language = 'bn'
   elif cl == 'Bosnian':
       language = 'bs'
   elif cl == 'Bulgarian':
       language = 'bg'
   elif cl == 'Catalan':
       language = 'ca'
   elif cl == 'Cebuano':
       language = 'ceb'
   elif cl == 'Chinese':
       language = 'zh'
   elif cl == 'Corsican':
       language = 'co'
   elif cl == 'Croatian':
       language = 'hr'
   elif cl == 'Czech':
       language = 'cs'
   elif cl == 'Danish':
       language = 'da'
   elif cl == 'Dutch':
       language = 'nl'
   elif cl == 'English':
       language = 'en'
   elif cl == 'Esperanto':
       language = 'eo'
   elif cl == 'Estonian':
       language = 'et'
   elif cl == 'Finnish':
       language = 'fi'
   elif cl == 'French':
       language = 'fr'
   elif cl == 'Frisian':
       language = 'fy'
   elif cl == 'Galician':
       language = 'gl'
   elif cl == 'Georgian':
       language = 'ka'
   elif cl == 'German':
       language = 'de'
   elif cl == 'Greek':
       language = 'el'
   elif cl == 'Gujarati':
       language = 'gu'
   elif cl == 'Haitian Creole':
       language = 'ht'
   elif cl == 'Hausa':
       language = 'ha'
   elif cl == 'Hawaiian':
       language = 'haw'
   elif cl == 'Hebrew':
       language = 'he'
   elif cl == 'Hindi':
       language = 'hi'
   elif cl == 'Hmong':
       language = 'hmn'
   elif cl == 'Hungarian':
       language = 'hu'
   elif cl == 'Icelandic':
       language = 'is'
   elif cl == 'Igbo':
       language = 'ig'
   elif cl == 'Indonesian':
       language = 'id'
   elif cl == 'Irish':
       language = 'ga'
   elif cl == 'Italian':
       language = 'it'
   elif cl == 'Japanese':
       language = 'ja'
   elif cl == 'Javanese':
       language = 'jv'
   elif cl == 'Kannada':
       language = 'kn'
   elif cl == 'Kazakh':
       language = 'kk'
   elif cl == 'Khmer':
       language = 'km'
   elif cl == 'Kinyarwanda':
       language = 'rw'
   elif cl == 'Korean':
       language = 'ko'
   elif cl == 'Kurdish':
       language = 'ku'
   elif cl == 'Kyrgyz':
       language = 'ky'
   elif cl == 'Lao':
       language = 'lo'
   elif cl == 'Latin':
       language = 'la'
   elif cl == 'Latvian':
       language = 'lv'
   elif cl == 'Lithuanian':
       language = 'lt'
   elif cl == 'Luxembourgish':
       language = 'lb'
   elif cl == 'Macedonian':
       language = 'mk'
   elif cl == 'Malagasy':
       language = 'mg'
   elif cl == 'Malay':
       language = 'ms'
   elif cl == 'Malayalam':
       language = 'ml'
   elif cl == 'Maltese':
       language = 'mt'
   elif cl == 'Maori':
       language = 'mi'
   elif cl == 'Marathi':
       language = 'mr'
   elif cl == 'Mongolian':
       language = 'mn'
   elif cl == 'Myanmar':
       language = 'my'
   elif cl == 'Nepali':
       language = 'ne'
   elif cl == 'Norwegian':
       language = 'no'
   elif cl == 'Odia':
       language = 'or'
   elif cl == 'Pashto':
       language = 'ps'
   elif cl == 'Persian':
       language = 'fa'
   elif cl == 'Polish':
       language = 'pl'
   elif cl == 'Portuguese':
       language = 'pt'
   elif cl == 'Punjabi':
       language = 'pa'
   elif cl == 'Romanian':
       language = 'ro'
   elif cl == 'Russian':
       language = 'ru'
   elif cl == 'Samoan':
       language = 'sm'
   elif cl == 'Scots Gaelic':
       language = 'gd'
   elif cl == 'Serbian':
       language = 'sr'
   elif cl == 'Sesotho':
       language = 'st'
   elif cl == 'Shona':
       language = 'sn'
   elif cl == 'Sindhi':
       language = 'sd'
   elif cl == 'Sinhala':
       language = 'si'
   elif cl == 'Slovak':
       language = 'sk'
   elif cl == 'Slovenian':
       language = 'sl'
   elif cl == 'Somali':
       language = 'so'
   elif cl == 'Spanish':
       language = 'es'
   elif cl == 'Sundanese':
       language = 'su'
   elif cl == 'Swahili':
       language = 'sw'
   elif cl == 'Swedish':
       language = 'sv'
   elif cl == 'Tajik':
       language = 'tg'
   elif cl == 'Tamil':
       language = 'ta'
   elif cl == 'Tatar':
       language = 'tt'
   elif cl == 'Telugu':
       language = 'te'
   elif cl == 'Thai':
       language = 'th'
   elif cl == 'Turkish':
       language = 'tr'
   elif cl == 'Turkmen':
       language = 'tk'
   elif cl == 'Ukrainian':
       language = 'uk'
   elif cl == 'Urdu':
       language = 'ur'
   elif cl == 'Uyghur':
       language = 'ug'
   elif cl == 'Uzbek':
       language = 'uz'
   elif cl == 'Vietnamese':
       language = 'vi'
   elif cl == 'Welsh':
       language = 'cy'
   elif cl == 'Xhosa':
       language = 'xh'
   elif cl == 'Yiddish':
       language = 'yi'
   elif cl == 'Yoruba':
       language = 'yo'
   elif cl == 'Zulu':
       language = 'zu'
   else:
       language == 'en'

   from_lang = "en"
   to_lang = language

   recog1 = spr.Recognizer()
   mc = spr.Microphone()

   with mc as source:

       recog1.adjust_for_ambient_noise(source, duration=0.9)
       audio = recog1.listen(source)
       get_sentence = recog1.recognize_google(audio)

   try:
       t1.insert("end",get_sentence + "\n")
       translator = Translator()
       text_to_translate = translator.translate(get_sentence, src=from_lang, dest=to_lang)
       text = text_to_translate.text

       speak = gTTS(text=text, lang=to_lang, slow=False)
       global output
       output = speak.text
       t2.insert("end",output + "\n")
       translate()

   except spr.UnknownValueError:
           t1.insert("Unable to Understand the Input")

   except spr.RequestError as e:
           t1.insert("Unable to provide Required Output".format(e))


# Background Image settings using Tkinter
img = ImageTk.PhotoImage(Image.open('translator.png'))
label = Label(image=img)
label.place(x=0, y=0)

# combobox for from-language selection
a = tk.StringVar()
auto_detect = ttk.Combobox(root, width=20,textvariable=a, state='readonly', font=('Corbel', 20, 'bold'), )

auto_detect['values'] = (
    'Auto Detect',
    'Afrikaans',
    'Albanian',
    'Arabic',
    'Armenian',
    'Azerbaijani',
    'Basque',
    'Belarusian',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    'Catalan',
    'Cebuano',
    'Chichewa',
    'Chinese',
    'Corsican',
    'Croatian',
    'Czech',
    'Danish',
    'Dutch',
    'English',
    'Esperanto',
    'Estonian',
    'Filipino',
    'Finnish',
    'French',
    'Frisian',
    'Galician',
    'Georgian',
    'German',
    'Greek',
    'Gujarati',
    'Haitian Creole',
    'Hausa',
    'Hawaiian',
    'Hebrew',
    'Hindi',
    'Hmong',
    'Hungarian',
    'Icelandic',
    'Igbo',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kannada',
    'Kazakh',
    'Khmer',
    'Kinyarwanda',
    'Korean',
    'Kurdish',
    'Kyrgyz',
    'Lao',
    'Latin',
    'Latvian',
    'Lithuanian',
    'Luxembourgish',
    'Macedonian',
    'Malagasy',
    'Malay',
    'Malayalam',
    'Maltese',
    'Maori',
    'Marathi',
    'Mongolian',
    'Myanmar',
    'Nepali',
    'Norwegian'
    'Odia',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Romanian',
    'Russian',
    'Samoan',
    'Scots Gaelic',
    'Serbian',
    'Sesotho',
    'Shona',
    'Sindhi',
    'Sinhala',
    'Slovak',
    'Slovenian',
    'Somali',
    'Spanish',
    'Sundanese',
    'Swahili',
    'Swedish',
    'Tajik',
    'Tamil',
    'Tatar',
    'Telugu',
    'Thai',
    'Turkish',
    'Turkmen',
    'Ukrainian',
    'Urdu',
    'Uyghur',
    'Uzbek',
    'Vietnamese',
    'Welsh',
    'Xhosa'
    'Yiddish',
    'Yoruba',
    'Zulu',
)

auto_detect.place(x=50, y=140)
auto_detect.current(0)
l = tk.StringVar()

# combobox for to-language selection
choose_langauge = ttk.Combobox(root, width=20, textvariable=l, state='readonly', font=('Corbel', 20, 'bold'))
choose_langauge['values'] = (
    'Afrikaans',
    'Albanian',
    'Arabic',
    'Armenian',
    'Azerbaijani',
    'Basque',
    'Belarusian',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    'Catalan',
    'Cebuano',
    'Chichewa',
    'Chinese',
    'Corsican',
    'Croatian',
    'Czech',
    'Danish',
    'Dutch',
    'English',
    'Esperanto',
    'Estonian',
    'Filipino',
    'Finnish',
    'French',
    'Frisian',
    'Galician',
    'Georgian',
    'German',
    'Greek',
    'Gujarati',
    'Haitian Creole',
    'Hausa',
    'Hawaiian',
    'Hebrew',
    'Hindi',
    'Hmong',
    'Hungarian',
    'Icelandic',
    'Igbo',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kannada',
    'Kazakh',
    'Khmer',
    'Kinyarwanda',
    'Korean',
    'Kurdish',
    'Kyrgyz',
    'Lao',
    'Latin',
    'Latvian',
    'Lithuanian',
    'Luxembourgish',
    'Macedonian',
    'Malagasy',
    'Malay',
    'Malayalam',
    'Maltese',
    'Maori',
    'Marathi',
    'Mongolian',
    'Myanmar',
    'Nepali',
    'Norwegian'
    'Odia',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Romanian',
    'Russian',
    'Samoan',
    'Scots Gaelic',
    'Serbian',
    'Sesotho',
    'Shona',
    'Sindhi',
    'Sinhala',
    'Slovak',
    'Slovenian',
    'Somali',
    'Spanish',
    'Sundanese',
    'Swahili',
    'Swedish',
    'Tajik',
    'Tamil',
    'Tatar',
    'Telugu',
    'Thai',
    'Turkish',
    'Turkmen',
    'Ukrainian',
    'Urdu',
    'Uyghur',
    'Uzbek',
    'Vietnamese',
    'Welsh',
    'Xhosa'
    'Yiddish',
    'Yoruba',
    'Zulu',
)

choose_langauge.place(x=600, y=140)
choose_langauge.current(0)

# Load and resize the icon images for buttons
translate_text_icon_img = Image.open("resources/icons/documents.png")
resized_translate_text_icon = translate_text_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
translate_text_icon = ImageTk.PhotoImage(resized_translate_text_icon)

clear_text_icon_img = Image.open("resources/icons/eraser.png")
resized_clear_text_icon = clear_text_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
clear_text_icon = ImageTk.PhotoImage(resized_clear_text_icon)

copy_text_icon_img = Image.open("resources/icons/copy.png")
resized_copy_text_icon = copy_text_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
copy_text_icon = ImageTk.PhotoImage(resized_copy_text_icon)

read_aloud_icon_img = Image.open("resources/icons/text_to_speech.png")
resized_read_aloud_icon = read_aloud_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
read_aloud_icon = ImageTk.PhotoImage(resized_read_aloud_icon)

voice_input_icon_img = Image.open("resources/icons/voice_recognition.png")
resized_voice_input_icon = voice_input_icon_img.resize((32, 32), Image.Resampling.LANCZOS)
voice_input_icon = ImageTk.PhotoImage(resized_voice_input_icon)


# Text Widget settings used in Tkinter GUI
t1 = Text(root, width=45, height=13, borderwidth=0, relief=RIDGE,font=('Calibri', 16))
t1.place(x=20, y=200)
t2 = Text(root, width=45, height=13, borderwidth=0, relief=RIDGE,font=('Calibri', 16))
t2.place(x=550, y=200)

# Button settings used in Tkinter GUI
translate_button = Button(root, text=" Translate Text ",image=translate_text_icon, compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
                command=translate,bg="#ffffff")
translate_button.place(x=40, y=565)

clear_button = Button(root, text=" Clear ",image=clear_text_icon, compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
               command=clear,bg="#ffffff")
clear_button.place(x=270, y=565)

copy_button = Button(root, text=" Copy ",image=copy_text_icon, compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
                command=copy,bg="#ffffff")
copy_button.place(x=485, y=565)

read_aloud = Button(root, text=" Read Aloud ",image=read_aloud_icon, compound="right" ,relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
                command=texttospeech,bg="#ffffff")
read_aloud.place(x=650, y=565)

voice_input = Button(root, text=" Voice Input ", image=voice_input_icon, compound="right", relief=RIDGE, borderwidth=0,
                     font=('Corbel', 20, 'bold'), cursor="hand2", command=speechtotext, bg="#ffffff")
voice_input.place(x=850, y=565)

root.mainloop()
