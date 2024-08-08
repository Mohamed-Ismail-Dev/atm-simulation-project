import sqlite3
import hashlib
import random

class Data:
    def __init__(self, name, password):
        self.user_name = name
        self.password = password
        self.balance = 0  # Initialize balance to 0
        self.conn = sqlite3.connect('user_data.db')
        self.cursor = self.conn.cursor()

    def checking(self):
        input_name = self.user_name.lower().strip()
        input_password = self.password.strip()

        query = "SELECT * FROM users WHERE LOWER(name)=? AND password=?"
        self.cursor.execute(query, (input_name, input_password))

        user = self.cursor.fetchone()

        if user:
            print("LOGGED IN SUCCESSFULLY")
            self.balance = user[3]
            return True
        else:
            return "INVALID INPUTS"

    def generate_otp(self):
        return random.randint(1000, 9999)  # 4-digit numeric OTP

    def hash_otp(self, otp):
        return hashlib.sha256(str(otp).encode()).hexdigest()  # Hashing OTP using SHA-256

    def otp(self):
        otp = self.generate_otp()
        hashed_otp = self.hash_otp(otp)
        print(f"OTP: {otp}")
        otpin = input("ENTER OTP (4 digits):")
        if hashed_otp == self.hash_otp(otpin):
            self.otp_status = True
            return self.otp_status
        else:
            return "INVALID OTP"

    def check_balance(self):
        otp = self.otp()
        if otp == True:
            return f"BALANCE: Rs.{self.balance}"
        else:
            return otp

    def withdraw(self):
        otp = self.otp()
        if otp == True:
            amount = int(input("ENTER AMOUNT:"))
            if amount <= self.balance:
                self.balance -= amount
                self.cursor.execute("UPDATE users SET balance=? WHERE name=?", (self.balance, self.user_name))
                self.conn.commit()
                return f"Rs.{amount} WITHDRAWAL SUCCESSFUL"
            else:
                return "INSUFFICIENT BALANCE"
        else:
            return otp

    def deposit(self):
        otp = self.otp()
        if otp == True:
            amount = int(input("ENTER AMOUNT:"))
            if amount > 0:
                self.balance += amount
                self.cursor.execute("UPDATE users SET balance=? WHERE name=?", (self.balance, self.user_name))
                self.conn.commit()
                return f"Rs.{amount} DEPOSITED SUCCESSFULLY"
            else:
                return "INVALID AMOUNT"
        else:
            return otp

    def start(self):
        login = self.checking()
        if login == True:
            print("WELCOME TO SBMI ATM")
            while True:
                print("""SELECT
                         1.BALANCE ENQUIRY
                         2.CASH DEPOSIT
                         3.CASH WITHDRAWAL
                         4.EXIT""")
                select = input("SELECT:")
                if select == '1':
                    print(self.check_balance())
                elif select == '2':
                    print(self.deposit())
                elif select == '3':
                    print(self.withdraw())
                elif select == '4':
                    break
        else:
            print("ERROR")

if __name__ == "__main__":
    # Create the users table if not exists
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            password TEXT,
            balance REAL DEFAULT 0
        )
    ''')
    conn.commit()

    # Insert sample users if not exists
    cursor.execute("SELECT * FROM users")
    if not cursor.fetchall():
        cursor.execute("INSERT INTO users (name, password, balance) VALUES ('ismail', '123456', 0)")
        cursor.execute("INSERT INTO users (name, password, balance) VALUES ('ayesha', '1020300', 0)")
        conn.commit()

    enter_name = input("ENTER USER NAME:")
    enter_pass = input("ENTER PASSWORD:")
    run = Data(enter_name, enter_pass)
    run.start()
