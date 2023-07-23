# String
# use input()

def concat(): # Nhập vào 2 chuỗi, ghép lại rồi in ra
    # VD: nor mal  ->  normal
    a = input("Nhap chuoi 1: ")
    b = input("Nhap chuoi 2: ")
    print(a+b)

def separate(): # Nhập vào 1 chuỗi, in ra từng ký tự của nó
    a = input("Nhap chuoi: ")
    for x in a:
        print(x)

def count_char(): # Nhập vào 1 chuỗi, in ra số ký tự nó có
    a = input("Nhap chuoi: ")
    count = 0
    for x in a:
        count += 1
    print(count)
            
def capitalize(): # Nhập vào 1 chuỗi, in ra nó nhưng tất cả viết hoa
    # VD: vrSCbg -> VRSCBG
    print(input("Nhap chuoi: ").upper())

if __name__ == "__main__":
    concat()
