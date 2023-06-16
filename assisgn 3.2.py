correct_username = "admin"
correct_npassword = "password"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    username = input("Username:n")
    password = input("Password:")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    
    print("Incorrect credentials. Please try again.")
    attempts += 1

if attempts == max_attempts:
    print("Maximum login attempts exceeded. Access denied.")
