import re
from datetime import datetime

def getDates(text):
    """
    :param text: Text to Parse
    :return: No. of occurences of date
    """
    pattern = {
        r'\d{4}/\d{2}/\d{2}': ['%Y/%m/%d'],
        r'\d{2}/\d{2}/\d{4}': ['%d/%m/%Y','%m/%d/%Y'],
        r'\d{2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec) \d{4}': ['%d %b %Y']
    }
    count = 0
    for k,v in pattern.items():
        match = re.findall(k, text)
        for m in match:
            for format in v:
                try:
                    datetime.strptime(m, format).date()
                    count += 1
                    break
                except:
                    pass
    return count

text = open("sample.txt","r").read()
print(getDates(text))