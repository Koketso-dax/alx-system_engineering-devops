# This script increases the amount of traffic an Nginx server can handle

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
exec { 'nginx-restart':
  command => '/usr/sbin/service nginx restart',
  path    => ['/usr/sbin', '/sbin', '/bin', '/usr/bin'],
}
