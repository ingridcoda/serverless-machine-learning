mak.SILENT:

authenticate-ecr:
	@echo Authenticating...
	aws ecr get-login-password --region ${AWS_REGION} --profile ${AWS_CREDENTIALS_PROFILE} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com
	@echo Authenticated successfully!
	
create-ecr:
	@echo Creating AWS ECR grouping...
	aws ecr create-repository --repository-name grouping --region ${AWS_REGION} --image-scanning-configuration scanOnPush=true --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS ECR grouping created successfully!
	@echo Adding docker default image at AWS ECR grouping...
	docker pull hello-world
	docker tag hello-world:latest ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/grouping
	docker push ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/grouping
	@echo AWS ECR grouping docker image added successfully!
	
create-role:
	@echo Creating AWS Role grouping...
	aws iam create-role --role-name grouping --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}' --profile ${AWS_CREDENTIALS_PROFILE}
	aws iam attach-role-policy --role-name grouping --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole --profile ${AWS_CREDENTIALS_PROFILE}
	sleep 10
	@echo AWS Role grouping created successfully!	
	
create-lambda:
	@echo Creating AWS Lambda Function grouping...
	aws lambda create-function --function-name grouping --timeout 900 --memory-size 2048 --package-type Image --code ImageUri=${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/grouping:latest --role arn:aws:iam::${AWS_ACCOUNT_NUMBER}:role/grouping --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS Lambda Function grouping created successfully!
	
create-aws-resources: authenticate-ecr create-ecr create-role create-lambda	

create-image:
	@echo Building docker image...
	docker build -t grouping .
	@echo Image built was successfully!

create: create-aws-resources create-image
	
deploy-ecr:
	@echo Updating docker image to deploy...
	docker build -t grouping .
	@echo Image updated successfully!
	@echo Updating docker image at AWS ECR grouping...
	aws ecr batch-delete-image --repository-name grouping --image-ids imageTag=latest --profile ${AWS_CREDENTIALS_PROFILE}
	docker tag grouping:latest ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/grouping
	docker push ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/grouping
	@echo AWS ECR grouping docker image deployed successfully!
	
deploy-lambda:
	@echo Deploying to AWS Lambda Function grouping...
	aws lambda update-function-code --function-name grouping --image-uri ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/grouping:latest --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS Lambda Function grouping deployed successfully!
	
deploy: authenticate-ecr deploy-ecr deploy-lambda
	
destroy-image:
	@echo Cleaning docker...
	docker system prune -a -f
	@echo Cleaned!
	
destroy-ecr:
	@echo Deleting AWS ECR grouping...
	aws ecr delete-repository --repository-name grouping --region ${AWS_REGION} --profile ${AWS_CREDENTIALS_PROFILE} --force
	@echo AWS ECR grouping deleted successfully!
	
destroy-lambda:
	@echo Deleting AWS Lambda Function grouping...
	aws lambda delete-function --function-name grouping --region ${AWS_REGION} --profile ${AWS_CREDENTIALS_PROFILE}	
	aws logs delete-log-group --log-group-name /aws/lambda/grouping --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS Lambda Function grouping deleted successfully!

destroy-role:
	@echo Deleting AWS Role grouping...
	aws iam detach-role-policy --role-name grouping --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole --profile ${AWS_CREDENTIALS_PROFILE}
	aws iam delete-role --role-name grouping --region ${AWS_REGION} --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS Role grouping deleted successfully!	
	
destroy-aws-resources: destroy-lambda destroy-ecr destroy-role

destroy: destroy-aws-resources destroy-image
	
