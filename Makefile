mak.SILENT:

authenticate-ecr:
	@echo Authenticating...
	aws ecr get-login-password --region ${AWS_REGION} --profile ${AWS_CREDENTIALS_PROFILE} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com
	@echo Authenticated successfully!
	
create-ecr:
	@echo Creating AWS ECR serverless-machine-learning...
	aws ecr create-repository --repository-name serverless-machine-learning --region ${AWS_REGION} --image-scanning-configuration scanOnPush=true --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS ECR serverless-machine-learning created successfully!
	@echo Adding docker default image at AWS ECR serverless-machine-learning...
	docker pull hello-world
	docker tag hello-world:latest ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/serverless-machine-learning
	docker push ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/serverless-machine-learning
	@echo AWS ECR serverless-machine-learning docker image added successfully!
	
create-role:
	@echo Creating AWS Role serverless-machine-learning...
	aws iam create-role --role-name serverless-machine-learning --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}' --profile ${AWS_CREDENTIALS_PROFILE}
	aws iam attach-role-policy --role-name serverless-machine-learning --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole --profile ${AWS_CREDENTIALS_PROFILE}
	sleep 10
	@echo AWS Role serverless-machine-learning created successfully!	
	
create-lambda:
	@echo Creating AWS Lambda Function serverless-machine-learning...
	aws lambda create-function --function-name serverless-machine-learning --timeout 900 --memory-size 2048 --package-type Image --code ImageUri=${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/serverless-machine-learning:latest --role arn:aws:iam::${AWS_ACCOUNT_NUMBER}:role/serverless-machine-learning --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS Lambda Function serverless-machine-learning created successfully!
	
create-aws-resources: authenticate-ecr create-ecr create-role create-lambda	

create-image:
	@echo Building docker image...
	docker build -t serverless-machine-learning .
	@echo Image built was successfully!

create: create-aws-resources create-image
	
deploy-ecr:
	@echo Updating docker image to deploy...
	docker build -t serverless-machine-learning .
	@echo Image updated successfully!
	@echo Updating docker image at AWS ECR serverless-machine-learning...
	aws ecr batch-delete-image --repository-name serverless-machine-learning --image-ids imageTag=latest --profile ${AWS_CREDENTIALS_PROFILE}
	docker tag serverless-machine-learning:latest ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/serverless-machine-learning
	docker push ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/serverless-machine-learning
	@echo AWS ECR serverless-machine-learning docker image deployed successfully!
	
deploy-lambda:
	@echo Deploying to AWS Lambda Function serverless-machine-learning...
	aws lambda update-function-code --function-name serverless-machine-learning --image-uri ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/serverless-machine-learning:latest --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS Lambda Function serverless-machine-learning deployed successfully!
	
deploy: authenticate-ecr deploy-ecr deploy-lambda

invoke:
	aws lambda invoke --profile ${AWS_CREDENTIALS_PROFILE} --function-name serverless-machine-learning --payload '${PAYLOAD}' --cli-binary-format raw-in-base64-out out --log-type Tail --query 'LogResult' --output text |  base64 -d
	
destroy-image:
	@echo Cleaning docker...
	docker system prune -a -f
	@echo Cleaned!
	
destroy-ecr:
	@echo Deleting AWS ECR serverless-machine-learning...
	aws ecr delete-repository --repository-name serverless-machine-learning --region ${AWS_REGION} --profile ${AWS_CREDENTIALS_PROFILE} --force
	@echo AWS ECR serverless-machine-learning deleted successfully!
	
destroy-lambda:
	@echo Deleting AWS Lambda Function serverless-machine-learning...
	aws lambda delete-function --function-name serverless-machine-learning --region ${AWS_REGION} --profile ${AWS_CREDENTIALS_PROFILE}	
	aws logs delete-log-group --log-group-name /aws/lambda/serverless-machine-learning --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS Lambda Function serverless-machine-learning deleted successfully!

destroy-role:
	@echo Deleting AWS Role serverless-machine-learning...
	aws iam detach-role-policy --role-name serverless-machine-learning --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole --profile ${AWS_CREDENTIALS_PROFILE}
	aws iam delete-role --role-name serverless-machine-learning --region ${AWS_REGION} --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS Role serverless-machine-learning deleted successfully!	
	
destroy-aws-resources: destroy-lambda destroy-ecr destroy-role

destroy: destroy-aws-resources destroy-image
	
