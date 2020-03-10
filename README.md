
# S3 Test

Testing AWS S3 with python using docker container

## Getting Started

Download the container image

```
docker pull satishvis/flasks3test
```

### Prerequisites

Docker

Python latest version

### Installing

The docker image does not contain the credentials to the AWS account. Hence the following steps are required.

After pulling docker image, create a .env_file.

It should contain the following

S3_KEY=`<YOUR S3_KEY>`

S3_SECRET=`<YOUR S3_SECRET>`

BUCKET=`<THE BUCKET NAME>`

You may also want to link a local volume to ensure that the docker image does not store images locally in its /app/uploads folder.

In order to pass the env variable mentioned in the above env file and mount the local volume you need to start the docker container with this following command or variations thereto:

```
docker run --name s3test --env-file=.env_file -it -d -p 5000:5000 -v ~/tmp:/app/uploads satishvis/flasks3test
```

Now you can open the http://localhost:5000 to see your bucket.


## Authors

* Satish Viswanathan
