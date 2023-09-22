# Puppet manifest that kills a process named killmenow

exec { 'kill-killmenow':
  command  => 'pkill -f killmenow',
  onlyif   => 'pgrep -f killmenow',
  path     => ['/bin', '/usr/bin'],
  provider => shell,
  returns  => '0',
}
