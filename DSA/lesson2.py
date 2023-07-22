# String

a = "Lesson"

def concat(): # Nhập vào 2 chuỗi, ghép lại rồi in ra
    # VD: nor mal  ->  normal
    a = "nor"
    b = "mal"
    S = a+b
    print(S)

def separate(a): # Nhập vào 1 chuỗi, in ra từng chữ cái của nó
    # VD: okb  ->
    # o
    # k
    # b
    
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print(a[4])
    print(a[5])

def count_char(a): # Nhập vào 1 chuỗi, in ra số chữ cái nó có
    # VD: example -> 7
    count = 0
    for x in a:
        if x is int:
            pass
        else:
            count += 1

    print("số chữ cái của chuỗi: " + str(count))
            
def capitalize(a): # Nhập vào 1 chuỗi, in ra nó nhưng tất cả viết hoa
    # VD: vrSCbg -> VRSCBG
    print(a.upper())

if __name__ == "__main__":
    concat()
