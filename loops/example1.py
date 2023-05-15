vowels="aeiou"
a_sentence="I like apples oranges and cars and horses"
new_sentence=""
#iterate the each chars in the sentence
for i,ch in enumerate(a_sentence):
#find the vowels
    if ch not in vowels:
#make the vowels upper case
        new_sentence=new_sentence+str.upper(ch)
    else:
        new_sentence=new_sentence + ch

#print the sentence with the uppercase vowels.
print(new_sentence)

for i in a_sentence:
    print(i)
sentence = "".join([i.upper() for i in a_sentence if i not in vowels ])
sentence2 = "".join([i.upper() for i in a_sentence if i in vowels ])

print([i for i in range(10) if i%2==0])
print([i.lower() for i in ["Apple","Car",1,2,3,4,5,6,"loadf"] if type(i)==str ])
print([i*2 for i in ["Apple","Car",1,2,3,4,5,6,"loadf",3.4,5.5] if type(i)==int or type(i)==float ])


print(f"{sentence}".format(sentence))
print(f"{sentence2}".format(sentence))