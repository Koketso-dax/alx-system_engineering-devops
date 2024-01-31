#!/usr/bin/env ruby
regex = /hb{0,1}t{1}n/
read = ARGV[0].scan(regex)
for a in read do
puts(a)
end
