user = "rockets"
password = "raptors"

c_user = input("Enter username: ")
c_password = input("Enter password: ")

if c_user == user and c_password == password:
    print("Welcome")
else:
    print("Login Failed")
