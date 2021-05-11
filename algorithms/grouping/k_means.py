from sklearn.cluster import KMeans

import common as c


def run(dataset_url, delimiter, num_clusters, init_method, num_init, max_iter, tolerance, seed):
    try:
        model = KMeans(n_clusters=num_clusters, init=init_method, n_init=num_init,
                       max_iter=max_iter, tol=tolerance, random_state=seed)
        c.run_with_grouping_model(model, dataset_url, delimiter)
    except Exception as e:
        raise e
