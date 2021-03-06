# Serverless Machine Learning - Classification

#### Final Project of Bachelor's Degree in Information Systems at PUC-Rio

Application to execute Machine Learning Classification algorithms on a serverless environment.

### Supported algorithms:

* Decision Tree (`"decision_tree"`);
* K-Neighbors Nearest (`"knn"`);
* Naive Bayes (`"naive_bayes"`);
* Logistic Regression (`"logistic_regression"`);
* Support Vector Machines (`"svm"`).

### JSON Parameters to run lambda at AWS Console:

* `"type"`: Type of model to be executed (required, should be `"classification"`);
* `"algorithm"`: Type of algorithm to be executed (required, because there are no default values);
* `"dataset_url"`: Dataset URL (required, should be an URL to a .csv dataset);
* `"delimiter"`: Dataset delimiter (`","` is the default);
* `"k_fold"`: Number of folds for cross validation (`10` is the default);
* `"seed"`: Seed for cross validation (`7` is the default);
* `"test_size"`: Test size for training and test validation (`0.25` is the default);
* `"criterion"`: The function to measure the quality of a split (for Decision Tree only; `gini` is the default);
* `"max_depth"`: Maximum depth of tree (for Decision Tree only; `None` is the default);
* `"k"`: Number of neighbors (for KNN algorithm only, `10` is the default);
* `"distance_type"`: Distance type (for KNN algorithm only; `"euclidean"` is the default);
* `"gamma"`: Gamma type (for SVM algorithm only; `"auto"` is the default);
* `"kernel"`: Kernel type (for SVM algorithm only; `"rbf"` is the default);
* `"c"`: Regularization parameter (for SVM algorithm only; `1.0` is the default);
* `"solver"`: Solver type (for Logistic Regression algorithm only; `"lbfgs"` is the default);
* `"max_iter"`: Maximum of iterations (for Logistic Regression algorithm only; `1000` is the default).
