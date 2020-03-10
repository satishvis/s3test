import boto3


class S3:
    def __init__(self, aws_access_key_id, aws_secret_access_key):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key)
        self.s3 = boto3.resource(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key)

    def upload_file(self, file_name, bucket):
        """
        Function to upload a file to an S3 bucket
        """
        object_name = file_name.split('/')[-1]
        response = self.s3_client.upload_file(file_name, bucket, object_name)

        return response

    def download_file(self, file_name, bucket):
        """
        Function to download a given file from an S3 bucket
        """
        output = f"downloads/{file_name}"
        self.s3.Bucket(bucket).download_file(file_name, output)

        return output

    def delete_file(self, file_name, bucket):
        '''
        Function to delete a file from an S3 bucket
        '''
        self.s3.Object(bucket, file_name).delete()

    def list_files(self, bucket):
        """
        Function to list files in a given S3 bucket
        """
        contents = []
        try:
            for item in self.s3_client.list_objects(Bucket=bucket)['Contents']:
                contents.append(item)
        except KeyError:
            print("No contents available")
            contents.append("No items in the bucket... Add some...")
        return contents
