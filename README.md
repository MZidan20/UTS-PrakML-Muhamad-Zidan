# UTS-PrakML-Muhamad-Zidan
Praktikum Machine Learning Kelas A (1227050079)
Silahkan download dataset berikut: https://www.kaggle.com/datasets/joshmcadams/oranges-vs-grapefruit
Sebagai informasi data tersebut dataset yang terdapat identifikasi sebagai buah jeruk ataupun anggur. Sehingga tugas kalian adalah membuat model untuk melakukan klasifikasi apakah buah tersebut merupakan jeruk atau anggur.

# 1. Lakukan Import Library
<img width="246" alt="image" src="https://github.com/user-attachments/assets/106257c3-12c8-4f22-8ca3-f581b2818581" />

# 2. Load Dataset
Membaca data citrus dari file CSV . <br>
<img width="172" alt="image" src="https://github.com/user-attachments/assets/c858849d-1368-4113-86cb-2b48199dd935" />

# 3. Eksplorasi Data
Menampilkan informasi umum pada csv.<br>
<img width="274" alt="image" src="https://github.com/user-attachments/assets/32fa951b-65de-4ec4-95b1-29617b3587e0" />

# 4. Label Kategori Ukuran
Mengelompokkan data menjadi tiga kategori ukuran (small, medium, large) berdasarkan berat.

# 5. Visualisasi Data
Membuat visualisasi pairplot untuk melihat hubungan antar fitur berdasarkan kategori ukuran. <br>
![image](https://github.com/user-attachments/assets/c941daf7-8515-4589-bdac-4f059286c99b)

# 6. Persiapan Data untuk Model
X = citrus[['diameter', 'weight', 'red', 'green', 'blue']]
y = citrus['size_category']
Memisahkan fitur dan label untuk proses pelatihan model.

# 7. Split Data
X_train, X_test, y_train, y_test = train_test_split(...)
Membagi data menjadi data latih dan uji (70:30) agar model bisa dievaluasi dengan data yang belum dilihat.

# 8. Train Model
Membuat dan melatih model Decision Tree untuk klasifikasi kategori ukuran. <br>
<img width="197" alt="image" src="https://github.com/user-attachments/assets/7b082281-df7f-486d-b9cd-a8d1ccad6b2f" />

# 9.  Evaluasi Model
Menampilkan metrik evaluasi (precision, recall, f1-score) dan matriks kebingungan untuk menilai kinerja model. <br>
<img width="227" alt="image" src="https://github.com/user-attachments/assets/caea9390-14c0-4717-90ae-bbdf288ff19f" />

# 10. Confusion Matrix <br>
<img width="235" alt="image" src="https://github.com/user-attachments/assets/429e10e7-49ee-4482-b0ab-a51ab1fa0312" />

# 11. Visualisasi Decision Tree
Menampilkan struktur pohon keputusan yang telah dilatih untuk interpretasi logika klasifikasi. <br>
<img width="350" alt="image" src="https://github.com/user-attachments/assets/0d7e25d7-d86e-48b7-a139-e51219cad69d" />

# 12. Example prediction
Menguji model dengan data buah baru untuk memprediksi ukurannya.
Prediction for sample orange: small









