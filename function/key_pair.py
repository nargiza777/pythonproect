def funct(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for k,v in kwargs.items():
        print(f"key is {k} - value is {v}")

funct(name="jake",lastname="Rogers",age=10)
funct(profession="Engineer",city="Frisco",age=50)
funct(Hobby="Football",music="Jazz")

###########################################

def funct(age,*args,**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(args)
    print(f"age is {age}")
    # for k,v in kwargs.items():
    #     print(f"key is {k} - value is {v}")

funct(10,1,name="jake",lastname="Rogers")  #these are kept in kwargs
# funct(profession="Engineer",city="Frisco",age=50)
# funct(1,2,3,4,5,Hobby="Football",music="Jazz")
