# Serverless Machine Learning - Grouping

#### Final Project of Bachelor's Degree in Information Systems at PUC-Rio

Application to execute Machine Learning Grouping algorithms on a serverless environment.

### JSON Parameters to run lambda at AWS Console:

* `"type"`: Type of algorithm to be executed (required, should be `"grouping"`);
* `"algorithm"`: Type of algorithm to be executed (required, because there are no default values);
* `"num_clusters"`: Number of clusters (`8` is the default);
* `"init_method"`: Initialization method (`"k-means++"` is the default);
* `"num_init"`: Initialization number (`10` is the default);
* `"max_iter"`: Maximum of iterations (`300` is the default);
* `"tolerance"`: Tolerance (`1e-4` is the default);
* `"seed"`: Seed for random generated dataset (`None` is the default);
* `"num_samples"`: Number of samples for random generated dataset (`100` is the default);
* `"num_features"`: Number of features for random generated dataset (`2` is the default);
* `"centers"`: Number of centers for random generated dataset (`None` is the default);
* `"cluster_std"`: Standard deviation for random generated dataset (`1.0` is the default);
* `"shuffle"`: Shuffle random generated dataset (`True` is the default);