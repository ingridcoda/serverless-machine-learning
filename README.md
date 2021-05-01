# Serverless Machine Learning

#### Final Project of Bachelor's Degree in Information Systems at PUC-Rio

Repository of applications that execute Machine Learning Classification and Grouping algorithms on a serverless
environment.

### Required resources

* [Python 3.8](https://wiki.python.org/moin/BeginnersGuide/Download)
* [Docker](https://docs.docker.com/get-docker/)
* [AWS Cli](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

### Environment preparing

Before deploying application, it's necessary to set some environment variables:

* `AWS_CREDENTIALS_PROFILE`: describes which AWS Credentials profile will be used for AWS Cli commands
* `AWS_ACCOUNT_NUMBER`: describes which AWS account will be used for AWS Cli commands
* `AWS_REGION`: describes which AWS region will be used for AWS Cli commands

To set these environment variables at Windows, open the command prompt as administrator and run the following commands:

* `set AWS_CREDENTIALS_PROFILE "profileName"`, changing `"profileName"` to the name of the desired AWS Credentials
  profile;
* `set AWS_ACCOUNT_NUMBER "1234567890"`, changing `"1234567890"` to the the
  desired [AWS Account Number](https://docs.aws.amazon.com/pt_br/general/latest/gr/acct-identifiers.html);
* `set AWS_REGION "region"`, changing `"region"` to the the
  desired [AWS Region](https://docs.aws.amazon.com/pt_br/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions)
  ;

To set these environment variables at Linux or MacOS, open the terminal and run the following commands:

* `export AWS_CREDENTIALS_PROFILE="profileName"`, changing `"profileName"` to the name of the desired AWS Credentials
  profile;
* `export AWS_ACCOUNT_NUMBER="1234567890"`, changing `"1234567890"` to the
  desired [AWS Account Number](https://docs.aws.amazon.com/pt_br/general/latest/gr/acct-identifiers.html);
* `export AWS_REGION="region"`, changing `"region"` to the
  desired [AWS Region](https://docs.aws.amazon.com/pt_br/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions)
  ;

These environment variables will be valid while the terminal session is open. When it's closed, the variables won't
exist anymore.

### Basic commands

* run `python3 -m venv venv/serverless-machine-learning` to create the virtual environment
* run `source venv/serverless-machine-learning/bin/activate` to work on the virtual environment
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

### Running Instructions

* [Classification Algorithms Aplications instructions](algorithms/classification/README.md)
* [Grouping Algorithms Aplications instructions](algorithms/grouping/README.md)
