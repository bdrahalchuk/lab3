from deep_translator import GoogleTranslator
from typing import Literal 
from langdetect import detect
from langdetect import detect_langs

def TransLate(text : str,  dest : str, src: str = 'auto') -> str:
    try:
        return GoogleTranslator(source=src, target=dest).translate(text)
    except Exception as e:
        return print(f"Помилка: {e}")


def LangDetect(text : str, set : Literal['lang', 'confidence', 'all'] = all ) -> str: 
    try:
        
        if set == 'lang':
            return f"lang: {detect(text)}"
        elif set == 'confidence':
            langs = detect_langs(text)[0]
            value = str(langs).split(':')[1]
            return f"{value}"
        elif set == 'all':
            langs = detect_langs(text)[0]
            value = str(langs).split(':')[1]
            return f"lang: {detect(text)}, confidence: {value}"
    except Exception as e:
        return print(f"Помилка: {e}")
    
def CodeLang(lang : str) : 
    try:
        languages = GoogleTranslator().get_supported_languages(as_dict=True)
        if lang in languages:
            return languages[lang]
        elif lang in languages.values():
            for code, name in languages.items():
                if name == lang:
                    return code
    except Exception as e:
        return f"Помилка: {e}"
        
def LanguageList(out: str, text: str):
    supported_languages = GoogleTranslator().get_supported_languages(as_dict=True)
    

    if out == 'screen':
        count = 0
        print(f"{'N':<3} {'Language':<20} {'ISO-639':<10} {'Text'}")
        print("-----------------------------------------------------")
        
        for lang, code in supported_languages.items():
            translated = GoogleTranslator(source='auto', target=code).translate(text)
            count += 1
            print(f"{count:<3} {lang:<20} {code:<10} {translated}")
    elif out == 'file':
        with open('language.txt', 'w', encoding='utf-8') as file:
            count = 0
            file.write(f"{'N':<3} {'Language':<20} {'ISO-639':<10} {'Text'}\n")
            file.write("-----------------------------------------------------\n")
            
            for lang, code in supported_languages.items():
                translated = GoogleTranslator(source='auto', target=code).translate(text)
                count += 1
                file.write(f"{count:<3} {lang:<20} {code:<10} {translated}\n")


