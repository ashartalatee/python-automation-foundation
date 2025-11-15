# Menampilkan hasil analisis
def print_report(result):
    print("Laporan Penjualan Harian")
    print(f"Total Penjualan : Rp {result['total']:,}")
    print(f"Rata-rata Penjualan: Rp {result['average']:,}")
    print(f"Penjualan Tertinggi: Rp {result['highest']:,}")
    print("=" * 35)