import keyword as ky
from wordsegment import segment,load
print("loading.....")
load()
print("please wait")
def decrypt_clue(text):   
    key_list = []
    text_new = text.readlines()
    for i in text_new:
        i = i.replace("\n","")
        words = segment(i)
        for x in words:
            if(ky.iskeyword(x)):
                key_list.append(x)
    return key_list 
text = open("E:\project_python_uni\p2\mysterious.txt", "r")
out = decrypt_clue(text)
out_Task1 = out[0]
print(out)
