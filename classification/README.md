# Serverless Machine Learning - Classification
####Final Project of Bachelor's Degree in Information Systems at PUC-Rio

Application to execute Machine Learning Classification algorithms on a serverless environment.

### Environment preparing
Before deploying application, it's necessary to set some environment variables:
* `AWS_CREDENTIALS_PROFILE`: describes which AWS Credentials profile will be used for awscli commands
* `AWS_ACCOUNT_NUMBER`: describes which AWS account will be used for awscli commands
* `AWS_REGION`: describes which AWS region will be used for awscli commands

### Useful commands
* run `python3 -m venv venv/classification` to create the virtual environment
* run `source venv/classification/bin/activate` to work on the virtual environment
* run `make install` to install the dependencies locally
* run `make deploy` to deploy application to AWS
* run `make destroy` to destroy all


### JSON Parameters to run lambda at AWS Console:
* `"algorithm"`: Type of algorithm to be executed (required, because there are no default values);
* `"dataset_name"`: Dataset name (only [scikit-learn datasets](https://scikit-learn.org/stable/datasets) are accepted;`"iris"` is the default);
* `"dataset_url"`: Dataset URL (if this value is valid, will be used instead of `"dataset_name"`);
* `"k_fold"`: Number of folds for cross validation (`10` is the default);
* `"seed"`: Seed for cross validation (`7` is the default);
* `"test_size"`: Test size for training and test validation (`0.25` is the default);
* `"k"`: Number of neighbors (for KNN algorithm only, `10` is the default);
* `"distance_type"`: Distance type (for KNN algorithm only; `"euclidean"` is the default);
* `"gamma"`: Gamma type (for SVM algorithm only; `"auto"` is the default);
* `"kernel"`: Kernel type (for SVM algorithm only; `"rbf"` is the default);
* `"solver"`: Solver type (for Logistic Regression algorithm only; `"lbfgs"` is the default).