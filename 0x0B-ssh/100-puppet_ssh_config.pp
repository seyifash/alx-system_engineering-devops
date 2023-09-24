#!/usr/bin/env bash
# using puppet to connect without password

class ssh {
file { '/etc/ssh/sshd_config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => "IdentityFile /root/.ssh/school\nPasswordAuthentication no\n",
}
}
