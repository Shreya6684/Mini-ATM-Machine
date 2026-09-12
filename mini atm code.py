# Mini Smart ATM System

user_data = {
    "12345": {"name": "Shreya Sharma", "pin": "2219", "balance": 5000, "transactions": []}
}

def register():
    print("\n--- Create New Account ---")
    user_id = input("Create User ID: ")
    
    if user_id in user_data:
        print("❌ User ID already exists!\n")
        return
    
    name = input("Enter Name: ")
    pin = input("Create PIN: ")
    
    user_data[user_id] = {
        "name": name,
        "pin": pin,
        "balance": 0,
        "transactions": []
    }
    
    print("✅ Account created successfully!\n")

def receipt(user_id, type, amount):
    balance = user_data[user_id]["balance"]
    print("\n------ 🧾 RECEIPT ------")
    print(f"User: {user_data[user_id]['name']}")
    print(f"Transaction: {type}")
    print(f"Amount: ${amount:.2f}")
    print(f"Available Balance: ${balance:.2f}")
    print("------------------------\n")

def login():
    user_id = input("Enter User ID: ")
    if user_id not in user_data:
        print("❌ Invalid User ID\n")
        return None
    
    user = user_data[user_id]
    attempts = 3
    
    while attempts > 0:
        pin = input(f"Enter PIN ({attempts} attempts left): ")
        if pin == user["pin"]:
            print(f"✅ Login Successful! Welcome {user['name']}\n")
            return user_id
        attempts -= 1
    
    print("❌ Account Locked!\n")
    return None

def check_balance(user_id):
    print(f"💰 Balance: ${user_data[user_id]['balance']:.2f}\n")

def deposit(user_id):
    amount = float(input("Enter deposit amount: $"))
    if amount <= 0:
        print("❌ Invalid amount!\n")
        return
    
    user_data[user_id]["balance"] += amount
    user_data[user_id]["transactions"].append(f"Deposit: +${amount:.2f}")
    
    print("✅ Deposit Successful!")
    receipt(user_id, "Deposit", amount)

def withdraw(user_id):
    amount = float(input("Enter withdrawal amount: $"))
    balance = user_data[user_id]["balance"]
    
    if amount <= 0 or amount > balance:
        print("❌ Invalid / Insufficient balance!\n")
        return
    
    if amount > balance * 0.5:
        print("⚠️ Suspicious Transaction!\n")
    
    user_data[user_id]["balance"] -= amount
    user_data[user_id]["transactions"].append(f"Withdrawal: -${amount:.2f}")
    
    print("✅ Withdrawal Successful!")
    receipt(user_id, "Withdrawal", amount)

def show_transactions(user_id):
    txns = user_data[user_id]["transactions"]
    print("\n📋 Last Transactions:")
    for t in txns[-5:]:
        print("•", t)
    print()

def main():
    print("=" * 40)
    print("   🏦 MINI SMART ATM SYSTEM 🏦")
    print("=" * 40)
    
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose option: ")
        
        if choice == "1":
            user_id = login()
            if user_id:
                while True:
                    print("\n--- MENU ---")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transactions")
                    print("5. Logout")
                    
                    ch = input("Select: ")
                    
                    if ch == "1":
                        check_balance(user_id)
                    elif ch == "2":
                        deposit(user_id)
                    elif ch == "3":
                        withdraw(user_id)
                    elif ch == "4":
                        show_transactions(user_id)
                    elif ch == "5":
                        break
                    else:
                        print("❌ Invalid option")
        
        elif choice == "2":
            register()
        
        elif choice == "3":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()