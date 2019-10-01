exec { 'Append a line to /var/www/html/wp-settings.php':
  command => "sed -i \"s|.*phpp.*|require_once(\
 ABSPATH . WPINC . '/class-wp-locale.php' );|\" /var/www/html/wp-settings.php",
  path    => '/bin',
}
