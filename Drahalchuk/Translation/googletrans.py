from googletrans import Translator
from typing import Literal 
import googletrans 

translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])


def TransLate(text : str,  dest : str, src: str = 'auto') -> str:
    try:
        translation = translator.translate(text, dest, src)
        return translation.text
    except Exception as e:
        return print(f"Помилка: {e}")



def LangDetect(text : str, set : Literal['lang', 'confidence', 'all'] = all ) -> str: 
    try:
        detection = translator.detect_legacy(text)
        if set == 'lang':
            return f"lang: {detection.lang}"
        elif set == 'confidence':
            return f"confidence: {detection.confidence}"
        elif set == 'all':
            return f"lang: {detection.lang}, confidence: {detection.confidence}"
    except Exception as e:
        return print(f"Помилка: {e}")
    

def CodeLang(lang : str) : 
    try:
        if(len(lang) < 3):
            return googletrans.LANGUAGES[lang]
        
        return googletrans.LANGCODES[lang]

    except Exception as e:
        return print(f"Помилка: {e}")
    

def LanguageList(out : str, text : str) :
    if(out == 'screen'):    
        count = 0
        print(f"{'N':<3} {'Language':<20} {'ISO-639':<10} {'Text'}")
        print("-----------------------------------------------------")
        for lang in googletrans.LANGCODES:
            translated = TransLate(text, lang)
            language = CodeLang(lang) 
            count+=1
            print(f"{count:<3} {lang:<20} { language:<10} {translated}")
    elif out == 'file':
        with open('language_list.txt', 'w', encoding='utf-8') as file:
            count = 0
            file.write(f"{'N':<3} {'Language':<20} {'ISO-639':<10} {'Text'}\n")
            file.write("-----------------------------------------------------\n")
            for lang in googletrans.LANGCODES:
                translated = TransLate(text, lang)
                language = CodeLang(lang)
                count += 1
                file.write(f"{count:<3} {lang:<20} {language:<10} {translated}\n")
