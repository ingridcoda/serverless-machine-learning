mak.SILENT:

install:
	pip install -r requirements/base.txt

deploy: destroy
	@echo Authenticating...
	aws ecr get-login-password --region ${AWS_REGION} --profile ${AWS_CREDENTIALS_PROFILE} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com
	@echo Successfully authenticated!
	@echo Building docker image to deploy...
	docker build -t grouping .
	@echo Image built successfully!
	@echo Updating docker image at AWS ECR grouping...
	aws ecr batch-delete-image --repository-name grouping --image-ids imageTag=latest --profile ${AWS_CREDENTIALS_PROFILE}
	docker tag grouping:latest ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/grouping
	docker push ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/grouping
	@echo AWS ECR grouping docker image successfully updated!
	@echo Deploying to AWS Lambda Function grouping...
	aws lambda update-function-code --function-name grouping --image-uri ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/grouping:latest --profile ${AWS_CREDENTIALS_PROFILE}
	@echo AWS Lambda Function grouping deploy was successful!

destroy:
	@echo Cleaning docker...
	docker system prune -a -f
	@echo Cleaned!