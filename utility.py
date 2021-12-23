def add(a, b):
    a= a +b
    print(a)
def sub(a,b):
    try:
        a=a-b
        print(a)
    except:
        print("exception")
    
    
a= int(input())
b= int(input())
# try:
#     pass
# except:
#     print("exception")

sub(a,b)
