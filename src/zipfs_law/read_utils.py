def getWordsFromVoinich(txt) -> str:
    txt = txt.replace("-", ",")
    txt = txt.replace('=', ',')

    return txt.split(",")



