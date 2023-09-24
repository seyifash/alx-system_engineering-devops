# ensuring ssh config maintains state

class { 'stdlib': }

file {'/etc/ssh/ssh_config':
  ensure => present
}
include stdlib

file_line {'Declare identity files':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentifyFile ~/.ssh/school',
  replace => true,
}

file_line {'Turn off password auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}
