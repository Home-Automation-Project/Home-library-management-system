import os
import subprocess



docker build --build-arg COUCHDB_USER=myadmin --build-arg COUCHDB_PASSWORD=mypassword -t fastapi-couchdb .