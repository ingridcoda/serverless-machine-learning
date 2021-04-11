mak.SILENT:

authenticate-ecr:
	@echo Authenticating...
	aws ecr get-login-password --region ${AWS_REGION} --profile ${AWS_CREDENTIALS_PROFILE} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com
	@echo Authenticated successfully!
	
create-ecr:
	@echo Creating AWS ECR classification...
	aws ecr create-repository --repository-name classification --region ${AWS_REGION} --image-scanning-configuration scanOnPush=true --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS ECR classification created successfully!
	@echo Adding docker default image at AWS ECR classification...
	docker pull hello-world
	docker tag hello-world:latest ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/classification
	docker push ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/classification
	@echo AWS ECR classification docker image added successfully!
	
create-role:
	@echo Creating AWS Role classification...
	aws iam create-role --role-name classification --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}' --profile ${AWS_CREDENTIALS_PROFILE}
	aws iam attach-role-policy --role-name classification --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole --profile ${AWS_CREDENTIALS_PROFILE}
	sleep 10
	@echo AWS Role classification created successfully!	
	
create-lambda:
	@echo Creating AWS Lambda Function classification...
	aws lambda create-function --function-name classification --timeout 900 --package-type Image --code ImageUri=${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/classification:latest --role arn:aws:iam::${AWS_ACCOUNT_NUMBER}:role/classification --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS Lambda Function classification created successfully!
	
create-aws-resources: authenticate-ecr create-ecr create-role create-lambda	

create-image:
	@echo Building docker image...
	docker build -t classification .
	@echo Image built was successfully!

create: create-aws-resources create-image
	
deploy-ecr:
	@echo Building docker image to deploy...
	docker build -t classification .
	@echo Image built was successfully!
	@echo Updating docker image at AWS ECR classification...
	aws ecr batch-delete-image --repository-name classification --image-ids imageTag=latest --profile ${AWS_CREDENTIALS_PROFILE}
	docker tag classification:latest ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/classification
	docker push ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/classification
	@echo AWS ECR classification docker image deployed successfully!
	
deploy-lambda:
	@echo Deploying to AWS Lambda Function classification...
	aws lambda update-function-code --function-name classification --image-uri ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/classification:latest --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS Lambda Function classification deployed successfully!
	
deploy: destroy authenticate-ecr deploy-ecr deploy-lambda
	
destroy-image:
	@echo Cleaning docker...
	docker system prune -a -f
	@echo Cleaned!
	
destoy-ecr:
	@echo Deleting AWS ECR classification...
	aws ecr delete-repository --repository-name classification --region ${AWS_REGION} --profile ${AWS_CREDENTIALS_PROFILE} --force
	@echo AWS ECR classification deleted successfully!
	
destroy-lambda:
	@echo Deleting AWS Lambda Function classification...
	aws lambda delete-function --function-name classification --region ${AWS_REGION} --profile ${AWS_CREDENTIALS_PROFILE}	
	aws logs delete-log-group --log-group-name /aws/lambda/classification --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS Lambda Function classification deleted successfully!

destroy-role:
	@echo Deleting AWS Role classification...
	aws iam detach-role-policy --role-name classification --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole --profile ${AWS_CREDENTIALS_PROFILE}
	aws iam delete-role --role-name classification --region ${AWS_REGION} --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS Role classification deleted successfully!	
	
destroy-aws-resources: destroy-lambda destroy-ecr destroy-role

destroy: destroy-aws-resources destroy-image
	
