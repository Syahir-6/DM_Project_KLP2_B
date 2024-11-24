from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Membaca data dengan delimiter yang benar
data = pd.read_csv('dataset.csv', delimiter=';')

# 1. Periksa nilai kosong
missing_values = data.isnull().sum()
print("Jumlah nilai kosong pada setiap kolom:")
print(missing_values[missing_values > 0])  # Tampilkan hanya kolom dengan nilai kosong

# 2. Isi nilai kosong (jika ada)
for column in data.columns:
    if data[column].dtype == 'object':  # Untuk kolom kategori
        if data[column].isnull().any():
            data[column] = data[column].fillna(data[column].mode()[0])  # Isi dengan mode
    else:  # Untuk kolom numerik
        if data[column].isnull().any():
            data[column] = data[column].fillna(data[column].mean())  # Isi dengan mean

# 3. Deteksi dan hapus duplikat
initial_rows = data.shape[0]
data.drop_duplicates(inplace=True)
final_rows = data.shape[0]
duplicates_removed = initial_rows - final_rows
print(f"Jumlah duplikat yang dihapus: {duplicates_removed}")

# 4. Normalisasi kolom numerik
numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
if not numeric_columns.empty:
    scaler = MinMaxScaler()
    data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

    # Format angka menjadi 2 desimal dengan apply
    data[numeric_columns] = data[numeric_columns].apply(lambda x: x.round(2))

# Tampilkan 5 data teratas setelah normalisasi
pd.set_option('display.float_format', '{:.2f}'.format)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print("\n5 data teratas setelah normalisasi:")
print(data.head())

# Menyimpan hasil ke file CSV baru
output_file = 'dataset_cleaned.csv'
data.to_csv(output_file, index=False, sep=';')  # Simpan dengan delimiter yang sesuai
print(f"\nHasil data telah disimpan di file: {output_file}")
