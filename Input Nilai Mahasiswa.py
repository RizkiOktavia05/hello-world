#!/usr/bin/env python
# coding: utf-8

# In[1]:

#Input Nilai Mahasiswa

nama_file = str(input('input nama fle : '))
daftar_nama_mhs  = []
daftar_nilai_mhs = []
jumlah_mhs = int(input('banyak mahasiswa : '))
print()

def nilai_akhir (nilai_tugas,nilai_uts,nilai_uas):
    NA = 0.15*nilai_tugas + 0.35*nilai_uts + 0.50*nilai_uas
    return NA

def index(NA) :
    if (NA >= 80 and NA <= 100):
        return 'A'
    elif (NA >= 70 and NA < 80):
        return 'B'
    elif (NA >= 55 and NA < 70):
        return 'C'
    elif (NA >= 40 and NA < 55):
        return 'D'
    elif (NA >= 0 and NA < 40):
        return 'E'
    else:
        return 'error'

for i in range(1, jumlah_mhs+1):
    nama_mhs    = str(input('Nama Mahasiswa %i        = ' %(i)))
    nilai_tugas = int(input('Nilai Tugas Mahasiswa %i = ' %(i)))
    nilai_uts   = int(input('Nilai UTS Mahasiswa %i   = ' %(i)))
    nilai_uas   = int(input('Nilai UAS Mahasiswa %i   = ' %(i)))
    print()

    NA = nilai_akhir(nilai_tugas,nilai_uts,nilai_uas)
    Index = index(NA)
    daftar_nilai_mhs.append([nama_mhs,nilai_tugas,nilai_uts,nilai_uas,NA,Index])
    daftar_nama_mhs.append(nama_mhs)

with open('%s.txt' %nama_file, 'w') as f:
    for j in range (len(daftar_nama_mhs)):
        f.write('%s.' %(j+1) + '\n')
        f.write('Nama Mahasiswa : %s' % daftar_nilai_mhs[j][0] + '\n')
        f.write('Nilai Tugas    : %.2f' % daftar_nilai_mhs[j][1] + '\n')
        f.write('Nilai UTS      : %.2f' % daftar_nilai_mhs[j][2] + '\n')
        f.write('Nilai UAS      : %.2f' % daftar_nilai_mhs[j][2] + '\n')
        f.write('Nilai Akhir    : %.2f' % daftar_nilai_mhs[j][4] + '\n')
        f.write('Nilai Indeks   : %s' % daftar_nilai_mhs[j][5] + '\n')
        f.write('\n')


# In[ ]:




