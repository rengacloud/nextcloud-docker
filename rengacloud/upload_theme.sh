#!/bin/sh
set -eu

# version_greater A B returns whether A > B
version_greater() {
    [ "$(printf '%s\n' "$@" | sort -t '.' -n -k1,1 -k2,2 -k3,3 -k4,4 | head -n 1)" != "$1" ]
}

# return true if specified directory is empty
directory_empty() {
    [ -z "$(ls -A "$1/")" ]
}

run_as() {
    if [ "$(id -u)" = 0 ]; then
        su -p www-data -s /bin/sh -c "$1"
    else
        sh -c "$1"
    fi
}

docker run --rm --volumes-from app -v $(pwd)/rengacloud/themes/rengacloud:/theme alpine cp -a /theme/. /var/www/html/themes/rengacloud/
docker exec app chown -R www-data:root themes
docker exec -it --user www-data app php occ maintenance:theme:update
docker stop proxy
docker start proxy