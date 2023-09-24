#!/usr/bin/env bash
# using puppet to connect without password

ssh_client_config {
file { ' ~/.ssh/config':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => "IdentityFile ~/.ssh/school\nPasswordAuthentication no\n",
}
}
