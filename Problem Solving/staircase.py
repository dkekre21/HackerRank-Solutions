n = int(input())
def staircase(n):
    for i in range(1,n+1):
      print(('#'*i).rjust(n,' '))
staircase(n)