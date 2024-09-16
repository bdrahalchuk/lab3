import json
import os
from googletrans import Translator

def load_config(config_file):
    with open(config_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_text_stats(text):
    num_chars = len(text)
    words = text.split()
    num_words = len(words)
    num_sentences = text.count('.') + text.count('!') + text.count('?')
    return num_chars, num_words, num_sentences

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    config = load_config('Drahalchuk/config.json')
    
    text_file = config["text_file"]
    target_language = config['target_language']
    output_type = config['output']
    max_characters = config['max_characters']
    max_words = config['max_words']
    max_sentences = config['max_sentences']

    if not os.path.exists(text_file):
        print(f"Файл {text_file} не найден.")
        return

    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()

    num_chars, num_words, num_sentences = get_text_stats(text)
    
    print(f"Файл: {text_file}")
    print(f"Розмір: {num_chars} символів")
    print(f"Кількість слів: {num_words}")
    print(f"Кількість речень: {num_sentences}")
    print(f"Мова: {target_language}")

    if num_chars > max_characters:
        text = text[:max_characters]
    if num_words > max_words:
        words = text.split()
        text = ' '.join(words[:max_words])
    if num_sentences > max_sentences:
        sentences = text.split('. ')
        text = '. '.join(sentences[:max_sentences]) + '.'

    translated_text = translate_text(text, target_language)

    if output_type == 'screen':
        print(f"Переклади ({target_language}):")
        print(translated_text)
    elif output_type == 'file':
        output_file = f"{os.path.splitext(text_file)[0]}_{target_language}.txt"
        with open(output_file, 'w') as f:
            f.write(translated_text)
        print("Ok")

main()

