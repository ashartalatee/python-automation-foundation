# Belajar bagaimana menulis blok kode yang bisa digunakan berulang kali (reasable)
print("Example 1: Basic Function")

def greet(name):
    """Fungsi sederhana untuk menyapa user."""
    print(f"Hello, {name}! Welcome to Python Automation.")

greet("Ashar")
greet("Data Engineer")

#Fungtion dengan return value
print("\nExample 2: Function with Return Value")
def calculate_tax(amount, rate):
    """Hitung pajak dari nominal tertentu."""
    tax = amount * rate
    return tax

total_tax = calculate_tax(1000000, 0.1)
print(f"Total pajak: Rp {total_tax:,}")

#Function dengan parameter dafault
print("\nExample 3: Default Parameter")

def send_report(name="Client", status="completed"):
    """Kirim laporan dengan nilai default"""
    print(f"Report sent to {name} - status: {status}")

send_report()
send_report("Ashar", "pennding")

#Function untuk automation pattern
print("\nExample 4: Modular Thinking in Automation")

def process_order(order_id):
    """Simulasi proses pesanan."""
    print(f"Processing order #{order_id}...")
    print("Task complete")

def run_batch(orders):
    """Menjalankan batch order menggunakan modular function."""
    for order in orders:
        process_order(order)
    print("All orders processed.")

# Eksekusi
orders = [101, 102, 103]
run_batch(orders)

# Function dengan multiple return
print("\n Example 5: Multiple Return Values")

def analyze_data(numbers):
    """Return hasil analisis sederhana."""
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

data = [10, 20, 30, 40, 50]
total, avg = analyze_data(data)
print(f"Total: {total}, Average: {avg}")