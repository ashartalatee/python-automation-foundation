#Melatih logika jika maka lakukan ini yang menjadi inti automation.
temperature = 32

if temperature > 30:
    print("Cuaca panas! nyalakan pendingin otomatis.")
elif temperature > 20:
    print("Cuaca hangat, pendingin standby.")
else:
    print("Cuaca dingin, pendingin dimatikan.")

#contoh dengan data dinamis
user_score = 78

if user_score >= 85:
    status = "Excellent"
elif user_score >= 70:
    status = "Good"
else:
    status = "Need Improvement"

print(f"User score: {user_score} → Status: {status}")

#Logical Operators
is_logged_in = True
has_permission = False

if is_logged_in and has_permission:
    print("Akses diberikan.")
elif is_logged_in and not has_permission:
    print("Akses terbatas.")
else:
    print("silahkan login terlebih dahulu.")


#Automation thinking example
customer_balance = 120000
auto_payment_threshold = 1000000

if customer_balance >= auto_payment_threshold:
    print("Jalankan auto-payment ke vendor.")
else:
    print(" Tunggu saldo mencukupi sebelum auto-payment.")