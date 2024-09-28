import boto3
from datetime import datetime
import os

def upload_to_s3(bucket_name, s3_file_path, local_file_path, partition=False):
    s3 = boto3.client('s3')
    s3_key = os.path.basename(s3_file_path)

    if (partition):
      partition_date = datetime.now().strftime('%Y-%m-%d')
      s3_key = f"date={partition_date}/{os.path.basename(s3_file_path)}"

    s3.upload_file(local_file_path, bucket_name, s3_key)
