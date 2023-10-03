# configure to include a custom http header
exec { 'update sytem':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'installed',
  require => Exec['update system']
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'configs':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

exec {'HTTP header':
  command  => sudo sed -i "server_name _;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default,
  provider => shell,
}

service { 'nginx':
  ensure => running,
  require => package['nginx'],
}
