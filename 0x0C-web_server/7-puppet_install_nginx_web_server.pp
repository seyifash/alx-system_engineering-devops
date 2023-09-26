# configuring an nginx server using puppet

package { 'nginx':
  ensure => installed,
}

file { 'var/www/html/index.html':
  content => 'Hello World!',
}

file_content { 'configs':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'server_name _;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent',
}
service { 'nginx':
  ensure  => running,
  require => package['nginx'],
} 
