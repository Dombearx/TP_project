import nltk, os
# import os


dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path+"\\nad_niemnem_txt\\Nad_Niemnem_Tom_pierwszy.txt", encoding="utf-8-sig") #utf8
lines = f.readlines()
text = ""
for l in lines:
    text += l

f.close()

sent_text = nltk.sent_tokenize(text)

output = open(dir_path+"\\nad_niemniem_lines.txt", "w", encoding="utf-8-sig")

for l in sent_text:
    output.write(l+"\n")

output.close()