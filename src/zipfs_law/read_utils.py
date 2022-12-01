import re

def getWordsFromVoinich(txt) -> str:
    txt = txt.replace("-", ",")
    txt = txt.replace('=', ',')

    return txt.split(",")

def getWordsFromWiki(txt) -> str:
    return re.findall(r'\w+', txt)




