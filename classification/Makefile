mak.SILENT:

install:
	pip install -r requirements/base.txt


local-run: destroy
	@echo Construindo imagem docker para execução local...
	docker build -t classification .
	@echo Imagem construída com sucesso!
	docker run classification

deploy: destroy
	@echo Autenticando...
	aws ecr get-login-password --region ${AWS_REGION} --profile ${AWS_CREDENTIALS_PROFILE} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com
	@echo Autenticado com sucesso!
	@echo Construindo imagem docker para deploy...
	docker build -t classification .
	@echo Imagem construída com sucesso!
	@echo Atualizando imagem docker no AWS ECR classification...
	aws ecr batch-delete-image --repository-name classification --image-ids imageTag=latest --profile ${AWS_CREDENTIALS_PROFILE}
	docker tag classification:latest ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/classification
	docker push ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/classification
	@echo Imagem docker AWS ECR classification atualizada com sucesso!
	@echo Fazendo deploy para a AWS Lambda Function classification...
	aws lambda update-function-code --function-name classification --image-uri ${AWS_ACCOUNT_NUMBER}.dkr.ecr.${AWS_REGION}.amazonaws.com/classification:latest --profile ${AWS_CREDENTIALS_PROFILE}
	@echo Deploy para a AWS Lambda Function classification feito com sucesso!

destroy:
	@echo Limpando docker...
	docker system prune -a -f
	@echo Limpo!