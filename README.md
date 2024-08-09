# SBMI ATM System

## Description

SBMI ATM System is a simple ATM simulation project developed in Python. It uses SQLite for database management and OTP (One-Time Password) for secure transactions. This project allows users to perform basic banking operations such as balance enquiry, cash deposit, and cash withdrawal.

## Features

- **User Authentication:** Secure login with username and password.
- **OTP Verification:** Additional security with 4-digit OTP for transactions.
- **Balance Enquiry:** Check the account balance.
- **Cash Deposit:** Deposit money into the account.
- **Cash Withdrawal:** Withdraw money from the account with balance verification.
- **Data Security:** User passwords and OTPs are secured using `encryption` techniques.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Mohamed-Ismail-Dev/atm-simulation-project.git
    cd atm-simulation-project
    ```

2. **Install dependencies:**
    Ensure you have Python installed. No additional packages are required as it uses the standard library.

3. **Database setup:**
    The `user_data.db` SQLite database will be created automatically when you run the script. Sample user data is also inserted automatically.

## Usage

1. **Run the application:**
    ```sh
    python atm.py
    ```

2. **Login:**
    Enter the username and password to log in.

3. **Choose an operation:**
    - Balance Enquiry
    - Cash Deposit
    - Cash Withdrawal
    - Exit

4. **OTP Verification:**
    Enter the 4-digit OTP sent to you for secure transactions.

## Sample Users

- **User 1:**
  - Username: `ismail`
  - Password: `123456`

- **User 2:**
  - Username: `ayesha`
  - Password: `1020300`

## Project Structure

```plaintext
atm-simulation-project/
├── user_data.db       # SQLite database
├── atm.py        # Main Python script
└── README.md          # Project documentation
```

## Contributing

Contributions are welcome! Please create a pull request or open an issue for any improvements or bugs.

## License

This project is licensed under the MIT License.

