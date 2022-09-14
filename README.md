Link deploy = https://aplikasi-fio.herokuapp.com/katalog/  

1. ![Bagan_Alifio](/Bagan_Alifio.jpg)

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment digunakan sebagai alat pembatas / pemisah virtual python environment agar tidak dapat diakses langsung dari luar / tanpa perantara. Virtual environment bersifat spesifik pada sebuah proyek. Dengan itu, kita dapat menjalankan proyek yang telah kita buat pada setiap versi Django yang terunduh pada laptop kita.

Contoh : Saat kita dapat mengerjakan sebuah proyek pada Django 4.1.1 dengan baik, kemudian beberapa saat kemudian muncul versi 4.1.2. Setelah kita melakukan upgrade ke versi 4.1.2, virtual environment berperan dalam menjaga agar setiap aplikasi memiliki modulnya sendiri. Dengan itu, aplikasi yang kita buat saat versi Django di laptop kita adalah 4.1.1 akan masih dapat dijalankan walaupun kita sudah mengunduh Django versi 4.1.2 akibat adanya pemisahan modul.

Tanpa menggunakan virtual environment, kita masih tetap bisa membuat / mengembangkan aplikasi web berbasis Django. Namun, proyek yang kita buat akan kemungkinan besar bermasalah saat dijalankan dengan Django versi lain dari yang dipakai saat awal mengembangkan aplikasi. Hal tersebut terjadi karena tanpa virtual environment, proyek yang sudah kita kembangkan tersebut tidak bisa beradaptasi pada Django versi lain. Lalu, modul aplikasi yang kita gunakan dalam mengembangkan aplikasi juga bisa diakses dari luar, sehingga aplikasi-aplikasi lain memiliki akses terhadap modul tersebut. Maka, pemakaian virtual environment merupakan hal yang sangat penting dalam mengembangkan apikasi web dengan basis Django.

referensi : https://code.tutsplus.com/id/tutorials/understanding-virtual-environments-in-python--cms-28272

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

Terdapat beberapa cara yang saya lakukan untuk mengimplementasikan instruksi 1-4. 
- Pertama, diawali dengan membuat repositori baru bernama Tugas-2-Alifio dan melakukan clone repository ke perangkat saya untuk mendapatkan template yang akan saya gunakan. 
- Kedua, saya membuka folder hasil clone tersebut di VsCode dan mulai mengerjakannya dari views.py. Mirip seperti lab 1, saya membuat fungsi show_katalog untuk menerima parameter request. Lalu, saya menampung data query pada variabel data_barang_katalog. Pada context, saya menambahkan nama dan NPM saya. Terakhir, saya melakukan return render(request, "katalog.html", context) untuk melakukan mapping ke katalog.html
- Ketiga, saya melakukan routing terhadap views.py pada fungsi urls.py di folder template dengan memanggil fungsi show_katalog untuk menghubungkan antara HTML dan web browser. 
- Keempat, saya melakukan mapping data-data yang sudah di-render di views.py agar dapat menampilkannya pada halaman HTML. Mapping tersebut saya lakukan pada katalog.html yang ada di folder templates untuk menampilkan Item Name, Item Price, Item Stock, Rating, Description, dan Item URL. Lalu, saya mengiterasi variabel list_katalog untuk menampilkan daftar data tersebut di tabel. Dilanjutkan dengan memanggil setiap variabel spesifik dari objek-objek pada list_katalog yang merupakan kontainer. 
- Kelima, saya mengaktifkan environment pada CMD, melakukan migration, loaddata, dan menjalankan proyek dengan melakukan python manage.py runserver. Setelah itu, saya mengecek ke web http://localhost:8000/katalog/ apakah web sudah dapat menampilkan data-data sesuai soal.
- Keeenam, saya melakukan deploy ke aplikasi Heroku. Diawali dengan melakukan git add-commit-push. Lalu, saya melakukan copy API key akun Heroku saya dan memasukkannya ke menu secret di Github. Terakhir, saya melakukan re-run worlkflow yang tadinya gagal.
