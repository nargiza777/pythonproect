with open('flower.jpg','rb') as readfrom:
    with open('backup_flower.jpg', 'wb') as write_to:
        for line in readfrom:
            write_to.write(line)
