include .env
export $(shell sed 's/=.*//' .env)

export LOCALSTACK_API_KEY

usage:       ## Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

install:     ## Install dependencies
	@which localstack || pip3 install localstack
	@which awslocal || pip3 install awscli-local


run-test:         ## Deploy and run the sample locally
	@echo "Running Test: Creating FTP server and uploading files to S3 via Transfer API"; \
		(Python3 sftp.py)

run-flask:	## Run flask app
	@echo "Running Test: Creating FTP server and uploading files to S3 via Transfer API"; \
	Python3 main.py


run-localstack: ## run localstack
	LOCALSTACK_API_KEY=$(LOCALSTACK_API_KEY) DEBUG=1 localstack start -d

stop-localstack: ## stop localstack 
	@echo
	localstack stop

ready:
	@echo Waiting on the LocalStack container...
	@localstack wait -t 30 && echo Localstack is ready to use! || (echo Gave up waiting on LocalStack, exiting. && exit 1)

logs:
	@localstack logs > logs.txt

test-ci:
	make start install ready run; return_code=`echo $$?`;\
	make logs; make stop; exit $$return_code;
	
.PHONY: usage install start run stop ready logs test-ci
