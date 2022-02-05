tutorial mongodb install docker:

https://dev.to/sonyarianto/how-to-spin-mongodb-server-with-docker-and-docker-compose-2lef

connect to mongodb
https://www.bmc.com/blogs/mongodb-docker-container/

tutorial: https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

Change ownership of volume in docker volumes:

(ubuntu): chown -R $USER:$USER /var/lib/docker/volumes/volume-name

then build the image:
```bash
docker-compose build --build-arg UID=$(id -u) && docker-compose up -d
```
to read the documentation:
```bash
cd docs/
make html
```