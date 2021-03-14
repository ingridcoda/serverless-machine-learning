mak.SILENT:

install:
	pip install -r requirements/base.txt

deploy:
	@echo Construindo imagem docker para deploy...
	docker build -t regression .
	@echo Imagem construída com sucesso!
	@echo Fazendo deploy para a AWS Lambda Function regression...
	docker tag regression:latest 274877485409.dkr.ecr.us-east-1.amazonaws.com/regression
	docker push 274877485409.dkr.ecr.us-east-1.amazonaws.com/regression
	@echo Deploy para a AWS Lambda Function regression feito com sucesso!

destroy:
	@echo Destruindo imagem docker...
	docker system prune -a -f