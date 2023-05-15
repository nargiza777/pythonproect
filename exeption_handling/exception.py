info = {
    'firstname':'Nargiza'
    'lastname':'osmon'
}
print(info['firstname'])
print(info['lastname'])
print(info['job'])

try:      #try your code here
    print(info['job'])
except Exception as e:
    print(type(e))
    print(f "{e}".format(e))
    print(e.args)