import numpy as np

"""
Implementation of Principal Component Analysis.
"""
class PCA:
    def __init__(self, n_components: int) -> None:
        self.n_components = n_components
        self.mean = None
        self.components = None

    def fit(self, X: np.ndarray) -> None:

        self.mean = np.mean(X,axis=0)
        self.std = np.std(X,axis=0)
        X_std = (X - self.mean)/self.std
        cov_matrix = np.cov(X_std.T)
        eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)
        max_idx = np.argmax(np.abs(eigen_vectors),axis=0)
        feature_signs = np.signs(eigen_vectors[max_idx,range(eigen_vectors.shape[0])])
        eigen_vectors *= feature_signs[np.newaxis,:]
        eigen_vectors = eigen_vectors.T
        eigen_pairs = [(np.abs(eigen_values[i]),eigen_vectors[i,:]) for i in range(len(eigen_values))]
        eigen_pairs.sort(key=lambda x: x[0], reverse=True)
        eigen_values_sorted = np.array([x[0] for x in eigen_pairs])
        eigen_vectors_sorted = np.array([x[1] for x in eigen_pairs])
        
        self.components = eigen_vectors_sorted[:self.n_components,:]

    def transform(self, X: np.ndarray) -> np.ndarray:

        raise NotImplementedError

    def reconstruct(self, X):
        raise NotImplementedError

