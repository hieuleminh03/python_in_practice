a = [1,2,3,4,5,5,6]

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

def print_larger_1(a): # in ra cac so lon hon x
    for x in a:
        if x > 1:
            print(x)
        
if __name__ == "__main__":
    print_larger_1(a)