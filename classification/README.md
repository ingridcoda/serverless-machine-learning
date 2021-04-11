# Serverless Machine Learning - Classification
#### Final Project of Bachelor's Degree in Information Systems at PUC-Rio

Application to execute Machine Learning Classification algorithms on a serverless environment.

### Environment preparing
Before deploying application, it's necessary to set some environment variables:
* `AWS_CREDENTIALS_PROFILE`: describes which AWS Credentials profile will be used for awscli commands
* `AWS_ACCOUNT_NUMBER`: describes which AWS account will be used for awscli commands
* `AWS_REGION`: describes which AWS region will be used for awscli commands

To set these environment variables at Windows, open the command prompt as administrator and run the following commands:
* `set AWS_CREDENTIALS_PROFILE "profileName"`, changing "profileName" to the name of the desired AWS Credentials profile;
* `set AWS_ACCOUNT_NUMBER "1234567890"`, changing "1234567890" to the the desired AWS Account Number;
* `set AWS_REGION "region"`, changing "region" to the the desired AWS Region;

To set these environment variables at Linux or MacOS, open the terminal and run the following commands:
* `export AWS_CREDENTIALS_PROFILE="profileName"`, changing "profileName" to the name of the desired AWS Credentials profile;
* `export AWS_ACCOUNT_NUMBER="1234567890"`, changing "1234567890" to the the desired AWS Account Number;
* `export AWS_REGION="region"`, changing "region" to the the desired AWS Region;

These environment variables will be valid while the terminal session is open. When it's closed, the variables won't exist anymore.

### Basic commands
* run `python3 -m venv ../venv/classification` to create the virtual environment
* run `source ../venv/classification/bin/activate` to work on the virtual environment
* run `make create` to create all required resources
* run `make deploy` to deploy application to AWS
* run `make destroy` to destroy all

### Other useful commands
* run `make create-aws-resources` to create only the required resources at AWS
* run `make destroy-aws-resources` to delete only the required resources at AWS
* run `make create-image` to create only the project's Docker image
* run `make destroy-image` to destroy only the project's Docker image
* run `make create-role` to create only the project's AWS Role
* run `make destroy-role` to delete only the project's AWS Role
* run `make create-ecr` to create only the project's AWS ECR
* run `make deploy-ecr` to deploy the project only to AWS ECR
* run `make destroy-ecr` to delete only the project's AWS ECR
* run `make create-lambda` to create only the project's AWS Lambda Function
* run `make deploy-lambda` to deploy the project only to AWS Lambda Function
* run `make destroy-lambda` to delete only the project's AWS Lambda Function

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
