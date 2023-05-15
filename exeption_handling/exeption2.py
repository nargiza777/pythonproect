try:
    print(name)
except:
    print("name is initialized to no name")
    name="no name"
finally:
    print(f"Hello {name}")

#############################################
