docker-compose stop
docker-compose rm -f
docker volume rm $(docker volume ls -q)
docker-compose build --pull
docker-compose up -d
sleep 20
/bin/bash ./initial_setup.sh