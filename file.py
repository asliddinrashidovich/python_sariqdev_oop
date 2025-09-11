import pickle

mybirth = 29021960

with open("pi_million_digits.txt") as file:
    pi = file.read()
pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
pi = pi.replace(' ','')


pi = float(pi)

with open("yang_pickle.txt", 'wb') as file:
    pickle.dump(pi, file)


inp = input("yozing")

with open('yang_pickle.txt', 'rb') as file:
    file.load(inp)