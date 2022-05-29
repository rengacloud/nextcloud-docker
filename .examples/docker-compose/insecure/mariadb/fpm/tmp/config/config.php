<?php
$CONFIG = array (
  'memcache.local' => '\\OC\\Memcache\\APCu',
  'apps_paths' => 
  array (
    0 => 
    array (
      'path' => '/var/www/html/apps',
      'url' => '/apps',
      'writable' => false,
    ),
    1 => 
    array (
      'path' => '/var/www/html/custom_apps',
      'url' => '/custom_apps',
      'writable' => true,
    ),
  ),
  'memcache.distributed' => '\\OC\\Memcache\\Redis',
  'memcache.locking' => '\\OC\\Memcache\\Redis',
  'redis' => 
  array (
    'host' => 'redis',
    'password' => '',
    'port' => 6379,
  ),
  'passwordsalt' => 'Z6djH/J62l3iwWqvtR2Gcb39sf1H6D',
  'secret' => '6b1fQ0VPs3Lu0dZIY+bk15G4jVpiqzeItOS4l04CYjbGkjYA',
  'trusted_domains' => 
  array (
    0 => 'localhost',
  ),
  'datadirectory' => '/var/www/html/data',
  'dbtype' => 'mysql',
  'version' => '24.0.1.1',
  'overwrite.cli.url' => 'http://localhost',
  'dbname' => 'rengacloud_storage',
  'dbhost' => 'db',
  'dbport' => '',
  'dbtableprefix' => 'oc_',
  'mysql.utf8mb4' => true,
  'dbuser' => 'rengacloud_storage',
  'dbpassword' => 'password123456',
  'installed' => true,
  'instanceid' => 'ocnlcbzdmat1',
  'theme' => 'rengacloud',
  'skeletondirectory' => '',
  'knowledgebaseenabled' => false,
  'default_language' => 'ru',
  'default_locale' => 'ru_RU',
);
