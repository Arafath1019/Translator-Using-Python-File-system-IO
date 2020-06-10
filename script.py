from translate import Translator

translator = Translator(to_lang="zh")

try:
    with open('test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('My_Translated_file.txt', mode='w') as translated_file:
            translated_file.write(translation)

except FileNotFoundError as err:

    print('File not found, please check your file path.')

except IOError as err:
    print(err)
