a=0
b=1
c=int(input("Enter the number of Terms you want:"))
s=0
print('Febonacci Series are:')
print(a,end=' ')
print(b,end=' ')
for i in range(1,c):
    s=a+b
    sum=s
    a=b
    b=s
    print(sum,end=' ')
