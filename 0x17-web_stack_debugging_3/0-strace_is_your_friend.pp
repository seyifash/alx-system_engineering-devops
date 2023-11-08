# fix the file that has the line "phpp" instead of php in the file "wp-settings.php" which causes a 500 error
exec {'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
