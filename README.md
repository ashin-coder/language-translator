<h1 align="center" id="title">Language Translator</h1>

![tittle_img](https://github.com/ashin-coder/language-translator/assets/73836674/04a6874c-adf6-4ba1-9030-83253d386e8f)

The Language Translator project is a versatile tool designed to empower seamless communication across more than 100 languages. Utilizing the power of Python, our project allows you to effortlessly translate text in real-time, breaking down language barriers and fostering effective global interactions. With its intelligent auto-detect function, the project can instantly recognize the language of the input text, eliminating the need for manual identification. Once the source language is determined, you have the freedom to select your desired target language from our extensive database. However, I have enabled features which extend beyond just text translation. my project offers additional features such as text-to-speech functionality, enabling you to hear the translated text. Furthermore, I have added support for speech-to-text conversion from English to the chosen language, providing a convenient and efficient method for translation. The translated text can be easily copied for use in any application or platform, allowing you to seamlessly integrate it into your desired context. Also enabled the option for users to easily remove any previous translations or input from the text box. This way, you can start fresh without any clutter, making it easier for you to work on your next translation or enter new text.

## Installation

1. Clone the repository: git clone https://github.com/ashin-coder/language-translator.git
2. Install Python (version 3.10 or Other Versions may work depending on compatibility) from the official website: Python
3. Install a Python IDE preferably PyCharm to prevent any kind of incompatibilities since this project was developed in PyCharm
4. Install the required dependencies using pip: pip install "dependency name" ( check the imports in the code)
5. Run the Application from the main.py file in the IDE

**Please Note**: As Mentioned before this installation is based on "PyCharm" IDE as it was developed in the same, Project may or may not work as expected in Other IDEs, also an Internet Connection is required for the libraries used in the application to function

## Features

1. Translate Text : Translate Data spanning over 100 languages.
2. Read Aloud : Text-to-Speech functionality allows users to hear the translated text in the desired language.
3. Voice Input : Speech-to-Text capability for conveniently inputting text through voice for translation.
4. Copy : Allow to quickly and easily save the translated text to the clipboard.
5. Clear : Allow to easily clear the text box, removing any previous translations or input.
5. A user-friendly Graphical User Interface (GUI) for seamless and intuitive usage.

## Implementation

The Language Translator project is a versatile tool developed using Python, aimed at facilitating seamless communication across more than 100 languages. It leverages the power of various libraries and APIs to provide a user-friendly and efficient translation experience. The core functionality of the project revolves around translating text from one language to another. By utilizing the Google Translate API through the `googletrans` library, the project enables users to effortlessly translate text in real time. The intelligent auto-detect function automatically identifies the language of the input text, eliminating the need for manual identification. This feature greatly simplifies the translation process, allowing users to quickly and accurately convert text from any language into their desired target language.

In addition to translation, the project incorporates several extra features to enhance the overall user experience. One of these features is the Read Aloud which is text-to-speech functionality, powered by the `gTTS` library. This functionality allows users to listen to the translated text, providing an additional layer of comprehension and accessibility. By converting the translated text into an audio file, the project enables users to hear the pronunciation and intonation of the translated content. The audio file is saved as an external file named “text_to_speech.mp3” in the project folder which is played by the default media player in the computer. This file gets replaced with a new one each time the Read Aloud functionality is used to hear audio of newer translations

Another notable feature of the Language Translator project is its support for speech-to-text conversion from English to the chosen target language, this feature is named Voice Input in the Project. By utilizing the `speech_recognition` library, the project allows users to speak in English and have their speech automatically converted into text in the target language. This feature provides a convenient and efficient method for translation, particularly for users who may prefer speaking over typing. As mentioned before, an internet connection is required for the libraries used in the project to function

To ensure seamless integration of the translated text into various applications and platforms, the project includes a copy function. By utilizing the `pyperclip` library, users can easily copy the translated text to their clipboard and paste it into any desired context without any additional steps. This feature enhances the versatility and flexibility of the project, enabling users to utilize the translated content in emails, documents, chat applications, and more.

The Project also offers a convenient method that allows you to swiftly clear any previous translations or input from the text box. By utilizing this feature, you can effortlessly start anew without any lingering content, ensuring a streamlined and uncluttered environment for your subsequent translation or text entry. This functionality enhances usability by promoting a clean and organized workflow.

The graphical user interface (GUI) of the project is implemented using the `tkinter` library, offering a user-friendly and intuitive interface for interacting with the translation tool. The GUI includes options for selecting the source language, choosing the target language, inputting text to be translated, and initiating the translation process using the Translate Text button. It also provides buttons for Read Aloud (text-to-speech conversion), Voice Input (speech-to-text conversion), Copy (copying the translated text) and Clear (removing any previous translations or input) functions. 

## Project Screenshots

* Translate Text
![text_translate](https://github.com/ashin-coder/language-translator/assets/73836674/bd609942-9381-444a-912f-9c3183a33727)

* Copy
![copy_1](https://github.com/ashin-coder/language-translator/assets/73836674/600ff069-707e-4e98-a9fb-cca3edb5ffa7)
![copy_2](https://github.com/ashin-coder/language-translator/assets/73836674/5722d2b1-7d88-4970-b27e-8c67cf76d616)

* Read Aloud
![read_aloud](https://github.com/ashin-coder/language-translator/assets/73836674/ca3ee180-f9bc-4f18-b740-770709da3868)

* Voice Input
![voice_input](https://github.com/ashin-coder/language-translator/assets/73836674/a1d9ddfc-477c-4946-a37a-19dfd32d9b76)

* Clear
![clear](https://github.com/ashin-coder/language-translator/assets/73836674/28b035b4-c624-4823-a49f-e44f3ec9cbac)

## Acknowledgments

I would like to thank the developers and contributors of Python, as well as the libraries and frameworks used in this project, for providing the tools and resources and also those who provided the knowledge and support to make this Language Translator project possible. The icons used in this project were sourced from Flaticon, a platform for high-quality icons. I appreciate the creators of the icons for their work

## Project Disclaimer: For Demonstration Purposes Only

**Please Note**: The project provided here is for demonstration purposes only and may contain bugs or glitches. It is important to understand that this implementation may require further development and refinement before it can be considered suitable for real-world applications. The intention behind sharing this project is to provide a starting point and showcase the potential of the concepts and technologies used. It is encouraged for users to further enhance and improve the project based on their specific needs and requirements.

Feel free to contribute, modify, or build upon this project to make it better and more robust. Your feedback, bug reports, and suggestions for improvement are highly appreciated. 
