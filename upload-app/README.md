# Simple upload app

This app provides a form that uploads a file to a storage bucket by using a presigned URL. To run the app locally you need to have [Docker](https://www.docker.com/) installed.

Parts of the application:
- [Next.js](https://nextjs.org/) frontend
- Python API
- [MinIO](https://min.io/) object storage (equivalent to AWS S3)


## Running the app locally with Docker

### Editing your `hosts` file
First you need to edit your `hosts` file, on Windows it is `C:\Windows\System32\drivers\etc\hosts`. To edit it, start Notepad as administrator, open the `hosts` file and add the following lines at the end of the file:
```
127.0.0.1 storage
127.0.0.1 pyapi
```
This is to enable your host system to resolve the hostnames in the Docker network where the application containers will run.

### Building and running the app
Make sure you are in the directory where this README file is located and run:
```
docker-compose up -d
```
The frontend of the app will be available at `localhost:3000`. The file storage server GUI will be available at `localhost:9090` (username: `admin`, password: `asdfasdf`).
