# Home-library-management-system
Manage your home library of books

## Features
- [ ] Lookup by isbn, author, title, keyword, genre, LC id, dewy decimal
- [ ] Containerized
- [ ] Can run on a Raspberry Pi, Home Assistant, docker or native
- [ ] Database backend
- [ ] Track lending a book
- [ ] Remind borrower
- [ ] Track book location
- [ ] library may include: books; ebooks; audio book; plex library movies and shows
- [ ] Book information includes: author, title, publisher, year, ISBN, simple annotation, genre (list), cover art, cover type (paper, hard, leather)
- [ ] Backup/restore db

# Installation
## Create docker image

## Run dockerfile
docker run -p 8000:8000 -p 5984:5984 -e COUCHDB_USER=myadmin -e COUCHDB_PASSWORD=mypassword fastapi-couchdb
