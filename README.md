# Mini-ATM-Machine
The Mini Smart ATM System is an interactive, menu-driven Python console application designed to simulate real-world automated teller machine (ATM) operations. Built with simplicity and functionality in mind, it provides users with a complete banking interface directly in the command line environment.
Key Features & Functionalities:
1.User Authentication & Security: Includes a login system with a maximum limit of 3 PIN attempts before locking the account to prevent unauthorized access.
2.Account Creation: Allows new users to seamlessly register unique User IDs, personal names, and initial secure PINs.
3.Core Banking Operations: Supports real-time balance inquiries, fund deposits, and cash withdrawals.
4.Input Validation: Restricts invalid entries such as negative amounts or withdrawals exceeding the user's current balance.
5.Fraud Warning System: Features basic anomaly detection that flags high-value withdrawals when a user attempts to withdraw more than 50% of their available balance.
6.Receipt Generation & History: Prints clear transaction summary receipts showing updated available balances, and stores the last 5 transactions for easy history tracking.

Technical Details:
Language: Python 3.x
Data Structure: Uses nested dictionaries for fast, key-value lookup of account details and user transactions.

How to Run-
Clone this repository to your local system:
git clone [https://github.com/Shreya6684/Mini-ATM-Machine.git](https://github.com/Shreya6684/Mini-ATM-Machine.git)
Run the main script using Python:
python main.py
