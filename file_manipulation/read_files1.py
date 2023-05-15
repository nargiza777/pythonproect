with open('readme.txt','r') as f:
    # f_content = f.read(100)
    # print(f_content,end='')
    # f_content = f.read(100)
    # print(f_content, end='')
    # f_content = f.read(100)
    # print(f_content, end='')
    # f_content = f.read(100)
    # print(f_content, end='')
    # f_content = f.read(100)
    # print(f_content, end='')
    size_to_read = 10
    f_content = f.read(size_to_read)
    while len(f_content) > 0:
        print(f_content,end='')
        f_content = f.read(size_to_read)