# 🔐 Secure Password Manager

A comprehensive cybersecurity tool built in Python that securely stores and retrieves passwords using industry-standard encryption. This project demonstrates the practical application of confidentiality, authentication, and secure file handling.

## 🚀 Features
* **Master Password Protection:** Uses **SHA-256 Hashing** to authenticate the user before granting access.
* **Strong Encryption:** Encrypts all stored passwords using **Fernet (Symmetric Encryption)** so data is unreadable at rest.
* **Hidden Input:** Masks password entry in the terminal to prevent "shoulder surfing."
* **Persistent Storage:** Saves encrypted data to a local file (`passwords.txt`), allowing data to survive system restarts.
* **Portable Deployment:** Compiled into a standalone `.exe` file using PyInstaller.

## 🛠️ Technologies Used
* **Python 3.x**
* **Cryptography Library:** For generating keys and encrypting data.
* **Hashlib:** For hashing the master password.
* **Getpass:** For secure, hidden user input.
* **PyInstaller:** For converting the script into an executable.

## ⚙️ How to Run
### Option 1: Run the Executable (No Python Required)
1. Navigate to the folder containing `secure_pass.exe`.
2. Double-click the file.
3. Follow the on-screen prompts to set up your Master Password.

### Option 2: Run from Source
1. Clone the repository:
   ```bash
   git clone [https://github.com/durvesh55/PasswordManager.git](https://github.com/durvesh55/PasswordManager.git)
Install dependencies:

Bash
pip install cryptography
Run the script:

Bash
python secure_pass.py
📂 Project Structure
secure_pass.py: The main source code.

secure_pass.exe: The compiled application.

master.hash: Stores the hashed master password (created on first run).

secret.key: The encryption key (DO NOT SHARE THIS).

passwords.txt: The encrypted database of passwords.

🔒 Security Note
This tool generates a secret.key file. If this file is lost, all stored passwords become irretrievable. If this file is stolen, the encryption can be bypassed. Keep it secure!


5.  **Save the file** (`Ctrl + S`).

---

### **Step 2: Push the Changes to GitHub**
Now we need to tell GitHub, "Hey, I updated the README, please show the new version."

Run these 3 commands in your terminal (one by one):

1.  **Stage the Change:**
    ```powershell
    & "C:\Program Files\Git\cmd\git.exe" add README.md
    ```

2.  **Commit (Save) the Change:**
    ```powershell
    & "C:\Program Files\Git\cmd\git.exe" commit -m "Updated README with project documentation"
    ```

3.  **Push (Upload) the Change:**
    ```powershell
    & "C:\Program Files\Git\cmd\git.exe" push
    ```

---

### **Step 3: Check Your Work**
Go back to your GitHub link: **[https://github.com/durvesh55/PasswordManager](https://github.com/durvesh55/PasswordManager)**

Refresh the page. You should now see a beautiful, professional project description right on the front page!