from Translation.deeptrans import *


translate = TransLate('Hello', 'uk')
print(translate)

detec = LangDetect('Hello', 'all')
print(detec)

code = CodeLang('uk')
print(code)
code = CodeLang('ukrainian')
print(code)

LanguageList('screen', 'Hallo')