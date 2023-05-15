try:
    f = open('readme1.txt', 'r')
except Exception as e:
    print(f"exception {e}".format(e))