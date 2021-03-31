# Serverless Machine Learning - Grouping
####Final Project of Bachelor's Degree in Information Systems at PUC-Rio

Application to execute Machine Learning Grouping algorithms on a serverless environment.

### Environment preparing
Before deploying application, it's necessary to set some environment variables:
* `AWS_CREDENTIALS_PROFILE`: describes which AWS Credentials profile will be used for awscli commands
* `AWS_ACCOUNT_NUMBER`: describes which AWS account will be used for awscli commands
* `AWS_REGION`: describes which AWS region will be used for awscli commands

### Useful commands
* run `python3 -m venv venv/grouping` to create the virtual environment
* run `source venv/grouping/bin/activate` to work on the virtual environment
* run `make install` to install the dependencies locally
* run `make deploy` to deploy application to AWS
* run `make destroy` to destroy all
