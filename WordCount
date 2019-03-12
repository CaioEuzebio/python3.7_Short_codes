
file = open('filetext.txt')
text = file.read()
text = text.lower()
import string
for c in string.punctuation:
    text = text.replace(c, ' ')
text = text.split()

d = {}
for p in text:
    if p not in d:
        d[p] = 1
    else:
        d[p] += 1
print("Times that %s word repeats: " %d['word'])
file.close()
