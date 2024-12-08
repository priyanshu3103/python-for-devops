import boto3

s3= boto3.resource('s3')

def list_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3):
    s3.create_bucket(Bucket="python-for-devops")
    print("Bucket creates successfully")
create_bucket(s3)
# list_buckets(s3)

# def backup_upload(s3, file_name, bucket_name, key_name):
#     data= open(file_name, 'rb')
#     s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
#     print("Backup uploaded successfully")

# region='us-east-1'
# file_name= "/mnt/c/Users/priya/Desktop/python zero to hero/backups/backup_2024-12-06.tar.gz"
# bucket_name="backup-data1"
# key_name='python-backup.tar.gz'

# backup_upload(s3, file_name, bucket_name, key_name)