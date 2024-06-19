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
        X_norm = self.normalize(X)
        cov_matrix = np.cov(X_norm.T)
        eigen_values, eigen_vectors = np.linalg.eigh(cov_matrix)
        sorted_idx = np.argsort(np.abs(eigen_values))[::-1]
        eigen_vectors_sorted = eigen_vectors[:, sorted_idx]
        
        self.components = eigen_vectors_sorted[:, :self.n_components].T
    
    def normalize(self,X: np.ndarray) -> np.ndarray:
        return X - np.mean(X, axis=0)
        
    def transform(self, X: np.ndarray) -> np.ndarray:
        return np.dot(self.normalize(X), self.components.T)

    def reconstruct(self, X: np.ndarray) -> np.ndarray:
        return np.dot(self.transform(X), self.components) + np.mean(X, axis=0)
