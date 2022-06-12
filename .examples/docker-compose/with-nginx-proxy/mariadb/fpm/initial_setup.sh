docker-compose exec --user www-data app php occ app:disable theming
docker-compose exec --user www-data app php occ app:disable firstrunwizard
docker-compose exec --user www-data app php occ app:install groupquota
docker-compose exec --user www-data app php occ config:system:set theme --value="rengacloud"
docker-compose exec --user www-data app php occ maintenance:theme:update
docker-compose exec --user www-data app php occ config:system:set skeletondirectory --value=""
docker-compose exec --user www-data app php occ config:system:set knowledgebaseenabled --value="false" --type=boolean
docker-compose exec --user www-data app php occ config:system:set default_language --value="ru"
docker-compose exec --user www-data app php occ config:system:set default_locale --value="ru_RU"
docker-compose exec --user www-data app php occ config:system:set trusted_domains 1 --value="storage.rengacloud.ru"

