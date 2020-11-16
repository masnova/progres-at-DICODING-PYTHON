'''print(3+3)
print(6*7)
print(3**10)
print("hai nov")'''

# NUMBERS
'''a = 5
print(a, "is of type", type(a))
a = 2.0
print(a, "is of type", type(a))
a = 1+2j
print(a, "is complex number?", isinstance(1+2j, complex))
b = 0.1234567890123456789
print(b)'''

# deret fibonacci
'''x = [0]*10005  # inisialisasi array 0 sebanyak 10005; x[0]=0
x[1] = 1  # x[1]=1

for j in range(2, 10001):
    x[j] = x[j-1]+x[j-2]  # Fibonacci
print(x[10000])'''


# x[0] artinya mengambil elemen paling awal, dengan index 0 dari List x.
# x[5] artinya mengambil elemen dengan index 5 dari List x.
# x[-1] artinya mengambil elemen dengan index paling belakang ke-1 dari List x.
# x[3:5] artinya membuat list dari anggota elemen List x dengan index 3 hingga sebelum index 5 (tidak termasuk elemen dengan index 5, dalam hal ini hanya index 3-4).
# x[:5] artinya membuat list dari anggota elemen List x paling awal hingga sebelum index 5 (tidak termasuk elemen dengan index 5, dalam hal ini hanya index 0-4).
# x[-3:] artinya membuat list dari anggota elemen List x mulai index ke-3 dari belakang hingga paling belakang.
# x[1:7:2] artinya membuat list dari anggota elemen List x dengan index 1 hingga sebelum index 7, dengan "step" 2 (dalam hal ini hanya index 1, 3, 5).
'''x = [5,10,15,20,25,30,35,40]
print(x[5])
print(x[-1])
print(x[3:5])
print(x[:5])
print(x[-3:])
print(x[1:7:2])'''

# perubahan pada list
'''z = [1,2,3,4]
z[3]=5
print (z)

#kedua
x = [1,2,3]
x[2]=4
x.append(5)
print(x)'''

#Untuk menghapus item pada list, gunakan fungsi del.
'''binatang = ['kucing', 'rusa', 'badak', 'macan']
del binatang[3]
print(binatang)'''

#slicing pada string 
'''s = "Hello World!"
print(s[4]) 		#ambil karakter kelima dari string s
print(s[6:11]) 		#ambil karakter ketujuh hingga sebelas dari string s
s[5]="d" 		    #ubah karakter keenam dari string s menjadi "d", seharusnya gagal karena immutable
s = "Halo Dunia!"	#ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
print (s)'''

#set
'''you = {1,2,3,3,2}
print(you)'''

#Konversi (conversion, cast) antar tipe data
#(standard type) misalnya: int(), float(), str(), dll.
'''print(float(5))
print(int(10.6))
print(int(-10.6))
print(float('2.5'))
print(str(25))
print(int('1p')) #klo mau run ini hrs ditutup
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))'''

#Memasukkan nilai variabel pada string
'''y = 10
print('nilai mtk aku', y)

#print('hai {}'.format('bro'))

nama = "ehan"
umur = 12
print ("hei, %s!" %nama)
print ("Umurnya si %s adalah %d" % (nama,umur))

list = [7, 9, 11, 13]
print("List saya: %s" % list)

#Beberapa argument specifier yang umum digunakan:
#%s - String
#%d - Integers
#%f - Bilangan Desimal
#%.<digit>f - Bilangan desimal dengan sejumlah digit angka dibelakang koma.

#Contoh mencetak representasi Hexa (bilangan basis 16):
a, b = 14, 11
a, b
print('a: %x and b: %X' % (a, b))'''

#input()
'''nilai = input('masukan angka : ')
print(nilai)'''

#konversi dengan int() atau float() akan menghasilkan error. Anda dapat menggunakan fungsi eval() 
#yang sekaligus juga berfungsi menyelesaikan ekspresi matematika.
'''print(eval('90+10*5*+1-3+2-9'))'''

#Mengubah Huruf Besar/Kecil
#upper #lower
'''kalimat = 'hei you'
low =  'HEI YOU'
kalimat = kalimat.upper()
low = low.lower()
print(kalimat)
print(low)'''

