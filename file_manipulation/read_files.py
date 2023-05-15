f = open('readme.txt','r')
print(f.read(20),end='')
###################################
with open('readme.txt', 'r') as f:
    f_content = f.read(100)
    print(f_content,end='')
