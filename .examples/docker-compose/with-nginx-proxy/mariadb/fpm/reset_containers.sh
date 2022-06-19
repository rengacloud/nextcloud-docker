docker-compose stop
docker-compose rm -f
docker volume rm $(docker volume ls -q)
docker-compose build --pull
docker-compose up -d
sleep 30
/bin/bash ../../../../../rengacloud/initial_setup.sh