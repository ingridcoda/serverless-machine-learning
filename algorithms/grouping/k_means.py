from sklearn.cluster import KMeans

import common as c


def run(num_clusters, init_method, num_init, max_iter, tolerance,
        seed, n_samples, n_features, centers, cluster_std, shuffle):
    try:
        model = KMeans(n_clusters=num_clusters, init=init_method, n_init=num_init,
                       max_iter=max_iter, tol=tolerance, random_state=seed)
        c.run_with_grouping_model(model, n_samples, n_features, centers, cluster_std, shuffle, seed)
    except Exception as e:
        raise e
