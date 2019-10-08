# Manifest to change the user limits
file {'/etc/security/limits.conf':
    ensure  => file,
    content => "holberton hard nofile 5000\nholberton soft nofile 4000\n"
}
