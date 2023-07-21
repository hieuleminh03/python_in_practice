a = [1,2,3,6,10,5,6]

def check_odd(a): # in ra tinh chan le cua tung so ?
    for x in a:
        if x%2 == 0:
            print("Chan")
        else:
            print("Le")
            
def sum(a): # tinh tong
    s = 0
    for x in a:
        s += x
    print("Tong la: " + str(s))
    
def tich(a): # tinh tich
    s = 1
    for x in a:
        s *= x
    print("Tich la: " + str(s))
    
def print_odd(a): # in ra cac so chan
    for x in a:
        if x%2 == 0:
            print(x)

def print_even(a): # in ra cac so le
    for x in a:
        if x%2 == 1:
            print(x)

def print_larger_x(a, x): # in ra cac so lon hon x
    for b in a:
        if b > x:
            print(b)
            
def test(a):
    a.append(2) # them vao cuoi
    del a[1] # xoa phan tu a[1]
    a.insert(3,50) # o index them gia tri
    
def swap(a, x, y): # doi cho gia tri 2 index x va y
    temp = x
    a[x] = a[y]
    a[y] = a[x]

def find_max(a): # tim gia tri lon nhat
    max = a[0]
    for x in a:
        if x > max:
            max = x # cap nhat lai gia tri cua max
    print(max)

def find_min(a): # tim gia tri nho nhat
    pass

def check_element(a, x): # kiem tra xem x co o trong list khong
    for b in a:
        if b == x:
            print("Yes")
            return
    print("No")

def del_list(a): # xoa toan bo list
    del a
    
def count_odd(a): # dem so phan tu chan trong danh sach
    count = 0
    for x in a:
        if x%2:
            pass
        else:
            count += 1
            
    print("So phan tu chan: " + str(count))
      
if __name__ == "__main__":
   count_odd(a)
        
