import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file dengan delimiter yang sesuai
file_path = '_supermarket.csv'
data = pd.read_csv(file_path, delimiter=';')

# Tampilkan lima baris pertama
print("5 baris pertama dari data:")
print(data.head())

# b. Periksa struktur dataset
print("\nInformasi Data:")
print(data.info())

# Periksa nilai kosong
print("\nNilai Kosong:")
print(data.isnull().sum())

print(data.describe())
# Isi nilai kosong pada kolom numerik dengan mean dan kategori dengan mode
for column in data.columns:
    if data[column].dtype == 'object':
        # Isi kolom kategori dengan mode (nilai terbanyak)
        data[column] = data[column].fillna(data[column].mode()[0])
    else:
        # Isi kolom numerik dengan rata-rata (mean)
        data[column] = data[column].fillna(data[column].mean())


# f. Normalisasi kolom numerik

# Simpan data yang telah diproses ke CSV baru dengan pemisah yang sesuai
# data.to_csv('_supermarket.csv', index=False, sep=';')


# Membersihkan kolom 'gross margin percentage' (menghapus karakter yang tidak sesuai dan mengonversi ke float)
data['gross margin percentage'] = (
    data['gross margin percentage']
    .str.replace('.', '', regex=False)
    .astype(float)
    .fillna(data['gross margin percentage'].mode()[0])
)

# Visualisasi awal: distribusi rating
plt.figure(figsize=(10, 6))
sns.histplot(data['Rating'], bins=20, kde=True, color='blue')
plt.title('Distribusi Rating Produk', fontsize=14)
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Frekuensi', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Visualisasi: Jumlah transaksi per kategori produk
plt.figure(figsize=(12, 7))
sns.countplot(data=data, y='Product line', order=data['Product line'].value_counts().index, palette='viridis')
plt.title('Jumlah Transaksi per Kategori Produk', fontsize=14)
plt.xlabel('Jumlah Transaksi', fontsize=12)
plt.ylabel('Kategori Produk', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Visualisasi: Boxplot berdasarkan kategori produk untuk kolom numerik
plt.figure(figsize=(15, 10))

# Kolom numerik untuk boxplot
numeric_columns = ['Unit price', 'Quantity', 'Tax 5%', 'Total', 'gross income', 'Rating']

# Iterasi untuk membuat subplot boxplot
for i, column in enumerate(numeric_columns, 1):
    plt.subplot(2, 3, i)  # Grid 2x3
    sns.boxplot(data=data, x='Product line', y=column, palette='coolwarm')
    plt.title(f'{column} by Product line', fontsize=12)
    plt.xlabel('Product line', fontsize=10)
    plt.ylabel(column, fontsize=10)
    plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
