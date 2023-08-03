# Python code to reverse a string
# using reversed()
  
# Function to reverse a string
def reverse(string):
    string = "".join(reversed(string))
    return string
  
s = "Quantrimang"
  
print("Chuỗi ban đầu là: ", end="")
print(s)
  
print("Chuỗi sau khi đảo ngược (sử dụng reversed) là: ", end="")
print(reverse(s))