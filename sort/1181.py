n=int(input())
words=[]
for i in range(n):
    word=input()
    words.append(word)

words=list(set(words))
for i in sorted(words, key = lambda word: (len(word),word)):
    print(i)