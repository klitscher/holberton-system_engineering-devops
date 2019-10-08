# Puppet script to fix another server
service { 'nginx':
  ensure => 'running',
  enable => true,
}

file { '/etc/default/nginx':
    ensure  => file,
    notify  => Service['nginx'],
    content => 'ULIMIT="-n 1048576"',
}
