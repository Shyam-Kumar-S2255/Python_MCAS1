s = input('string : ')
for i in s.casefold():
    if i=='a' or i=='e' or i=='i' or i=='o' or  i=='u':
        print(i,end=" ")
    