#Awalan dan Akhiran
#rsteip() menghapus whitespace pada sebelah kanan string atau akhir string
'''print('Dicoding    '.rstrip())

#lstrip() menghapus whitespace pada sebelah kiri atau awal string
print('    Dicoding'.lstrip())

#strip() Metode strip() akan menghapus whitespace pada bagian awal atau akhir string. 
print('    Dicoding    '.strip())
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip('Code'))

#startswith() Metode startswith() akan mengembalikan nilai True jika string diawali dengan kata awalan tertentu yang 
# kita inginkan, jika tidak maka akan mengembalikan nilai False.
print('Dicoding Indonesia'.startswith('Hi'))

#endswith() Metode endswith() ini kebalikannya dari metode startswith(), metode ini akan mengembalikan nilai True jika 
# string diakhiri dengan kata akhiran tertentu yang kita inginkan, jika tidak maka akan mengembalikan nilai False. 
print('Dicoding Indonesia'.endswith('Ho'))

#join() Metode join() adalah metode yang dipakai untuk menggabungkan sejumlah string. 
print(' '.join(['masnova17', '.com', '!']))
print('123'.join(['Dicoding', 'Indonesia', '!']))'''

#split() Sebaliknya, metode split() adalah metode yang memisahkan substring berdasarkan delimiter tertentu (defaultnya 
#adalah whitespace, tab, atau newline).
'''print('Dicoding Indonesia !'.split())
#another ex
print('Dicoding123Indonesia123!'.split('123'))
#another ex Anda juga dapat menggunakan metode split() ini untuk memisahkan setiap baris pada string multiline:
print('''#Halo,
#aku ikan,
#aku suka sekali menyelam
#aku tinggal di perairan.
#Badanku licin dan renangku cepat.
#Senang berkenalan denganmu.'''.split('\n'))'''

#replace() mengembalikan string baru dalam kondisi substring telah tergantikan dengan parameter yang dimasukkan.
'''string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))
#another ex
string = "Ayo belajar Coding di Dicoding karena Coding adalah bahasa masa depan"
print(string.replace("Coding", "Pemrograman", 1))''' #angka 1 diilangin bakalan ubah semua kata coding

#isupper() akan mengembalikan nilai True jika semua huruf dalam string adalah huruf besar, dan akan mengembalikan 
#nilai False jika terdapat satu saja huruf kecil di dalam string tersebut.
'''kata = ‘DICODING’
kata.isupper()

kata = ‘Dicodng’
kata.isupper()'''

#islower() adalah kebalikan dari metode isupper(), metode ini akan mengembalikan nilai True jika semua huruf dalam 
# string adalah huruf kecil, dan akan mengembalikan nilai False jika terdapat satu saja huruf besar di dalam string tersebut.
'''kata = ‘dicoding’
kata.islower()'''
#another ex
'''print('Dicoding'.upper().lower())
print('Dicoding'.lower().upper())
print('DICODING'.upper().lower().islower())
print('DICODING'.upper().lower().isupper())'''

#isalpha() akan mengembalikan nilai True jika semua karakter dalam string adalah huruf alfabet, jika tidak maka akan mengembalikan nilai False.
'''print('nova'.isalpha())'''
#isalnum() nilai True jika karakter dalam string adalah alfanumerik yaitu hanya huruf atau hanya angka
'''print('nova123'.isalnum())'''
#isdecimal() engembalikan nilai True jika karakter dalam string berisi hanya angka/numerik
'''print('123'.isdecimal())'''
#isspace() nilai True jika string berisi hanya karakter whitespace, seperti spasi, tab, newline, atau karakter whitespaces lainnya,
'''print(' '.isspace())'''
#istitle() Metode ini akan mengembalikan True jika string berisi huruf kapital di setiap kata dan dilanjutkan dengan huruf kecil seterusnya
'''print('Nama ova'.istitle())'''

'''while True:
    print('Masukkan nama Anda:')
    name = input()
    if name.isalpha():
        print("Halo", name)
        break
    print('Masukkan nama Anda dengan benar.')'''

# zfill() Jika kita ingin menerapkan zfill pada data berupa angka, maka kita harus mengonversinya terlebih dahulu ke dalam bentuk string menggunakan str() seperti di bawah ini:
# Contoh 1: Penggunaan zfill 5 pada angka satuan
'''angka = 5
print (str(angka).zfill(5));
# Contoh 2: Penggunaan zfill 5 pada angka ratusan
angka = 300
print (str(angka).zfill(5));
# Contoh 3: Penggunaan zfill 5 pada angka desimal negatif (memiliki koma)
angka = -0.45
print (str(angka).zfill(5));
# Contoh 4: Penggunaan zfill 7 pada angka desimal negatif (memiliki koma)
angka = -0.45
print (str(angka).zfill(7));'''

#zfill() pd string
# Contoh 1
'''kata = 'aku'
print (kata.zfill(5));
# Contoh 2
kata = 'kamu'
print (kata.zfill(5));
# Contoh 3
kata = 'dirinya'
print (kata.zfill(5));'''

#rjust() Berikut penerapan rjust() dan contoh kodenya. Pembahasan lengkap akan dijelaskan di bawah setelah uraian kodenya ya.
'''print('nova'.rjust(20))
print('nova'.ljust(20))
print('nova'.ljust(20, '?'))
print('nova'.center(20))
print('nova'.center(20, '-'))'''

