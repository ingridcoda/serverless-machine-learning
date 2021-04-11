# Serverless Machine Learning - Grouping
#### Final Project of Bachelor's Degree in Information Systems at PUC-Rio

Application to execute Machine Learning Grouping algorithms on a serverless environment.

### Environment preparing
Before deploying application, it's necessary to set some environment variables:
* `AWS_CREDENTIALS_PROFILE`: describes which AWS Credentials profile will be used for awscli commands
* `AWS_ACCOUNT_NUMBER`: describes which AWS account will be used for awscli commands
* `AWS_REGION`: describes which AWS region will be used for awscli commands

### Basic commands
* run `python3 -m venv venv/grouping` to create the virtual environment
* run `source venv/grouping/bin/activate` to work on the virtual environment
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
* `"dataset_url"`: Dataset URL (if this value is valid, will be used instead of `"dataset_name"`).
