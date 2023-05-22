include .env
export $(shell sed 's/=.*//' .env)

usage:       ## Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

install:     ## Install dependencies
	@which localstack || pip3 install localstack
	@which awslocal || pip3 install awscli-local

run-flask:	## Run flask app
	@echo "Running Test: Creating FTP server and uploading files to S3 via Transfer API"; \
	(source venv/bin/activate; python3 main.py)

run-sftp:
	docker-compose up -d sftp

run-localstack:
	docker-compose up -d localstack

stop: ## stop localstack
	@echo
	docker-compose down

ready:
	@echo Waiting on the LocalStack container...
	@localstack wait -t 30 && echo Localstack is ready to use! || (echo Gave up waiting on LocalStack, exiting. && exit 1)

logs:
	@localstack logs > logs.txt

.PHONY: usage install start run stop ready logs test-ci
