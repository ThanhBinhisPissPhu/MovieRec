docker run \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="movielens" \
-v $(pwd)/postgres:/var/lib/postgresql/data:rw \
-p 5432:5432 \
postgres:13

pgcli --host localhost --user root --port 5432 --dbname movielens

docker run -it \
-e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
-e PGADMIN_DEFAULT_PASSWORD="root" \
-p 8080:80 \
dpage/pgadmin4


###### Network ######

docker network create pgnetwork


docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="movielens" \
-v $(pwd)/postgres:/var/lib/postgresql/data:rw \
-p 5432:5432 \
--network pgnetwork \
--name pgdatabase \
postgres:13


docker run -it \
-e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
-e PGADMIN_DEFAULT_PASSWORD="root" \
-p 8080:80 \
--network pgnetwork \
--name pgadmin \
dpage/pgadmin4