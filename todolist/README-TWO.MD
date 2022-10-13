Readme Tugas 6

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
- Pada asynchronus programming, program yang ingin diproses dalam waktu yang sama dapat dilakukan tanpa harus menunggu mengantri atau bisa dibilang tidak perlu adanya waktu tunggu akibat proses kode sebelumnya harus diselesaikan terlebih dahulu. Kita dapat menjalankan kode selanjutnya secara langsung. Dengan pemanggilan asynchronus programming, suatu sistem dapat melakukan pembaharuan tanpa harus direfresh atau dilakukan run ulang karena dengan asynchronus programming bisa menjalankan beberapa tugas secara bersamaan. 

- Pada synchronus programming, program dijalankan secara sequential, dimana program dijalankan secara terurut didasarkan pada antrian program yang ingin dieksekusi. Setiap fungsi synchronus dipanggil, proses fungsi tersebut  harus diselesaikan terlebih dahulu agar program dapat mengeksekusi kode selanjutnya. Pemanggilan function pun tidak dapat dilakukan secara bersamaan, hanya dapat dilakukan secara satu per satu.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
= Event-Driven Programming merupakan paradigma pemrograman yang didasarkan pada event. Suatu event dalam aplikasi akan menentukan jalannya program. Dengan event, akan terjadi tindakan / pesan dari user. Contoh event driven programming pada tugas ini adalah akan munculnya popup yang berupa modal dari halaman atas aplikasi saat user melakukan click tombol (button click) pada tombol Add New Task.

3.  Jelaskan penerapan asynchronous programming pada AJAX.
= Penerapan asynchronus programming pada AJAX telah dilakukan pada tugas 6 ini. Suatu proses AJAX akan dieksekusi saat sebuah event diberikan oleh user. Contohnya adalah saat user melakukan click tombol Add New Task, akan adanya pop up tempat user memasukkan todolist yang berisikan judul dan deskripsi. Setelah user mensubmit todo yang ditambahkan, todo tersebut akan langsung muncul pada halaman todolist user tanpa harus dilakukan refresh web.  

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Pertama, saya membuat fungsi baru bernama show_json dengan parameter request pada views.py. Fungsi tersebut akan melakukan pengembalian semua data dari task_list dalam JSON.

- Kedua, saya melakukan penambahan path('json/', show_json, name='show_json'), pada urlpatterns di urls.py. 

- Ketiga, saya mengambil data task_list dengan AJAX GET pada todolist.html yang diawali dengan "$.get..."

- Keempat pada bagian Ajax POST, saya membuat tombol Add Task untuk menampilkan modal dengan form sebagai tempat user menambahkan task dengan menggunakan modal yang tersedia pada bootstrap melalui link berikut https://getbootstrap.com/docs/4.0/components/modal/ dan saya tambah dalam todolist.html

- Kelima, saya membuat view baru untuk melakukan penambahan new task pada database dengan mengimplemenntasikan fungsi input_task pada views.py dengan parameter request. Didalamnya, banyak digunakan method get untuk mendapatkan data.

- Keenam, saya melakukan penghubungan antara form yang sudah saya buat pada modal dengan menambahkan kode potongan kode "$("msg")..." pada todolist.html.

- Ketujuh, saya menutup modal dan mengecek apakah modal sudah terimplementasikan pada program saya atau belum.