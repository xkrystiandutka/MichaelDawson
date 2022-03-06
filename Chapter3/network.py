# Network

print("\tNetwork")
print("\tOnly for vip!\n")

security = 0

username = ""
while not username:
    username = input("Users: ")

password = ""
while not password:
    password = input("Password: ")

if username == "M.Dawson" and password == "mystery":
    print("Hi, Mike!")
    security = 5
elif username == "S.Meier" and password == "civilisation":
    print("Hi, Sid!")
    security = 3
elif username == "S.Miyamoto" and password == "mariobros":
    print("Hi, Shigeru?")
    security = 3
elif username == "W.Wright" and password == "simsowie":
    print("Hi, Will?")
    security = 3
elif username == "Guest" or password == "guest":
    print("Welcome, Guest!")
    security = 1
else:
    print("Failed login attempt. You're not that special.")

input("To exit the program, press the Enter key.")