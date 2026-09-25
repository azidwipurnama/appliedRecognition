# You are allowed to use this code but do not remove the following
# recognition: "This code has been developed by Mohammad Nasucha, Ph.D."
# Scientific knowledge to obtain:
# Students understand nonlinear regression through polynomial function.
# High skill to obtain:
# (1) creating synthetic nonlinear dataset;
# (2) mapping dataset value to real pixel coordinates; 
#     data variables are x and y
#     screen coordinates are x_kanvas and y_kanvas
# (3) auto-adjustment with respect to the x data range, y data range, 
#     and the size of the canvas;
# (4) clustering.
import matplotlib.pyplot as plt
import numpy as np
import random
print ("\033c")                                       #Clear the terminal.

#USER ENTRIES
nama_file = "dataset_nonlinier.npy"
kanvas_row_min, kanvas_row_max = 0, 1000 #ukuran kanvas
kanvas_col_min, kanvas_col_max = 0, 1333 #ukuran kanvas
data_x_min, data_x_max = 0, 100           #range of independent data
data_y_min, data_y_max = 0, 200           #range of dependent data
randval = 0.3 * (data_y_max - data_y_min)
margin_row = round(0.05 * kanvas_row_max)
margin_col = round(0.05 * kanvas_col_max)
m, b = 0.08, 8                     #garis regresi linier u/ simulasi data: y = mx + b
a, b, c, d =  0.0004, -0.06, 1.4, 130
N = 1                              #Ini artinya jumlah dataset = N * rentang data
warna_axis  = (255, 255, 255)
warna_data1 = (255, 190, 30)
warna_data2  = (0, 30, 255)
warna_garis = (255, 0, 0)
nd = 10                         #data node diameter
lw = 4                         #line width
rn = round(nd/2)                #radii of the data nodes
rl = round(lw/2)                #radii of the circles that make up the line
I = 1000                        #banyaknya data (nodes) yang ingin didemokan: 0 - N

def buat_lingkaran(gambar, py, px, r, warna): #sebagai unsur dasar garis, kurva, dan nodes (data)
    for y in range(py-r, py+r+1):
        for x in range (px-r, px+r+1):
            if (y-py)**2 + (x-px)**2 <= r**2:
                gambar[y,x] = warna

#Jawaban tambahkan sumbu x dan y
def buat_garis(gambar, py1, px1, py2, px2, r, warna):
    py1 = round(py1)
    px1 = round(px1)
    py2 = round(py2)
    px2 = round(px2)

    jumlah_titik = max(abs(py2 - py1), abs(px2 - px1)) + 1

    for t in np.linspace(0, 1, jumlah_titik):
        py = round(py1 + t * (py2 - py1))
        px = round(px1 + t * (px2 - px1))

        buat_lingkaran(gambar, py, px, r,    warna
        )
#
def buat_kurva(gambar, m, n, o, warna, lw):
    hw = int(lw/2)
    for x in range(0+hw, kanvas_col_max-hw):          #ensuring no node crashes the canvas' margins
        y = round(m*x**2 + n*x + o)
        if y > 0+hw and y < kanvas_row_max-hw and x > 0+hw and x < kanvas_col_max-hw:
            py = y; px = x; r = hw
            buat_lingkaran(gambar, py, px, r, warna)

def konversi_koord_data_ke_koord_kanvas(y_data, x_data, data_y_min, data_y_max, data_x_min, data_x_max, \
                                        kanvas_row_min, kanvas_row_max, kanvas_col_min, kanvas_col_max, \
                                        margin_row, margin_col):
    ver_ratio = (kanvas_row_max-kanvas_row_min-2*margin_row)/(data_y_max-data_y_min)
    hor_ratio = (kanvas_col_max-kanvas_col_min-2*margin_col)/(data_x_max-data_x_min)
    y_kanvas = round(y_data * ver_ratio + margin_row)
    x_kanvas = round(x_data * hor_ratio + margin_col)
    return (y_kanvas, x_kanvas)

