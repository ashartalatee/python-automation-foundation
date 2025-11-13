# 🔁 Day 4 — Loop & Iteration

## 1️⃣ Kenapa ini penting
- Automation = pekerjaan berulang yang diotomatisasi.
- Loop adalah “mesin” di balik setiap script automation.
- Tanpa loop, sistem tidak bisa memproses banyak data secara efisien.

## 2️⃣ Jenis Loop di Python
| Jenis | Kapan digunakan | Contoh |
|--------|------------------|---------|
| for loop | Saat tahu berapa kali proses diulang | `for x in data:` |
| while loop | Saat belum tahu kapan berhenti (berdasarkan kondisi) | `while status == "running":` |

## 3️⃣ Pola Umum (Iteration Patterns)
| Pattern | Deskripsi | Contoh Automation |
|----------|-------------|-------------------|
| Sequential Processing | Memproses data satu per satu | Loop invoice list untuk kirim email |
| Conditional Loop | Berhenti saat kondisi terpenuhi | Loop download sampai sukses |
| Accumulation | Mengumpulkan hasil ke list | Menyimpan hasil scraping |
| Monitoring Loop | Berjalan terus sampai status berubah | Cek API status tiap 5 detik |

## 4️⃣ Analogi
Loop = “mesin conveyor” dalam pabrik automation.  
Setiap data adalah barang yang lewat di atasnya,  
dan Python memutuskan kapan conveyor berhenti.
