https://aplikasi-fio.herokuapp.com/todolist/login/ 
https://aplikasi-fio.herokuapp.com/todolist/ 

1.  Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
INLINE CSS
Tempat pengimplementasian : Langsung pada tag elemen HTML yang ingin diubah. 
Fungsi umum : Biasanya Inline CSS hanya digunakan untuk mengaplikasikan style hanya pada satu elemen (spesifik).
Kelebihan : Pengimplementasiannya sangat cepat ketika kita hanya ingin mengubah / mencocokkan style perubahan pada satu elemen HTML yang kita inginkan. 
Kekurangan : Sangat tidak efisien ketika digunakan untuk merubah style pada elemen HTML yang banyak seperti pada proyek dengan skala besar karena pengimplementasiannya bisa pada setiap satu elemen HTML.

- INTERNAL CSS
Tempat pengimplementasian : Langsung di dalam tag '<style>' pada file CSS yang sama dengan file HTML (pada file HTML).
Fungsi umum : Menciptakan interface pada sebuah halaman web yang unik, dimana interface tersebut tidak diimplementasikan di halaman website kita yang lain .
Kelebihan : Cocok digunakan untuk membuat tampilan yang berbeda dari halaman lain. Lalu, HTML dan CSSnya berlokasi pada file yang sama, sehingga kita tidak perlu mengunggah beberapa file. Tak hanya itu, ID serta Class pada internal CSS dapat digunakan oleh internal stylesheet.
Kekurangan : Sangat tidak efektif dan efisien saat kita ingin membuat website dengan banyak halaman yang menggunakan style CSS sama (menggunakan style CSS yang sama pada file-file HTML lain). Lalu, penggunaan internal CSS juga mengakibatkkan performa website kita cenderung lambat.

- EXTERNAL CSS
Tempat pengimplementasian : Pada file CSS yang terpisah/berbeda dengan file HTML. File tersebut merupakan file khusus dengan ekstensi ".css".
Fungsi umum : Mengaplikasikan CSS pada banyak halaman website sekaligus.
Kelebihan : Sangat efektif untuk digunakan dalam mengatur CSS pada proyek besar yang tiap halamannya ingin mengimplementasikan CSS yang identik. Lalu, durasi loading pengaksesan website kita juga lebih singkat.
Kekurangan : Koneksi internet user yang lambat dapat menyebabkan file CSS mengalami kegagalan pemanggilan oleh file HTML. Hal ini menyebabkan tampilan halaman website kita yang banyak mengimplementasikan file CSS tersebut menjadi berantakan.

2. Jelaskan tag HTML5 yang kamu ketahui.
- <!DOCTYPE html> = Berperan dalam pendeklarasian / pendefinisian untuk melakukan identifikasi mengenai jenis dokumen HTML yang kita gunakan.
- <html>..</html> = Berperan dalam melakukan root, dimana seluruh tag pada tag <HTML> adalah gambaran dokumen HTML atau bisa disebut juga sebagai tag pembuka dalam pembuatan dokumen html. 
- <title>..</title> = Berfungsi untuk pembuatan judul pada halaman web, biasanya tulisannya akan tampil dengan font berukuran besar.
- <head>..</head> = Berfungsi sebagai meta information mengenai dokumen. Pada tag ini, kita dapat menambahkan tag yang berisi informasi penulis, informasi key word dari dokumen, dan lainnya.
- <body>..</body> = Sebagai tempat pembuatan/pendefinisian konten-konten website dengan HTML.

3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- Selektor tag, berperan dalam melakukan pemilihan elemen. Contohnya:
p {
    color: greem;
}

- Selektor class, berperan dalam melakukan pemilihan elemen sesuai dengan nama class yang diberikan. Ciri khasnya adalah tanda titik pada bagian depan selektor class. Contoh:
.blue {
    color: grey;
    background: blue;
    padding: 15px;
}

- Selektor ID, selektor ini bersifat unik karena hanya dapat digunakan hanya oleh sebuah elemen. Ciri khas dari selektor ID adalah penggunaan '#' pada bagian depan selektor ID.  Contoh:
#header {
    background: teal;
    color: blue;
    height: 150px;
    padding: 75px;
}

- Selektor Atribut, selektor ini melakukan pemilihan elemen sesuai dengan atribut. Contoh:
input[type=text] {
    background: none;
    color: blue;
    padding: 50px;
    border: 2px solid blue;
}

- Selektor Universal, selektor ini berperan dalam penyeleksian seluruh elemen yang berada pada scope yang didefinisikan. Contoh:
* {
    border: 2px solid blue;
}
Dari kode tersebut didapatkan bahwa seluruh elemennya akan mempunyai garis 'solid' berukuran 2 px yang warnanya adalah biru.

- Selektor pseudo, selektor ini berperan dalam pemilihan elemen semu, yaitu pada state di elemen. Contohnya saat melakukan click atau hover.
hover {
    ...
}

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Terdapat beberapa langkah yang saya lakukan dalam mengimplementasikan checklist di atas.
- Saya meletakkan link rel, href, dan script src pada base.html
- Lalu, saya membuat Navbar dengan warna hijau yang cukup tua, lalu dikombinasikan dengan warna hijau muda dari background website. Untuk menentukan kombinasi warna yang cocok, saya menggunakan colour palette pada website https://colorhunt.co/palette/fcf8e894b49fecb390df7861 . Semua hal tersebut saya implementasikan pada create_task.html , login.html , register.html , todolist.html
- Kemudian, saya mulai memindahkan beberapa elemen dan tabel ke tengah. Lalu, table tersebut saya isi dengan data dummy karena program saya tidak dapat memunculkan data yang diinput user. Kemudian saya menambahkan margin-bottom sebesar 20 px pada table tersebut agar tidak terlalu dekat dengan cards.
- Lalu, saya mengimplementasikan cards pada todolist.html yang berisikan data-data dummy.
- Kemudian, saya menambahkan emoticon pada beberapa halaman html yang referensinya saya ambil pada website berikut https://www.w3schools.com/charsets/ref_emoji.asp
- Setelah tampilan dari seluruh halaman HTML telah sesuai dengan tampilan yang saya inginkan, saya memastikan kembali bahwa websitenya sudah responsif dengan mengecilkan tampilan search engine yang saya gunakan melalui metode minimize dan split screen.
- Setelah itu, saya melakukan push dan deploy aplikasi.

Referensi :
https://www.niagahoster.co.id/blog/perbedaan-internal-external-dan-inline-css/
https://www.petanikode.com/css-dalam-html/ 
https://codepolitan.com/blog/pengenalan-html5-belajar-html 
https://www.petanikode.com/css-selektor/ 










