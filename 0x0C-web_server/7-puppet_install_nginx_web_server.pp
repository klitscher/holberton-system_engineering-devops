#Sets up server with nginx

exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}

Exec['apt-update'] -> Package <| |>

package {'nginx':
  ensure => latest,
  name   => 'nginx',
}


file { 'index':
  ensure  => 'present',
  require => Package['nginx'],
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
}


file { 'config':
  ensure  => 'present',
  require => Package['nginx'],
  path    => '/etc/nginx/sites-available/default'
  content => 'server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    location /redirect_me {
    return 301 http://example.com/;'
}
