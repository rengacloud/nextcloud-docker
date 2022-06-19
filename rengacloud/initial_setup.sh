docker exec -it --user www-data app php occ app:disable theming
docker exec -it --user www-data app php occ app:disable firstrunwizard
docker exec -it --user www-data app php occ app:install groupquota
docker exec -it --user www-data app php occ config:system:set theme --value="rengacloud"
docker exec -it --user www-data app php occ maintenance:theme:update
docker exec -it --user www-data app php occ config:system:set skeletondirectory --value=""
docker exec -it --user www-data app php occ config:system:set knowledgebaseenabled --value="false" --type=boolean
docker exec -it --user www-data app php occ config:system:set default_language --value="ru"
docker exec -it --user www-data app php occ config:system:set default_locale --value="ru_RU"