# string literals
'''print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")'''

#len() Salah satu fungsi yang paling bermanfaat untuk List atau String adalah len() yang akan menghitung panjang 
# atau banyaknya elemen dari List (untuk String menjadi menghitung jumlah karakternya).
'''contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(contoh_list)
print(len(contoh_list))
 
contoh_set = set([1, 3, 3, 5, 5, 5, 7, 7, 9])
print(contoh_set)
print(len(contoh_set))
 
contoh_string = "Belajar Python"
print(contoh_string)
print(len(contoh_string))'''

#min() dan max() nilai minimum dan maksimum dari suatu list menggunakan fungsi min() dan max().
'''angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))'''

#Count Untuk mengetahui berapa kali suatu objek muncul dalam list, Anda dapat menggunakan fungsi count().
'''genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))'''

#Penggabungan dan Replikasi Pada List juga dimungkinkan adanya penggabungan (+) dan replikasi (*).
'''angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
#versi tambah
gabung = angka + huruf
print(gabung)
#versi X 2
yangdikali = huruf * 2
print(yangdikali)
#another
satu = [1]*4
print(len(satu))
print(satu)'''

#range Fungsi range() memberikan deret bilangan dengan pola tertentu.
'''for i in range(1, 11):
    print(i)'''

'''for i in range(1, 11):
    print(i)'''

# in dan not in Fungsi ini akan mengembalikan nilai boolean True atau False.
'''kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)'''

#Memberikan nilai untuk multiple variable
'''data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]

data = ['shirt', 'white', 'L'] # From List
apparel, color, size = data
data = ('shirt', 'white', 'L')  # From Tuple
apparel, color, size = data
print(data)

apparel, color = 'shirt', 'white'
apparel, color = color, apparel
print(apparel)
print(color)'''

# Sort Sort Jika Anda ingin mengurutkan angka atau urutan huruf, maka Anda bisa menggunakan metode sort().
'''angka = [100, 1000, 500, 200, 600]
angka.sort()
print(angka)
# another EX
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)
#urutannya terbalik make reverse true
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)
print(kendaraan)'''

'''print(1-2)
a = 2
a *= 3
print(a)'''

# IF
'''kelerengku = 10
if kelerengku:
   print ("Cetak ini jika benar")
   print (kelerengku)'''

# ELSE 
'''tinggi_badan = int(input("Masukkan tinggi badan Anda : "))
if tinggi_badan>=160:
   print ("Silakan, Anda boleh masuk")
else:
   print ("Maaf, Anda belum boleh masuk")'''

'''bilangan = 4
if bilangan % 2 == 0:
    print('Bilangan {} adalah genap'.format(bilangan))
else:
    print('Bilangan {} adalah ganjil'.format(bilangan))'''

'''nilai = int(input("Masukkan nilai tugas Anda : "))
if nilai>80:
   print("Selamat! Anda mendapat nilai A")
   print("Pertahankan!")
elif nilai>70:
   print("Hore! Anda mendapat nilai B")
   print("Tingkatkan!")
elif nilai>60:
   print("Hmm.. Anda mendapat nilai C")
   print("Ayo semangat!")
else:
   print("Waduh, Anda mendapat nilai D")
   print("Yuk belajar lebih giat lagi!")'''

'''bilangan = 1
if bilangan > 0:
    print('Bilangan {} adalah positif'.format(bilangan))
elif bilangan < 0:
    print('Bilangan {} adalah negatif'.format(bilangan))
else:
    print('Bilangan {} adalah nol'.format(bilangan))'''

# FOR
'''for huruf in 'Dicoding':  # Contoh pertama
    print('Huruf: {}'.format(huruf))
 
flowers = ['mawar', 'melati', 'anggrek']
for flower in flowers:  # Contoh kedua
    print('Flower: {}'.format(flower))'''

'''flowers = ['mawar', 'melati', 'anggrek']
for index in range(len(flowers)):
    print('Bunga: {}'.format(flowers[index]))'''

# WHILE
'''count = 0
while (count < 7):
    print('Hitungannya adalah: {}'.format(count))
    count = count + 1'''

'''var = 1
while var == 1:  # This constructs an infinite loop
    num = input('Masukkan angka: ')
    print('Anda memasukkan angka: {}'.format(num))
 
 
while True:  # This constructs an infinite loop
    num = input('Masukkan angka: ')
    print('Anda memasukkan angka: {}'.format(num))'''

#Perulangan Bertingkat Ada kalanya Anda perlu untuk melakukan perulangan bertingkat, misalnya untuk 
#menghasilkan contoh print-out berikut:
'''for i in range(0, 6):
    for j in range(0, 6 - i):
        print('*', end='')
    print()'''

