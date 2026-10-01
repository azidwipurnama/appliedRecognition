print ("\033c")
import random
import matplotlib.pyplot as plt
import numpy as np

# List untuk menyimpan data
data = []

# Membuat 100 data dengan nilai u dan v acak
for i in range(100):
    u = random.randint(0, 100)
    v = random.randint(0, 100)
    data.append([u, v])

# Memisahkan data menjadi dua list: x (atau u) dan y (atau v)
x, y = zip(*data)

# Membuat scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c='blue', marker='o', alpha=0.7)

# Menghitung batas x untuk garis
x_values = np.linspace(0, 100, 100)

# Menentukan persamaan garis
y1 = 0.8 * x_values + 8
y2 = -0.8 * x_values + 92

# Batasi y1 dan y2 pada rentang 0 - 100
y1 = np.clip(y1, 0, 100)
y2 = np.clip(y2, 0, 100)

# Plot garis y1
plt.plot(x_values, y1, color='red', label='y = 0.8x + 8')

# Plot garis y2
plt.plot(x_values, y2, color='green', label='y = -0.8x + 92')

# Inisialisasi list untuk setiap kelompok
kelompok_1 = []
kelompok_2 = []
kelompok_3 = []
kelompok_4 = []

# Menghitung nilai y pada garis merah dan hijau untuk setiap x
for xi, yi in zip(x, y):
    y_red = 0.8 * xi + 8
    y_green = -0.8 * xi + 92

    if yi > y_red and yi < y_green:
        kelompok_1.append((xi, yi))
    elif yi > y_red and yi > y_green:
        kelompok_2.append((xi, yi))
    elif yi < y_red and yi > y_green:
        kelompok_3.append((xi, yi))
    elif yi < y_red and yi < y_green:
        kelompok_4.append((xi, yi))

# Print data untuk setiap kelompok
print("\nKelompok 1 (Garis Merah > Data dan Garis Hijau < Data):")
print(kelompok_1)
print("Jumlah data dalam kelompok 1 adalah : ", len(kelompok_1))

print("\nKelompok 2 (Garis Merah > Data dan Garis Hijau > Data):")
print(kelompok_2)
print("Jumlah data dalam kelompok 2 adalah : ", len(kelompok_2))

print("\nKelompok 3 (Garis Merah < Data dan Garis Hijau > Data):")
print(kelompok_3)
print("Jumlah data dalam kelompok 3 adalah : ", len(kelompok_3))

print("\nKelompok 4 (Garis Merah < Data dan Garis Hijau < Data):")
print(kelompok_4)
print("Jumlah data dalam kelompok 4 adalah : ", len(kelompok_4))

# Set batas sumbu
plt.xlim(0, 100)
plt.ylim(0, 100)

# Plot settings
plt.title('Scatter Plot with 2 Linear Lines')
plt.xlabel('u')
plt.ylabel('v')
plt.grid(True)
plt.legend()