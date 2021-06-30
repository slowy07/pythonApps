from machine_learning.k_nearest_neighbours import X_test, X_train
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
iris.key()

print(f"Target name : \n {iris.target_names}")
print(f"\nFeatures: \n {iris.feature_names}")

X_train, X_test, y_train, y_test = train_test_split(
    iris["data"], iris["target"], random_state = 4
)

knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train, y_train)

X_new = [[1, 2, 1, 4], [2, 3, 4, 5]]
prediction = knn.predict(X_new)
print(
    f"\nNew array: \n {X_new}\n\nTarget Names Prediction: \n"
    f" {iris['target_names'][prediction]}"
)