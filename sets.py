#lists we use []
#tuples we use ()
#sets we use {}
cs_courses={'History','Math','Physics','CompSci','CompSci','CompSci'}
print("This is the content of cs_courses",cs_courses)
art_courses={'History','Math','Art','Design','Design','Design'}
print("This is the content of art_courses",art_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.union(art_courses))
print(cs_courses.difference(art_courses))
print(art_courses.difference(cs_courses))
art_courses.remove('Math')
art_courses.add('Computer')
print(art_courses)
print("after the pop")
print("-------------------")

print("This is poped ",art_courses.pop())

print(art_courses)
art_courses.pop()
print(art_courses)
art1_courses= art_courses.copy()
print("This is the content of art_courses ",art_courses)
print("This is the content of art1_courses ",art1_courses)