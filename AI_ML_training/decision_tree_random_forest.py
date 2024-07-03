class DecisionTree:
    def __init__(self, max_depth: int = 5, model_type: str = "classifier"):
        self.max_depth = max_depth
        self.model_type = model_type

        assert model_type in [
            "classifier",
            "regressor",
        ], "model_type must be either 'classifier' or 'regressor'"

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        self.tree = self._build_tree(X, y, 0)

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.array([self._traverse_tree(x, self.tree) for x in X])

    def _build_tree(self, X: np.ndarray, y: np.ndarray, depth: int) -> dict:
        if depth >= self.max_depth or self._is_pure(y):
            return self._create_leaf(y)

        feature, threshold = self._find_best_split(X, y)
        
        if feature is None or threshold is None:
            return self._create_leaf(y)
        
        mask = X[:,feature] <= threshold
        left_X, left_y = X[mask], y[mask]
        right_X, right_y = X[~mask],y[~mask]
        
        left_child = self._build_tree(left_X,left_y,depth+1)
        right_child = self._build_tree(right_X,right_y,depth+1)
        
        return {
            "feature": feature,
            "threshold": threshold,
            "left": left_child,
            "right": right_child,
        }

    def _is_pure(self, y: np.ndarray) -> bool:
        return len(set(y)) == 1

    def _create_leaf(self, y: np.ndarray):
        if self.model_type == "classifier":
            classes, counts = np.unique(y, return_counts=True)
            majority_class = classes[np.argmax(counts)]
            return majority_class

        else:

            return np.mean(y)


    def _find_best_split(self, X: np.ndarray, y: np.ndarray) -> tuple[int, float]:
        best_gini = float("inf")
        best_mse = float("inf")
        best_feature = None
        best_threshold = None

        for feature in range(X.shape[1]):
            sorted_indices = np.argsort(X[:, feature])
            for i in range(1, len(X)):
                if X[sorted_indices[i - 1], feature] != X[sorted_indices[i], feature]:
                    threshold = (
                        X[sorted_indices[i - 1], feature]
                        + X[sorted_indices[i], feature]
                    ) / 2
                    mask = X[:, feature] <= threshold
                    left_y, right_y = y[mask], y[~mask]

                    if self.model_type == "classifier":
                        gini = self._gini_index(left_y, right_y)
                        if gini < best_gini:
                            best_gini = gini
                            best_feature = feature
                            best_threshold = threshold
                    else:
                        mse = self._mse(left_y, right_y)
                        if mse < best_mse:
                            best_mse = mse
                            best_feature = feature
                            best_threshold = threshold

        return best_feature, best_threshold

    def _gini_index(self, left_y: np.ndarray, right_y: np.ndarray) -> float:
        def gini(y):
            _, counts = np.unique(y, return_counts=True)
            sample_num = len(y)
            result = 1.0
            for count in counts:
                result -= (count/sample_num)**2
            return result
        
        left_gini = gini(left_y)
        right_gini = gini(right_y)
        total_samples = len(left_y) + len(right_y)
        weighted_gini = (len(left_y)/total_samples*left_gini) + (len(right_y)/total_samples*right_gini)
        return weighted_gini


    def _mse(self, left_y: np.ndarray, right_y: np.ndarray) -> float:
        def mse(y):
            return np.sum((y-np.mean(y))**2) / len(y) if len(y) > 0 else 0
        left_mse = mse(left_y)
        right_mse = mse(right_y)
        total_samples = len(left_y)+len(right_y)
        weighted_mse = (len(left_y)/total_samples*left_mse) + (len(right_y)/total_samples*right_mse)
        return weighted_mse

    def _traverse_tree(self, x: np.ndarray, node: dict):
        if isinstance(node, dict):
            feature, threshold = node["feature"], node["threshold"]
            if x[feature] <= threshold:
                return self._traverse_tree(x, node["left"])
            else:
                return self._traverse_tree(x, node["right"])
        else:
            return node


class RandomForest:
    def __init__(
        self,
        n_estimators: int = 100,
        max_depth: int = 5,
        model_type: str = "classifier",
    ):


        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.model_type = model_type



    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        self.trees = []
        for _ in range(self.n_estimators):
            tree = DecisionTree(max_depth=self.max_depth,
                         model_type='classifier'
                         )

            n_samples = X.shape[0]
            bootstrap_indices = np.random.choice(n_samples,
                                                 size=n_samples,
                                                 replace=True
            )
            X_bootstrap = X[bootstrap_indices]
            y_bootstrap = y[bootstrap_indices]
            tree.fit(X_bootstrap, y_bootstrap)
            self.trees.append(tree)


    def _most_common_label(self, y):
        counter = Counter(y)
        most_common = counter.most_common(1)[0][0]
        return most_common

    def predict(self, X):
        predictions = np.array([tree.predict(X) for tree in self.trees])
        tree_preds = np.swapaxes(predictions, 0, 1)
        predictions = np.array([self._most_common_label(pred) for pred in tree_preds])
        print(predictions)
        return predictions
