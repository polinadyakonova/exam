#Дьяконова Полина, БКЛ161
from bs4 import BeautifulSoup
import os, json

d = {}
for num in os.listdir("thai_pages"):
    f = open("thai_pages/" + num, "r", encoding = "utf-8")
    html = f.read()
    f.close()
    d1 = {}
    s = BeautifulSoup(html, "html.parser")
    text = s.get_text()
    #print(text)
    tr_items = s.find_all("tr")
    for i in tr_items:
        end = i.find_all("td")
        if end:
            w = end[0].find("a")
            if w:
                w = w.get_text()
                d1[w] = end[-1].get_text()                
    d.update(d1)

f = open("thai-eng.json", "w", encoding = "utf-8")
f.write(json.dumps(d)) #json
f.close()

d_con = {}
for key in d:
    if ";" in d[key]: #разделяем значения
        keys = d[key].split(';')
        for k in keys:
            d_con[k.strip()] = key
    else:
        d_con[d[key]] = key

f = open("eng-thai.json", "w", encoding = "utf-8")
f.write(json.dumps(d_con)) #обратный json
f.close()
        
#f = open("dict.txt", "w", encoding = "utf-8")
#for key in d:
#    f.write(key + " " + d[key] + "\n")
#f.close()