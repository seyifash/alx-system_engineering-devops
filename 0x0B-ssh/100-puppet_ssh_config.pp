# using puppet to connect without password

file { '/etc/ssh/ssh_config':
  ensure => present
}

file_line { 'identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentifyFile ~/.ssh/school',
}

file_line { 'password auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}
