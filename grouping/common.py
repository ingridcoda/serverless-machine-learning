from sklearn.datasets import make_blobs


def generate_dataset(n_samples, n_features, centers, cluster_std, shuffle, seed):
    X, y = make_blobs(n_samples=n_samples,
                      n_features=n_features,
                      centers=centers,
                      cluster_std=cluster_std,
                      shuffle=shuffle,
                      random_state=seed)

    return X, y


def run_with_model(model, n_samples, n_features, centers, cluster_std, shuffle, seed):
    X, y = generate_dataset(n_samples, n_features, centers, cluster_std, shuffle, seed)
    predictions = model.fit_predict(X)
    distortion = model.inertia_
    print(f"Model predictions: {predictions}")
    print(f"Model distortion: {distortion}")
