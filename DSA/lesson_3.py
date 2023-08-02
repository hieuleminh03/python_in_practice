# lesson 3

def check_palindrome(): # Nhap vao 1 chuoi, kiem tra xem chuoi do co phai la palindrome ko
    # xyz ko phai palindrome
    # xyx -> xyx
    # abba -> abba
    # neu la palindrome print("yes") ko thi print("no")
    # goi y: su dung ham len(a) de nhan ve do dai cua chuoi
    a = input("Nhap chuoi: ")
    b = reverse(a)
    if a==b:
        print("ok")
    else:
        print("!!")

def reverse(): # nhap vao 1 chuoi, in ra chuoi do viet nguoc lai
    # abc -> cba
    # 0xyyx -> xyyx0
    a = input("Nhap chuoi: ")
    l = len(a)
    b = ""
    # zux
    # l = 3
    # i in (0,2)
    # i = 0 -> b+a[2] -> b = "x"
    # i = 1 -> b+a[1] -> b = "xu"
    # i = 2 -> b+a[0] -> b = "xuz"
    for i in range(0, l):
        b = b+a[l-i-1]
    return b

def reverse(a):
    l = len(a)
    b = ""
    # zux
    # l = 3
    # i in (0,2)
    # i = 0 -> b+a[2] -> b = "x"
    # i = 1 -> b+a[1] -> b = "xu"
    # i = 2 -> b+a[0] -> b = "xuz"
    for i in range(0, l):
        b = b+a[l-i-1]
    return b

def test():
    a = input("Chuoi: ")

if __name__ == "__main__":
    check_palindrome()