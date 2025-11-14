# 📘 Day 6 — Data Structures for Automation

## 1️⃣ Kenapa Lists & Dictionaries penting?
Dalam automation, hampir semua data datang dalam bentuk:
- list (kumpulan item)
- dictionary (data berpasangan key–value)

Contoh nyata:
- Data dari API → JSON → dictionary + list
- Data dari SQL → list of dicts
- Data CSV → list of rows
- Data order, transaksi, tracking → dict

## 2️⃣ Pola umum dalam data automation

### 🔹 1. Loop Through List
Memproses banyak item sekaligus (batch)

### 🔹 2. Extract Key from Dictionary
Menarik data tertentu dari struktur JSON

### 🔹 3. Transform Data
Mengubah format data supaya siap digunakan

### 🔹 4. Aggregation
Menghitung total, rata-rata, minimum, dst.

## 3️⃣ Kenapa ini relevan untuk Python Automation?
Karena setiap sistem (ETL, API, bot, scraper, report generator) 
menggunakan list dan dictionary sebagai tulang punggung datanya.

Jika kamu paham Lists + Dicts, kamu sudah bisa:

- memproses 1.000+ data dalam loop  
- membaca JSON dari API  
- mengolah data CSV  
- mem-build mini ETL pipeline  
- mengotomatisasi laporan  
