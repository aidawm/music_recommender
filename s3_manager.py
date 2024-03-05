import boto3
from botocore.exceptions import ClientError
import json
from fileinput import filename 

class S3:
    def __init__(self) -> None:
         data_address = "configs.json"
         f = open(data_address)
         self.configs = json.load(f)
         self.configs = self.configs["s3"]   
         self.connect_to_s3()


    def connect_to_s3(self):
        try:
            self.s3_resource = boto3.resource(
                's3',
                endpoint_url=self.configs["endpoint_url"],
                aws_access_key_id=self.configs["aws_access_key_id"],
                aws_secret_access_key=self.configs["aws_secret_access_key"]
            )

        except Exception as exc:
            logging.error(exc)

        else:
            # bucket
            self.bucket = self.s3_resource.Bucket('cloudmusic')
   
   
    def upload_object(self,id,file):
        id = str(id) + ".mp3"
        file.filename = id
        self.bucket.Object(file.filename).put(Body=file.read())

   