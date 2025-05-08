import sys
# N = total number of words
# r = required length of word 

def factorial(n):
    if n < 2:
        return 1
    else:
        print(n)
        return n * factorial(n-1)
    
def Permutation():
    N, r = input("Enter numbers in format : N <space> R : ").split(" ")
    if int(r) > int(N):
        print("Not Possible as The Total length is lower than required word length\n");sys.exit()
    else:
        print(
            factorial(int(N)) / factorial(int(N)-int(r))
            )



##### PERMUTATION using Lambda ######

def factorials(N:int):
    if N < 2:
        return 1
    else:
        return N * ( factorials( N-1 ))

x = lambda a, b : factorials(a) / factorials(a-b)
print( x(3,3) )
