import os
from minio import Minio
from minio.error import ResponseError

client = Minio('192.168.1.199:81',
                  access_key='minioadmin',
                  secret_key='minioadmin',secure=False)

try:
    data = client.get_partial_object('testbucket', 'test.jpg', offset=1000, length=0, request_headers=None)
    with open('test.jpg', 'wb') as file_data:
        for d in data:
            file_data.write(d)
except ResponseError as err:
    print(err)
