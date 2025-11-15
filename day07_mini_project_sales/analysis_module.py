# Menghitung total, rata-rata, dan data penting lainya
def analyze_sales(cleaned_sales):
    total = sum(cleaned_sales)
    average = total / len(cleaned_sales)
    highest = max(cleaned_sales)

    return {
        "total": total,
        "average": average,
        "highest": highest
    }