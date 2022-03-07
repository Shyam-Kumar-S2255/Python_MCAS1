class Time():
    def __init__(self):
        self.__h=int(input('HH:'))
        self.__m=int(input('MM:'))
        self.__s=int(input('SS:'))
    def __add__(self,value):
        return self.__h+value.__h,self.__m+value.__m,self.__s+value.__s
t1=Time()
t2=Time()
h,m,s=t1+t2
print(h,'-',m,'-',s)