doc=input()
word=input()
answer=0
while word in doc:
    answer+=1
    word_idx=doc.index(word)
    doc=doc[word_idx+len(word):]

print(answer)
