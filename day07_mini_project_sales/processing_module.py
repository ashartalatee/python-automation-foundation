# Membersihkan dan memvalidasi data
def clean_sales_data(sales):
    cleaned = []
    for s in sales:
        if isinstance(s, (int, float)) and s >= 0:
            cleaned.append(s)
    return cleaned