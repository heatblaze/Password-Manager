# Password-Manager
A secure and user-friendly password manager built using Python and Tkinter. This tool allows users to store and retrieve credentials securely, as well as manage passwords efficiently via a graphical user interface (GUI).

---

# Features
1. Secure Password Encryption: Encrypts passwords to ensure data security.
2. GUI-Based Management: User-friendly Tkinter interface for adding and retrieving passwords.
3. Local Storage: Credentials are stored locally in an encrypted format.

---

# Technologies used
- Programming Language: Python
- GUI Framework: Tkinter
- Database: SQLite (built-in Python library)
- Encryption: cryptography library (AES encryption)

---

# Prerequisites
- Python 3.6 or higher
- Required Python libraries: tkinter, cryptography, and SQLite3 (built-in).

---

# Usage

## Add Password
- Enter the Service Name, Username, and Password in their respective fields.
- Click Add Password to securely store the credentials.

## Retrieve Password
- Enter the Service Name in the respective field.
- Click Retrieve Password to fetch the stored credentials.

## Security
- Passwords are encrypted using AES (Advanced Encryption Standard) before being stored locally.
- A unique key is used for encryption and decryption to ensure data confidentiality.

---

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/heatblaze/Password-Manager.git
