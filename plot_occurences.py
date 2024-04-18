import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

path = "data/ue_metrics_1_2.csv"
df = pd.read_csv(path, delimiter=";")
print(df["cfo"], df["dl_snr"])
plt.plot(df["cfo"])
plt.show()

import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

def create_tsne_signature_from_csv(file_path):
    data = pd.read_csv(file_path, delimiter=";")
    data = data.iloc[1:-1]
    tsne = TSNE(n_components=2)
    transformed_data = tsne.fit_transform(data)
    plt.scatter(transformed_data[:, 0], transformed_data[:, 1])
    plt.show()

# create_tsne_signature_from_csv(path)
    
def extract_occurences(filepath):
    df1 = pd.read_csv(filepath, delimiter=";")
    df1["snr"] = df1["dl_snr"].round(1)
    df1["cfo"] = df1["cfo"].round(-1)
    cfo_liste = df1["cfo"][2:-2]
    snr_liste = df1["snr"][2:-2]
    occ_cfo = Counter(sorted(cfo_liste))
    occ_snr = Counter(sorted(snr_liste))
    return occ_snr, occ_cfo



filepath1 = path
filepath2 = "data/ue_metrics_0404_2.csv"
filepath3 = "data/ue_metrics_0404_2.csv"
filepath4 = "data/ue_metrics_1_1.csv"
filepath5 = "data/ue_metrics0404_3.csv"
filepath6 = "data/ue_metrics0304.csv"

occ_snr1, occ_cfo1 = extract_occurences(filepath1)
occ_snr2, occ_cfo2 = extract_occurences(filepath2)
occ_snr3, occ_cfo3 = extract_occurences(filepath3)
occ_snr4, occ_cfo4 = extract_occurences(filepath4)
occ_snr5, occ_cfo5 = extract_occurences(filepath5)
occ_snr6, occ_cfo6 = extract_occurences(filepath6)
# occ_snr1, occ_cfo1 = extract_occurences(filepath1)


# Création d'une figure et d'un axe
fig, ax = plt.subplots()

ax.plot(list(occ_snr1.keys()), list(occ_snr1.values()), label="Device 1")#a garder
# ax.plot(list(occ_snr2.keys()), list(occ_snr2.values()), label="Device 2")
# ax.plot(list(occ_snr3.keys()), list(occ_snr3.values()), label="Device 3")
ax.plot(list(occ_snr4.keys()), list(occ_snr4.values()), label="Device 4")#a garder
# ax.plot(list(occ_snr5.keys()), list(occ_snr5.values()), label="Device 5")
# ax.plot(list(occ_snr6.keys()), list(occ_snr6.values()), label="Device 6")

# Définition des étiquettes et du titre
ax.set_xlabel("SNR")
ax.set_ylabel("Occurrences")
ax.set_title("Occurrences des valeurs de SNR par device")

# Ajout de la légende
ax.legend()

# Afficher le graphique
plt.show()

# Création d'une figure et d'un axe
fig, ax = plt.subplots()

ax.plot(list(occ_cfo1.keys()), list(occ_cfo1.values()), label="Device 1")
# ax.plot(list(occ_cfo2.keys()), list(occ_cfo2.values()), label="Device 2")
# ax.plot(list(occ_cfo3.keys()), list(occ_cfo3.values()), label="Device 3")
ax.plot(list(occ_cfo4.keys()), list(occ_cfo4.values()), label="Device 4")
# ax.plot(list(occ_cfo5.keys()), list(occ_cfo5.values()), label="Device 5")
# ax.plot(list(occ_cfo6.keys()), list(occ_cfo6.values()), label="Device 6")

# Définition des étiquettes et du titre
ax.set_xlabel("CFO")
ax.set_ylabel("Occurrences")
ax.set_title("Occurrences des valeurs de CFO par device")

# Ajout de la légende
ax.legend()

# Afficher le graphique
plt.show()

