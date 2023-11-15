# enable the user holberton to log in and open files without error
exec {'change-os-configuration-for-holberton-user-hardfile':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

exec {'change-os-configuration-for-holberton-user-softfile':
  command => "sed -i '/^holberton soft/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
