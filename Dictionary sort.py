y={'carl':40,'alan':2,'bob':1,'danny':3}
l=list(y.items())
print("Dictionary",y)
l.sort()
print('Ascending order is',dict(l))
l.sort(reverse=True)
print('Descending order is',dict(l))
