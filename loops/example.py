vowels="aeiou"
a_sentence="Hello world"
new_sentence=""
#TASK IS: check a_sentence: check if the char is in vowels, if it's there - make it upper case

#iterate the each chars in the sentence
for i,ch, in enumerate(vowels):
#find the vowels
    if ch in vowels:
#make the vowels upper case
        new_sentence=new_sentence+str.upper(ch)#if it's in the vowel - put it in new_sentence
    else:     #if it's not there, just edit
        new_sentence=new_sentence + ch

#print that on the screen
print(new_sentence)
