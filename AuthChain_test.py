from AuthChain import AuthChain

def registration(username, password):
    blockchain.register_user('user1', 'password123')
    return "    [*] User signed up: " + username

def login(username, password):
    return "Login successful!" if blockchain.login_user(username, password) else "Invalid username or password!"

# AuthChain test
if __name__ == "__main__":

    # Create a new instance
    blockchain = AuthChain()
    
    # Test users
    test_users = [('user1', 'pass1',), ('user2', 'pass2',)]

    # Test user sign up
    for k_name, k_pass in test_users:
            print("[0]", "User registration:",k_name, k_pass)
            print("[0]", registration(k_name, k_pass))

    # 1. Correct data login test
    print("[1]", "Correct data login test:", test_users[0][0], test_users[0][1])
    print("[1]", login(test_users[0][0], test_users[0][1]) )

    # 2. Incorrect data login test
    print("[2]", "Incorrect data login test:", test_users[0][0], "incorrect_password")
    print("[2]", login(test_users[0][0], "incorrect_password") )

    # 3. Unexistent user login
    print("[3]", "Unexistent user login:", "unexistent", "incorrect_password")
    print("[3]", login("unexistent", "incorrect_password") )
