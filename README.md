# Simple Locking Protocol (Exclusive Lock Only)
Program dibuat dengan bahasa Python untuk mensimulasikan protokol Simple Locking. 
## Petunjuk Penggunaan Program
- Buat file `.txt` yang berisi rangkaian transaksi dengan format sebagai berikut `R1X` dengan `R` merupakan jenis transaksi antara Read, Write, atau Commit, `1` berarti nomor transaksi, dan `X` merupakan resource yang digunakan. Setiap transaksi dipisahkan dengan `;`. Contoh:
  ```
  W1X;W2X;W2Y;R1Y;C1;C2;W3X;W3Y;C3
  ```
- Jalankan program dengan menggunakan command `python3 main.py` dari directory repository.
- Ketikkan nama file `.txt` yang berisi transaksi sesuai format
- Program akan mengeluarkan keluaran berupa hasil pembacaan file dan hasil transaksi final.