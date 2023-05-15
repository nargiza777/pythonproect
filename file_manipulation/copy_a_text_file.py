with open('readme.txt','r') as readfrom:
    with open('copy_readme.txt', 'w') as write_to:
        for line in readfrom:
            write_to.write(line)
