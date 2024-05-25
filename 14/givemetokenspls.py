import nltk.tokenize
import re
from collections import Counter
with open("txt.txt", encoding="utf-8") as f:
    text = f.read()
run1 = text.split()
with open("output.txt", "w", encoding="utf-8") as d:
    for i in range(len(run1)):
        d.write(run1[i] + "\n")
run2 = re.findall(r"\w+", text)
with open("output2.txt", 'w', encoding="utf-8") as dd:
    for i in range(len(run2)):
        dd.write(run2[i] + "\n")
run3 = nltk.tokenize.word_tokenize(text)
file = open("output3.txt", "w", encoding="utf-8")
for i in range(len(run3)):
    file.write(run3[i] + '\n')
file.close()

print(f"длина слов подсчитанная с помощью len(split()): {len(run1)}")
print(f"длина слов подсчитанная с помощью Counter(split()): {sum(Counter(run1).values())}")
print(f"длина слов подсчитанная с помощью len(re): {len(run2)}")
print(f"длина слов подсчитанная с помощью Counter(re): {sum(Counter(run2).values())}")
print(f"длина слов подсчитанная с помощью len(nltk): {len(run3)}")
print(f"длина слов подсчитанная с помощью Counter(nltk): {sum(Counter(run3).values())}")