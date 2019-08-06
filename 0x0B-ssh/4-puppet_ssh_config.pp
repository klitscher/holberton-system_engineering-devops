# Puppet file to set up configuration of server

file_line {
  'Turn off passwd auth':
    ensure             => 'present',
    path               => '/etc/ssh/ssh_config',
    line               => 'PasswordAuthentication no',
    match              => '^*.PasswordAuthentication yes$',
    append_on_no_match => true,
}

file_line {
  'Declare identity file':
    ensure             => 'present',
    path               => '/etc/ssh/ssh_config',
    line               => 'IdentityFile ~/.ssh/holberton',
    match              => '^IdentityFile',
    multiple           => true,
    append_on_no_match => true,
}
