# lesson 3

def check_palindrome(): # Nhap vao 1 chuoi, kiem tra xem chuoi do co phai la palindrome ko
    # xyz ko phai palindrome
    # xyx -> xyx
    # abba -> abba
    # neu la palindrome print("yes") ko thi print("no")
    # goi y: su dung ham len(a) de nhan ve do dai cua chuoi
    a = input("Nhap chuoi: ")
    b = reverse(a)
    if a == b:
        print("yes")
    else:
        print("no")

def reverse(): # nhap vao 1 chuoi, in ra chuoi do viet nguoc lai
    # abc -> cba
    # 0xyyx -> xyyx0
    a = input("nhap chuoi:")
    pass
    l = len(a)
    b = ""
    for i in range(0 , l):
        b = b+a[l-i-1]
    return b
def reverse(a):
    pass
    l = len(a)
    b = ""
    for i in range(0 , l):
        b = b+a[l-i-1]
    return b
def test():
    a = input("Chuoi: ")
    pass
if __name__ == "__main__":
    check_palindrome()