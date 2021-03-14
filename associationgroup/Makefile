mak.SILENT:

install:
	pip install -r requirements/base.txt

deploy:
	@echo Construindo imagem docker para deploy...
	docker build -t association-group .
	@echo Imagem construída com sucesso!
	@echo Fazendo deploy para a AWS Lambda Function association-group...
	docker tag association-group:latest 274877485409.dkr.ecr.us-east-1.amazonaws.com/association-group
	docker push 274877485409.dkr.ecr.us-east-1.amazonaws.com/association-group
	@echo Deploy para a AWS Lambda Function association-group feito com sucesso!

destroy:
	@echo Destruindo imagem docker...
	docker system prune -a -f