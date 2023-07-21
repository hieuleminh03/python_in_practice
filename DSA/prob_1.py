# statement: https://oj.vnoi.info/problem/fc148_sand
# Cho 2 số nguyên S và A
# Kiểm tra xem có tồn tại cặp (x,y) sao cho
# x + y = S
# x AND y = A ?

def solve(A,S):
    for x in range(0,int(S/2)):
        y = S - x
        if x & y == A:
            return 1
    return 0
    

n = int(input())

while n:
    
    (S,A) = input().split()
    
    S = int(S)
    A = int(A)
    
    print("Yes" if solve(S, A) else "No")
        
    n-=1