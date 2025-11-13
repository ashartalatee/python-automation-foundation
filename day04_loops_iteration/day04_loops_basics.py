# Belajar bagaimana sistem mengulangi proses secara otomatis
# sampai semua data selesai diproses atau kondisi tertentu tercapai.

# for loop contoh dasar
print(" Example 1: For Loop over List")
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"Processing fruit: {fruit}")

    # For Loop dengan Range
print("\n Example 2: Range Loop")
for i in range(1, 6):
    print(f"Batch {i} processed")

#while loop (conditional loop)
print("\n Example 3: While Loop")
count = 0
while count < 3:
    print(f"Running task {count+1}")
    count += 1

# Automation thinking Example
print("\n Example 4: Automation Loop Simulation")
orders = [1001, 1002, 1003, 1004]
processed = []

for order in orders:
    print(f"Processing order #{order}")
    processed.append(order)

print("\n All orders processed:", processed)

#While Loop with Break Condition
print("\n Example 5: While Loop with Break")
battery_level = 100

while battery_level > 0:
    print(f"Battery at {battery_level}% → Running task...")
    battery_level -= 20
    if battery_level <= 20:
        print("Battery low! Stopping automation.")
        break