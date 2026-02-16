from cryptography.fernet import Fernet
import os
import getpass
import hashlib  # NEW: Library for hashing passwords

# --- FUNCTION: MASTER PASSWORD SYSTEM ---
def check_master_password():
    """
    Handles the login process.
    Returns True if login is successful, False otherwise.
    """
    HASH_FILE = "master.hash"

    # CASE 1: No Master Password exists yet (First Run)
    if not os.path.exists(HASH_FILE):
        print("--- SETUP MASTER PASSWORD ---")
        while True:
            pwd = getpass.getpass("Create a NEW Master Password: ")
            confirm = getpass.getpass("Confirm Master Password: ")
            
            if pwd == confirm and pwd != "":
                # Hash the password using SHA-256
                hashed_pwd = hashlib.sha256(pwd.encode()).hexdigest()
                
                # Save the HASH, not the password
                with open(HASH_FILE, "w") as f:
                    f.write(hashed_pwd)
                print("Master Password set successfully!\n")
                return True
            else:
                print("Passwords didn't match or were empty. Try again.\n")

    # CASE 2: Master Password exists (Normal Login)
    else:
        # Read the stored hash
        with open(HASH_FILE, "r") as f:
            stored_hash = f.read()

        # Ask user for password
        pwd = getpass.getpass("Enter Master Password to unlock: ")
        
        # Hash their input to see if it matches the stored hash
        input_hash = hashlib.sha256(pwd.encode()).hexdigest()

        if input_hash == stored_hash:
            print("Access Granted.\n")
            return True
        else:
            print("ACCESS DENIED. Wrong password.\n")
            return False

# --- EXISTING KEY MANAGEMENT ---
def load_key():
    file = open("secret.key", "rb")
    key = file.read()
    file.close()
    return key

# --- MAIN EXECUTION START ---

# 1. First, check the Master Password. If it fails, quit.
if not check_master_password():
    exit()

# 2. Check if encryption key exists (for the data)
if not os.path.exists("secret.key"):
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

key = load_key()
fernet = Fernet(key)

# --- FUNCTION: ADD PASSWORD ---
def add():
    name = input('Account Name: ')
    pwd = getpass.getpass("Password (hidden): ")
    
    encrypted_pwd = fernet.encrypt(pwd.encode()).decode()

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + encrypted_pwd + "\n")
    print(f"Success! Password for {name} added.\n")

# --- FUNCTION: VIEW PASSWORDS ---
def view():
    if not os.path.exists('passwords.txt'):
        print("No passwords saved yet.\n")
        return

    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:
                user, passw = data.split("|")
                try:
                    decrypted_pwd = fernet.decrypt(passw.encode()).decode()
                    print(f"Account: {user} | Password: {decrypted_pwd}")
                except:
                    print(f"Error decrypting password for {user}")
    print("\n")

# --- MAIN LOOP ---
while True:
    mode = input("Menu: (view) passwords, (add) new password, (q) quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")