#MAIN PROGRAM
gambar = np.zeros(shape=(kanvas_row_max, kanvas_col_max, 3), dtype=np.uint8) #Create the canvas.

#Create dummy dataset x dan y and save them to a list.
data = []                                 #Buat satu list kosong.
for n in range(0, N):
    for x in range(data_x_min, data_x_max+1):
        y = a*x**3 + b*x**2 + c*x + d + random.uniform(-randval, randval)
        data.append((y,x))    #Simpan setiap nilai data (y dan x) ke dalam list.
np.save(nama_file, data)

#Show the data onto the kanvas
data = np.load(nama_file)
print(data)
print(len(data))
for i in range(0, len(data)):
    y_data, x_data = data[i][0], data[i][1]
    koordinat_kanvas = konversi_koord_data_ke_koord_kanvas(y_data, x_data, data_y_min, data_y_max, data_x_min, data_x_max, \
                                        kanvas_row_min, kanvas_row_max, kanvas_col_min, kanvas_col_max, \
                                        margin_row, margin_col)
    y_kanvas, x_kanvas = koordinat_kanvas[0], koordinat_kanvas[1]
    #print(i,y_data, x_data, y,x)
    if y_data >= a*x_data**3 + b*x_data**2 + c*x_data + d:
        buat_lingkaran(gambar, y_kanvas, x_kanvas, rn, warna_data1)
    if y_data < a*x_data**3 + b*x_data**2 + c*x_data + d:
        buat_lingkaran(gambar, y_kanvas, x_kanvas, rn, warna_data2)

#Show the curve; for now using the same equation as the dummy data generator.
line_coordinate = []
Iy = kanvas_row_max-kanvas_row_min - 2 * margin_row
Ix = kanvas_col_max-kanvas_col_min - 2 * margin_col
dy = (data_y_max - data_y_min) / Iy                               #Ini float.
dx = (data_x_max - data_x_min) / Ix                               #Ini float.
x = data_x_min - dx
for i in range(0, Ix):
    x = x + dx                    #Ini float.
    y = a*x**3 + b*x**2 + c*x + d #Ini float.
    line_coordinate.append((y,x))              #Simpan koordinat titik-titik pada garis.
    koordinat_kanvas = konversi_koord_data_ke_koord_kanvas(y, x, data_y_min, data_y_max, data_x_min, data_x_max, \
                                        kanvas_row_min, kanvas_row_max, kanvas_col_min, kanvas_col_max, \
                                        margin_row, margin_col)
    y_kanvas, x_kanvas = round(koordinat_kanvas[0]), round(koordinat_kanvas[1])
    buat_lingkaran(gambar, y_kanvas, x_kanvas, rl, warna_garis)

# Draw X-Axis and Y-Axis
# X-AXIS
# Y = 0
py_axis_x = konversi_koord_data_ke_koord_kanvas(data_y_min, data_x_min, data_y_min, data_y_max, data_x_min, data_x_max, kanvas_row_min, kanvas_row_max, kanvas_col_min, kanvas_col_max, margin_row, margin_col)[0]
buat_garis(gambar, py_axis_x, margin_col, py_axis_x, kanvas_col_max - margin_col, rl, warna_axis)

# Y-AXIS
# X = 0
px_axis_y = konversi_koord_data_ke_koord_kanvas( data_y_min, data_x_min, data_y_min, data_y_max, data_x_min, data_x_max, kanvas_row_min, kanvas_row_max, kanvas_col_min, kanvas_col_max, margin_row, margin_col)[1]
buat_garis(gambar, margin_row, px_axis_y, kanvas_row_max - margin_row, px_axis_y, rl, warna_axis)

# Tampilkan hasil di windownya Plt tanpa label apapun.
plt.figure(facecolor='black')
plt.axis('off')  # Matikan garis kartesius bawaan
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Hilangkan padding/margin
plt.imshow(gambar, origin='lower')
plt.show()