#dict from page no 97
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

favorite_languages_poll = ['jen','golu','edward','phil','raman','sarah',]

for favorite_language_poll in favorite_languages_poll:
    if favorite_language_poll in favorite_languages.keys():
        print("thank you for responding in poll")
    else:
        print("please take part in poll")
    
