# Flask App and AWS File Transfer

Example file transfer with flask app and docker sftp server for learning/testing purposes.

_\*note:_ to use the sftp.localstack version of this to emulate aws transfer family set up you will need a localstack API key (free trial, then changes to a monthly subscription).

The local version should work without keys or env vars

## References and Resources

[baermat Github Repo](https://github.com/localstack/localstack-pro-samples/tree/master/transfer-ftp-s3)

[Leiland - Medium Article](https://medium.com/@lejiend/create-sftp-container-using-docker-e6f099762e42)

[Edward S. - Hostinger-Tutorial](https://www.hostinger.my/tutorials/how-to-use-sftp-to-safely-transfer-files/)

##### Other References:

[Flask Docs](https://flask.palletsprojects.com/en/2.2.x/)

[Local Stack Docs](https://docs.localstack.cloud/getting-started/installation/)

[Python Env Vars](https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5)

[Color Logs](https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output)

## Run in Project:

Env vars:

- change the variables in localsftp if not using localstack, and update the .env file with relevqnt env vars if using localstack with API key

- Create virtualenv:
  `python3 -m venv venv`

- Install dependencies:
  `pip3 -r requirements.txt`

- Localstack (only if you have an Localstack api key):
  `make run-localstack`

- Docker SFTP server:
  `make run-sftp`

- Flask App:
  `make run-flask`
