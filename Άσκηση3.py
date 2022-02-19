import re

file = input("Give filename:")
with open(file, "r") as f:
    text = f.read()
    text = " ".join(re.findall(r'[\w ]+', text))

text_list = text.split(" ")
i = 0
while i < len(text_list)-1:
    j = i + 1
    removed = False
    while j < len(text_list):
        if (len(text_list[i])+len(text_list[j]) == 20):
            text_list.pop(i)
            removed = True
            j -= 1
            text_list.pop(j)
            break
        j += 1
    if not removed:
        i += 1

word_count = {}

for word in text_list:
    if len(word) not in word_count.keys():
        word_count[len(word)] = 1
    else:
        word_count[len(word)] += 1

print(word_count)