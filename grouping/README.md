# Serverless Machine Learning - Grouping
#### Final Project of Bachelor's Degree in Information Systems at PUC-Rio

Application to execute Machine Learning Grouping algorithms on a serverless environment.

### Environment preparing
Before deploying application, it's necessary to set some environment variables:
* `AWS_CREDENTIALS_PROFILE`: describes which AWS Credentials profile will be used for awscli commands
* `AWS_ACCOUNT_NUMBER`: describes which AWS account will be used for awscli commands
* `AWS_REGION`: describes which AWS region will be used for awscli commands

To set these environment variables at Windows, open the command prompt as administrator and run the following commands:
* `set AWS_CREDENTIALS_PROFILE "profileName"`, changing `"profileName"` to the name of the desired AWS Credentials profile;
* `set AWS_ACCOUNT_NUMBER "1234567890"`, changing `"1234567890"` to the the desired AWS Account Number;
* `set AWS_REGION "region"`, changing `"region"` to the the desired AWS Region;

To set these environment variables at Linux or MacOS, open the terminal and run the following commands:
* `export AWS_CREDENTIALS_PROFILE="profileName"`, changing `"profileName"` to the name of the desired AWS Credentials profile;
* `export AWS_ACCOUNT_NUMBER="1234567890"`, changing `"1234567890"` to the the desired AWS Account Number;
* `export AWS_REGION="region"`, changing `"region"` to the the desired AWS Region;

These environment variables will be valid while the terminal session is open. When it's closed, the variables won't exist anymore.

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
