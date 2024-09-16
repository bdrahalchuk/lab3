from Translation.googletrans import *


translate = TransLate('Hello', 'uk')
print(translate)

detec = LangDetect('Hello', 'all')
print(detec)

code = CodeLang('uk')
print(code)
code = CodeLang('ukrainian')
print(code)

LanguageList('file', 'Hallo')