import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

np.random.seed(42)

data1 = np.random.normal(loc =-5, scale=1, size=300)
data2 = np.random.normal(loc =5, scale=1, size=700)

data = np.concatenate([data1,data2])

plt.hist(data, bins=30, density=True)
plt.title("Sucos Originais")
plt.show()

gmm = GaussianMixture(n_components=2)
gmm.fit(data.reshape(-1,1))

samples = gmm.sample(1000)[0]
plt.hist(samples, bins=30, density=True, color='green', label='Suco Primavera')
plt.hist(data, bins=30, density=True, color='red', label='Suco Originais')
plt.title('Comparação')
plt.legend()
plt.show()