# BREAK Pernyataan break menghentikan perulangan kemudian keluar, dilanjutkan dengan mengeksekusi pernyataan 
# (statement) setelah blok perulangan. Salah satu penggunaannya yang paling sering adalah sebuah kondisi eksternal yang membutuhkan program untuk keluar dari perulangan.
'''for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))
    #contoh 2
for i in range (0,10):
    for j in range (0,10):
        if j>i:
            print()
            break
        else:
            print("*",end="")'''

#Continue Pernyataan continue akan membuat iterasi saat ini berhenti, kemudian melanjutkan ke iterasi berikutnya, mengabaikan pernyataan (statement) yang berada antara continue hingga akhir blok perulangan.
'''for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))'''


#Else setelah For
#Pada Python juga dikenal fungsi else setelah for. Fungsinya diutamakan pada perulangan yang bersifat pencarian - untuk memberikan jalan keluar program saat pencarian tidak ditemukan.
'''for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, ' adalah bilangan prima')'''

# Else setelah While
# Berbeda dengan Else setelah For, pada statement while, blok statement else akan selalu dieksekusi saat kondisi pada while menjadi salah.
'''n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")'''

'''n = 10
while n > 0:
    n = n - 1
    print(n)
else:
    print("Loop selesai")'''

# PASS adalah operasi bersifat Null (kosong), tidak ada yang terjadi saat ia dipanggil.
'''def sebuahfungsi():
    pass'''

'''import sys
data=''
while(data!='exit'):
    try:
        data=input('masukan sebuah integer (type exit to exit): ')
        print('got integer: {}'.format(int(data)))
    except:
        if data == 'exit':
            pass  # exit gracefully without prompt any error
        else:
            print('error: {}'.format(sys.exc_info()[0]))'''

#List Comprehension (membuat list dengan inline loop dan if)
#Ada kalanya Anda perlu untuk membuat sebuah list baru dari dengan sebuah operasi dari list sebelumnya. 
#Misalnya membuat nilai kuadrat dari semua item dalam list:
#Cara 1
'''angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print('hasilnya', pangkat)'''

#Cara 2 List Comprehension
'''angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)'''

# memanggil fungsi : Mendefinisikan sebuah fungsi hanya memberikan namanya, menentukan parameter yang ingin 
# menjadi bagian dari fungsi dan struktur dasar kode tersebut. Setelah struktur dasar terpenuhi, Anda dapat memanggilnya 
# pada fungsi yang lain atau dari Python prompt.
'''def cetak( param1 ):
    print(param1)
    return
 
#panggil
cetak("Panggilan Pertama")
cetak("Panggilan Kedua")'''

# Return
# Pernyataan return [expression] akan membuat eksekusi program keluar dari fungsi saat itu, sekaligus mengembalikan 
# nilai tertentu. Nilai return yang tidak mengembalikan (ekspresi) nilai bersifat sama dengan contoh di bawah ini. 
'''def kali(angka1, angka2):
    # Kalikan kedua parameter
    hasil = angka1 * angka2
    print('Dicetak dari dalam fungsi: {}'.format(hasil))
    return hasil
 
# Panggil fungsi kali
keluaran = kali(10, 20);
print('Dicetak sebagai kembalian: {}'.format(keluaran))'''

'''kumpulan_angka = [5, 8, 10, 12, 15, 17, 19, 25, 32, 42, 55, 75, 80, 88, 92, 99, 102, 120]
for angka in kumpulan_angka:
    if (angka > 99):
        break
    if(angka %% 3 == 0):
        print(angka)'''

'''kumpulan_angka = [5, 8, 10, 12, 15, 17, 19, 25, 32, 42, 55, 75, 80, 88, 92, 99, 102, 120]
for angka in kumpulan_angka:
    if (angka > 99):
        break
    if(angka % 3 == 0):
        print(angka)'''

'''kumpulan_angka = [5, 8, 10, 12, 15, 17, 19, 25, 32, 42, 55, 75, 80, 88, 92, 99, 102, 120]
for angka in kumpulan_angka:
    if(angka % 3 == 0):
        print(angka)'''

'''a = 'ABC'.join(['Dicoding', '', 'Indonesia'])
print(a)'''

'''class Kalkulator:
    """contoh kelas kalkulator sederhana"""
 
    def f(self):
        return 'hello world'
 
    @staticmethod
    def kali_angka(angka1, angka2):
        return '{} x {} = {}'.format(angka1, angka2, angka1 * angka2)
    
    k = Kalkulator()
    a = k.kali_angka(2, 3)
    print(a)'''

x = 'hello'
print(type(x))