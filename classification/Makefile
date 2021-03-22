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
	aws ecr get-login-password --region us-east-1 --profile pessoal | docker login --username AWS --password-stdin 274877485409.dkr.ecr.us-east-1.amazonaws.com
	@echo Autenticado com sucesso!
	@echo Construindo imagem docker para deploy...
	docker build -t classification .
	@echo Imagem construída com sucesso!
	@echo Atualizando imagem docker no AWS ECR classification...
	aws ecr batch-delete-image --repository-name classification --image-ids imageTag=latest --profile pessoal
	docker tag classification:latest 274877485409.dkr.ecr.us-east-1.amazonaws.com/classification
	docker push 274877485409.dkr.ecr.us-east-1.amazonaws.com/classification
	@echo Imagem docker AWS ECR classification atualizada com sucesso!
	@echo Fazendo deploy para a AWS Lambda Function classification...
	aws lambda update-function-code --function-name classification --image-uri 274877485409.dkr.ecr.us-east-1.amazonaws.com/classification:latest --profile pessoal
	@echo Deploy para a AWS Lambda Function classification feito com sucesso!

destroy:
	@echo Limpando docker...
	docker system prune -a -f
	@echo Limpo!