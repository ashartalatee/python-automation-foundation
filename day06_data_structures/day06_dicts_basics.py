# Data struktures - Dictionaries
print("DICTIONARY BASICS")

# Dictionary sederhana
user = {
    "name": "Ashar",
    "role": "Automation Developer",
    "level": 1
}

print(user)
print("Name:", user["name"])
print("Role:", user["role"])

# Update nilai
user["level"] = 2
print("Updated user:")

# Menambah key baru
user["skills"] = ["Python", "Automation", "Data Processing"]
print("User with skills:", user)

# Looping dictionary
print("\nLOOPING DICTIONARY")
for key, value in user.items():
    print(f"{key} → {value}")

# Dictionary of objects (mirip JSON)
orders = [
    {"id": 101, "amount": 150000, "status": "pending"},
    {"id": 102, "amount": 200000, "status": "shipped"},
    {"id": 103, "amount": 175000, "status": "completed"},
]

print("\nPROCESS ORDERS")
for order in orders:
    print(f"Order #{order['id']} - Rp {order['amount']:,} - {order['status']}")