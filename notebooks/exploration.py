"""
SenSante - Exploration du dataset patients_dakar.csv
Lab 1 : Git, Python et Structure Projet
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

# chemin absolu basé sur l'emplacement du script
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "../data/patients_dakar.csv.xlsx")

df = pd.read_excel(file_path)



# ===== PREMIERS APERÇUS =====
print("=" * 50)
print("SENSANTE - Exploration du dataset")
print("=" * 50)

# Dimensions du dataset
print(f"\nNombre de patients : {len(df)}")
print(f"Nombre de colonnes : {df.shape[1]}")
print(f"Colonnes : {list(df.columns)}")

# Aperçu des 5 premières lignes
print("\n--- 5 premiers patients ---")
print(df.head())

# ===== STATISTIQUES DE BASE =====
print("\n--- Statistiques descriptives ---")
print(df.describe().round(2))

# ===== REPARTITION DES DIAGNOSTICS =====
print("\n--- Répartition des diagnostics ---")
diag_counts = df["diagnostic"].value_counts()
for diag, count in diag_counts.items():
    pct = count / len(df) * 100
    print(f"{diag:12s} : {count:3d} patients ({pct:.1f}%)")

# ===== REPARTITION PAR REGION =====
print("\n--- Répartition par région (top 5) ---")
region_counts = df["region"].value_counts().head(5)
for region, count in region_counts.items():
    print(f"{region:15s} : {count:3d} patients")

# ===== TEMPERATURE MOYENNE PAR DIAGNOSTIC =====
print("\n--- Température moyenne par diagnostic ---")
temp_by_diag = df.groupby("diagnostic")["temperature"].mean()
for diag, temp in temp_by_diag.items():
    print(f"{diag:12s} : {temp:.1f} °C")

print("\n" + "=" * 50)
print("Exploration terminée !")
print("Prochain lab : entraîner un modèle ML")
print("=" * 50)

# Répartition des diagnostics
df['diagnostic'].value_counts().plot(kind='bar', color=['green','red','blue','orange'])
plt.title("Répartition des diagnostics")
plt.xlabel("Diagnostic")
plt.ylabel("Nombre de patients")
plt.show()

for diag, color in zip(['sain','paludisme','grippe','typhoïde'], ['green','red','blue','orange']):
    subset = df[df['diagnostic'] == diag]
    plt.hist(subset['temperature'], bins=20, alpha=0.5, label=diag, color=color)

plt.title("Température par diagnostic")
plt.xlabel("Température (°C)")
plt.ylabel("Fréquence")
plt.legend()
plt.show()

# Top 5 régions
df['region'].value_counts().head(5).plot(kind='bar', color='purple')
plt.title("Top 5 régions")
plt.xlabel("Région")
plt.ylabel("Nombre de patients")
plt.show()

