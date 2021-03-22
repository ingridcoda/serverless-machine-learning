mak.SILENT:

install:
	pip install -r requirements/base.txt


local-run: destroy
	@echo Construindo imagem docker para execução local...
	docker build -t grouping .
	@echo Imagem construída com sucesso!
	docker run grouping

deploy: destroy
	@echo Autenticando...
	aws ecr get-login-password --region us-east-1 --profile pessoal | docker login --username AWS --password-stdin 274877485409.dkr.ecr.us-east-1.amazonaws.com
	@echo Autenticado com sucesso!
	@echo Construindo imagem docker para deploy...
	docker build -t grouping .
	@echo Imagem construída com sucesso!
	@echo Atualizando imagem docker no AWS ECR grouping...
	aws ecr batch-delete-image --repository-name grouping --image-ids imageTag=latest --profile pessoal
	docker tag grouping:latest 274877485409.dkr.ecr.us-east-1.amazonaws.com/grouping
	docker push 274877485409.dkr.ecr.us-east-1.amazonaws.com/grouping
	@echo Imagem docker AWS ECR grouping atualizada com sucesso!
	@echo Fazendo deploy para a AWS Lambda Function grouping...
	aws lambda update-function-code --function-name grouping --image-uri 274877485409.dkr.ecr.us-east-1.amazonaws.com/grouping:latest --profile pessoal
	@echo Deploy para a AWS Lambda Function grouping feito com sucesso!

destroy:
	@echo Limpando docker...
	docker system prune -a -f
	@echo Limpo!