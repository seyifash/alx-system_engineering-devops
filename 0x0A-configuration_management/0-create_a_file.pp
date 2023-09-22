# Puppet manifest to create a file in tmp with specific permissions and content

file { '/tmp/school':           # resource type file
  ensure  => 'file',            # Ensure it exist
  mode    => '0744',            # file permissions
  owner   => 'www-data',        # File owner is www-data
  group   => 'www-data',        # file group is www-data
  content => 'I love Puppet',   # file content
}
