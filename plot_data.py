import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from scipy.stats import norm
from extract_data import extract_cfo_from_data, extract_SNR_from_data, extract_joint_data, extract_data_csv

# CFO = extract_cfo_from_data('data.txt')
# SNR = extract_SNR_from_data('data.txt')
# print(len(CFO))
filename = "ue_metrics_1_2.csv"
CFO, SNR = extract_data_csv(f"data/{filename}")
CFO, SNR = CFO[1:-1], SNR[1:-1]
CFO = [round(abs(x)) for x in CFO]
print(len(SNR), len(CFO))
# Pour CFO
fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
axs[0].hist(CFO, bins=30, color='b')
axs[1].hist(SNR, bins=30, color='g')
# Calcule la distribution normale
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, np.mean(CFO), np.std(CFO))

# Trace la distribution normale
plt.plot(x, p, 'k', linewidth=2)
plt.title("Distribution normale pour CFO")
plt.show()

# CFO, SNR = extract_joint_data('data.txt')

fig, axs = plt.subplots( tight_layout=True)

# We can increase the number of bins on each axis
axs.hist2d(CFO, SNR, bins=100)
plt.title("Empreinte CNO-SNR")
plt.show()

# # Pour SNR
# plt.figure(figsize=(10, 5))
# plt.hist(SNR, bins=30, density=True, alpha=0.6, color='g')

# # Calcule la distribution normale
# xmin, xmax = plt.xlim()
# x = np.linspace(xmin, xmax, 100)
# p = norm.pdf(x, np.mean(SNR), np.std(SNR))

# # Trace la distribution normale
# plt.plot(x, p, 'k', linewidth=2)
# plt.title("Distribution normale pour SNR")
# plt.show()

from mpl_toolkits.mplot3d import Axes3D

# Calculer l'histogramme 2D
hist, xedges, yedges = np.histogram2d(CFO, SNR, bins=30)

# Créer une grille pour le graphique 3D
xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1], indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Définir la hauteur de chaque barre en fonction du nombre d'occurrences
dx = dy = 0.1 * np.ones_like(zpos)
dz = hist.ravel()

# Créer une figure 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Ajouter les données au graphique
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')

# Définir les labels des axes
ax.set_xlabel('CFO')
ax.set_ylabel('SNR')
ax.set_zlabel('Occurrences')

# Afficher le graphique
plt.show()