from dataclasses import replace


a='ammu'
b='anu'
print(a.replace(a[0:2],b[0:2]))
print(b.replace(b[0:2],a[0:2]))