#!/usr/bin/env bash
# using puppet to connect without password

file { '/root/.ssh/config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => "IdentityFile /root/.ssh/school\nPasswordAuthentication no\n",
}
