import json
def lang(str):
    configf = open("config.json", "r")
    config = json.loads(configf.read())
    configf.close()
    langf = open("lang/"+config["lang"]+".json", "r",encoding = 'utf-8')
    lang = json.loads(langf.read())
    langf.close()
    print(lang[str])
    return lang[str]

