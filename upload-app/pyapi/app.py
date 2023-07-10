import os

from minio import Minio
from flask import Flask, request
from flask_cors import CORS


UPLOAD_BUCKET = os.environ['UPLOAD_BUCKET']

app = Flask(__name__)
CORS(app)

client = Minio(
    endpoint=os.environ['MINIO_ENDPOINT'],
    access_key=os.environ['MINIO_ROOT_USER'],
    secret_key=os.environ['MINIO_ROOT_PASSWORD'],
    secure=False
)


@app.post('/upload-url')
def get_presigned_url():
    object_name = request.json.get('filename')
    if object_name is None:
        return {'error': "The request must contain a 'filename' property"}
    url = client.presigned_put_object(UPLOAD_BUCKET, object_name)
    return {'url': url}
    

if __name__ == '__main__':
    if not client.bucket_exists(UPLOAD_BUCKET):
        client.make_bucket(UPLOAD_BUCKET)
        print(f'Created bucket "{UPLOAD_BUCKET}"')
    print(f'Bucket "{UPLOAD_BUCKET}" already exists')
    app.run('0.0.0.0')
