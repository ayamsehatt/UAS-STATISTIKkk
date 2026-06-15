import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. MEMBACA DATA
df = pd.read_csv("statistik_populasi_sulteng.csv")

print("=" * 50)
print("ANALISIS STATISTIK POPULASI SULAWESI TENGAH")
print("=" * 50)

print("\n=== 5 BARIS PERTAMA ===")
print(df.head())

print("\n=== INFORMASI DATA ===")
print(df.info())

print("\n=== STATISTIK DESKRIPTIF ===")
print(df.describe())

# 2. TOTAL POPULASI
total_populasi = df["populasi_ribu"].sum()

print("\n=== TOTAL POPULASI ===")
print(f"Total Populasi : {total_populasi:,.2f} ribu jiwa")

# 3. POPULASI TERBESAR DAN TERKECIL
terbesar = df.loc[df["populasi_ribu"].idxmax()]
terkecil = df.loc[df["populasi_ribu"].idxmin()]

print("\n=== POPULASI TERBESAR ===")
print(terbesar[["kabupaten_kota", "populasi_ribu"]])

print("\n=== POPULASI TERKECIL ===")
print(terkecil[["kabupaten_kota", "populasi_ribu"]])

# 4. GRAFIK POPULASI
plt.figure(figsize=(10,6))

sns.barplot(
data=df,
x="kabupaten_kota",
y="populasi_ribu"
)

plt.title("Populasi Penduduk Kabupaten/Kota Sulawesi Tengah")
plt.xlabel("Kabupaten/Kota")
plt.ylabel("Populasi (Ribu Jiwa)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("grafik_populasi.png")
plt.show()

print("Grafik Populasi berhasil disimpan!")

# 5. GRAFIK KEPADATAN
plt.figure(figsize=(10,6))

sns.barplot(
data=df,
x="kabupaten_kota",
y="kepadatan_jiwa_km2"
)

plt.title("Kepadatan Penduduk Kabupaten/Kota")
plt.xlabel("Kabupaten/Kota")
plt.ylabel("Jiwa per Km²")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("grafik_kepadatan.png")
plt.show()

print("Grafik Kepadatan berhasil disimpan!")

# 6. LAJU PERTUMBUHAN
plt.figure(figsize=(10,6))

sns.barplot(
data=df,
x="kabupaten_kota",
y="laju_pertumbuhan_pct"
)

plt.title("Laju Pertumbuhan Penduduk")
plt.xlabel("Kabupaten/Kota")
plt.ylabel("Persentase (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("grafik_pertumbuhan.png")
plt.show()

print("Grafik Pertumbuhan berhasil disimpan!")

# 7. KESIMPULAN
print("\n")
print("=" * 50)
print("KESIMPULAN")
print("=" * 50)
print(f"Jumlah Data Kabupaten/Kota : {len(df)}")
print(f"Total Populasi             : {total_populasi:,.2f} ribu jiwa")
print(f"Populasi Terbesar          : {terbesar['kabupaten_kota']}")
print(f"Populasi Terkecil          : {terkecil['kabupaten_kota']}")
print("=" * 50)
