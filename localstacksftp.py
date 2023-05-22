import io
import time
import boto3
from ftplib import FTP, FTP_TLS
from logger import logger
import config
keys=config.keys

def create_transfer_api():
    transfer_client, s3_client = get_clients()

    logger.info('Creating FTP server in AWS Transfer API')
    role_arn = 'arn:aws:iam::testrole'

    rs = transfer_client.create_server(
        EndpointType='PUBLIC',
        IdentityProviderType='SERVICE_MANAGED',
        Protocols=['FTP']
    )
    time.sleep(1)

    server_id = rs['ServerId']
    port = int(server_id.split(':')[1])

    s3_client.create_bucket(Bucket=keys['BUCKET'])

    transfer_client.create_user(
        ServerId=server_id,
        HomeDirectory=keys['BUCKET'],
        HomeDirectoryType='PATH',
        Role=role_arn,
        UserName=keys['USERNAME']
    )
    logger.info(f" server id: {server_id}, port: {port}")
    return server_id, port


def upload_files(server_id, ftp_port, file, filename):
    transfer_client, s3_client = get_clients()
   
    ftp = FTP()
    print('Connecting to AWS Transfer FTP server on local port %s' % ftp_port)
    ftp.connect(host=keys['HOST_NAME'], port=ftp_port)

    # connect to FTP server
    result = ftp.login(keys['USERNAME'], keys['FTP_USER_DEFAULT_PASSWD'])
    assert 'Login successful.' in result

    # upload file to root dir
    logger.info('Uploading file to FTP root directory')
    retry(ftp.storbinary, cmd='STOR %s' % filename, fp=io.BytesIO(file))

    # upload file to sub dir
    logger.info('Uploading file to FTP sub-directory')
    ftp.mkd(keys['S3_DIR'])
    ftp.cwd(keys['S3_DIR'])
    retry(ftp.storbinary, cmd='STOR %s' % filename,fp=io.BytesIO(file))

    ftp.quit()


def download_files(server_id, ftp_port, file, filename):
    transfer_client, s3_client = get_clients()
    
    logger.info('Downloading files from S3 root and sub-directory')

    rs = s3_client.get_object(Bucket=keys['BUCKET'], Key=filename)
    assert rs['Body'].read() == file

    rs = s3_client.get_object(Bucket=keys['BUCKET'], Key='{}/{}'.format(keys['S3_DIR'], filename))
    assert rs['Body'].read() == file


def get_clients():
    return boto3.client('transfer', endpoint_url=keys['EDGE_URL']), boto3.client('s3', endpoint_url=keys['EDGE_URL'])

# copied from localstack, to avoid "connection refused" errors

def retry(function, retries=3, sleep=1.0, sleep_before=0, **kwargs):
    raise_error = None
    if sleep_before > 0:
        time.sleep(sleep_before)
    retries = int(retries)
    for i in range(0, retries + 1):
        try:
            return function(**kwargs)
        except Exception as error:
            raise_error = error
            time.sleep(sleep)
    raise raise_error

def test():
    server_id, ftp_port = create_transfer_api()
    upload_files(server_id, ftp_port, b'title "Test" \nfile content!!', keys['S3_FILENAME'])
    download_files(server_id, ftp_port, b'title "Test" \nfile content!!', keys['S3_FILENAME'])
    print('Tests succesfully completed.')

if __name__=='__main__':
    test()