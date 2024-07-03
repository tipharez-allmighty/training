from collections import Counter

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

np.random.seed(0)

def train_test_split(
    df: pd.DataFrame, target: str, test_size: float = 0.3
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    split_idx = int(len(df) * (1 - test_size))
    train = df.iloc[:split_idx]
    test = df.iloc[split_idx:]


    X_train = train.drop(target, axis=1).values
    y_train = train[target].values
    X_test = test.drop(target, axis=1).values
    y_test = test[target].values

    return X_train, X_test, y_train, y_test


def normalize(X: np.ndarray) -> np.ndarray:
    X = (X - np.min(X))/(np.max(X) - np.min(X))
    return X

class LinearModel:
    def __init__(
        self, learning_rate=0.01, iterations=1000, model_type="linear"
    ) -> None:
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.model_type = model_type

        assert model_type in [
            "linear",
            "logistic",
        ], "model_type must be either 'linear' or 'logistic'"
        self.intercept_ = None
        self.coef_ = None
        self.beta = None
        self.theta = None

       
    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        X = np.insert(X, 0, 1, axis=1)
        onehot_encoder = OneHotEncoder(sparse_output=False)
        y_hot = onehot_encoder.fit_transform(y.reshape(-1, 1))
        if self.model_type == "logistic":
            #pass
            self.theta = np.zeros((X.shape[1], y_hot.shape[1]))
            for _ in range(self.iterations):
                gradient = self._compute_gradients(X,y_hot)
                self.theta -= self.learning_rate*gradient
                loss = self._loss(X, y_hot)

        else:

            self.beta = np.linalg.inv(X.T@X)@X.T@y
            self.intercept_ = self.beta[0]
            self.coef_ = self.beta[1:]

    def predict(self, X: np.ndarray) -> np.ndarray:
        X = np.insert(X, 0, 1, axis=1)
        if self.model_type == "linear":
            return X @ np.concatenate(([self.intercept_],self.coef_))

        elif self.model_type == "logistic":
            Z = -X @ self.theta
            probabilities = self._softmax(Z)
            return np.argmax(probabilities, axis=1)

    
    def _loss(self, X: np.ndarray, y_encoded: np.ndarray) -> float:
        Z = -X @ self.theta
        N = X.shape[0]
        loss = 1/N * (np.trace(X @ self.theta  - y_encoded) + np.sum(np.log(np.sum(np.exp(Z), axis=1))))
        return loss      
    
    def _softmax(self, z: np.ndarray) -> np.ndarray:
        exp = np.exp(z)
        return exp / np.sum(exp, axis=1, keepdims=True)

    def _compute_gradients(self, X: np.ndarray, y: np.ndarray) -> np.ndarray:
        if self.model_type == "linear":
            raise NotImplementedError
        elif self.model_type == "logistic":
            Z = -X @ self.theta
            N = X.shape[0]
            P = self._softmax(Z)
            gd = 1/N * X.T @ (y - P)
            return gd

def accuracy(y_true, y_pred):
    return np.mean(y_true==y_pred)
  
def mean_squared_error(y_true, y_pred):
    return np.sum((y_true-y_pred)**2) / len(y_true)
