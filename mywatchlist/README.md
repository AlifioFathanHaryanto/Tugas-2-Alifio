Readme Tugas 3

README TUGAS 3

Link deploy = https://aplikasi-fio.herokuapp.com/mywatchlist/

1.	Jelaskan perbedaan antara JSON, XML, dan HTML!
Berikut adalah perbedaan antara ketiganya:
-	JSON 
Kepanjangan : JavaScript Object Notation 
Ekstensi file : .json
Struktur: Terdiri atas dua bagian, yaitu kumpulan nilai / value yang berpasangan (ex: objek) dan kumpulan dari nilai/value yang terurut. 
Cara Kerja: Elemen-elemen dari JSON disimpan dengan efisien, namun tidak dikemas secara rapi untuk dibaca. 
Fungsionalitas: JSON dapat dipakai untuk melakukan pengiriman data melalui penguraian data, lalu mengirimkannya via internet. 

-	XML 
Kepanjangan : Extensible Markup Language 
Ekstensi file : .xml
Strukturnya : Terdiri atas 3 bagian, yaitu deklarasi, atribut, serta elemen. 
Cara Kerja : Elemen-elemen dari XML disimpan secara terstruktur dan sistematis sehingga dapat terbaca dengan mudah, namun XML menyimpan elemen-elemennya dengan kurang efisien. 
Fungsionalitas : Dengan keunggulannya pada data yang sistematis, pengguna dari XML bisa memakainya untuk memberikan catatan. XML biasa dipakai untuk melakukan penyederhanaan terhadap pertukaran serta penyimpanan data. Fokus utama dari XML adalah dalam proses transfer data.  

-	HTML 
Kepanjangan : HyperText Markup Language
Ekstensi file : .html atau .htm
Cara Kerja : HTML dapat kita open menggunakan search engine.
Strukturnya : Terdiri atas empat bagian utama, yaitu DOCTYPE (Document Type Declaration), tag <html>, tag <head>, dan tag <body>. 
Fungsionalitas : HTML biasa dipakai untuk membangun / membuat website yang dapat kita akses melalui internet. HTML akan memudahkan proses penyusunan bagian kalimat penjelasan dan heading pada website yang sedang dibuat. Fokus utama dari HTML adalah menyajikan data dengan baik.

2.	Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dibutuhkan dalam pengimplementasian sebuah platform untuk melakukan pengiriman data antar stack. Data tersebut berupa format data yang terdapat berbagai macam jenis, seperti yang saya pelajari yaitu JSON, XML, dan HTML. Setiap format data tersebut memiliki karakteristik tersendiri sesuai dengan yang telah saya jelaskan pada nomor 1.

3.	Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Dalam mengimplementasikan seluruh checklist di atas, hal pertama yang saya lakukan adalah membuat new app pada folder proyek Django tugas 2 dengan nama mywatchlist. Saya membuat aplikasi baru dengan memberikan perintah python manage.py startapp mywatchlist. Lalu, saya melakukan penambahan path mywatchlist. Kemudian, saya membuat model mywatchlist pada models.py dengan atribut watched (bertipe charField), title (bertipe charField), rating (bertipe IntegerField), release_date (bertipe CharField), dan review (bertipe TextField). Lalu, saya menambahkan 10 data mengenai objek MyWatchList tadi yang berisikan data dan review dari film pada file json yang saya letakkan di dalam folder fixtures. Setelah itu, saya melakukan manage.py runserver untuk melihat apakah html saya sudah berhasil terbuat pada internet yang saya akses melalui search engine. Setelah HTML tersebut berhasil ditampilkan, saya lanjutkan dengan menyajikan data dengan format XML dan JSON mengikutin Langkah-langkah pada lab 2.
Dalam menyajikan data dengan format XML dan JSON, hal pertama yang saya lakukan adalah membuat fungsi untuk menerima paramenter request pada views.py di folder mywatchlist. Lalu, saya melakukan import HttpResponse dan Serializer dari Django. Kemudian, saya membuat variabel pada fungsi tersebut bernama data sebagai penyimpan data hasil query. Lalu, saya melakukan return function dengan serialisasi (disesuaikan dengan formatnya, “xml” / “json”) dengan parameter data dan melakukan import fungsi yang sudah saya buat pada urls.py (disesuaikan dengan formatnya, show_json / show_xml). Terakhir, saya menambahkan path url dan dilanjutkan dengan memberikan perintah  python manage.py runserver untuk mengecek keberhasilan penyajian data dengan mengakses (http://localhost:8000/mywatchlist/xml/) atau (http://localhost:8000/mywatchlist/json/ ) di internet dengan search engine yang sudah saya download.


Referensi :
https://www.dicoding.com/blog/apa-itu-json/
https://www.dicoding.com/blog/apa-itu-xml/#:~:text=XML%20sendiri%20merupakan%20markup%20language,deklarasi%2C%20atribut%2C%20dan%20elemen.  
https://www.exabytes.co.id/blog/perbedaan-xml-dan-html/#:~:text=Kelebihan%20XML,-Beberapa%20Keunggulan%20XML&text=XML%20membuat%20dokumen%20dapat%20diangkut,Ini%20menyederhanakan%20proses%20perubahan%20platform. 
