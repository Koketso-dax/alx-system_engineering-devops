#!/usr/bin/env ruby
regex = /hb{0,1}t+n/
read = ARGV[0].scan(regex)
for a in read do
  print(a)
end
print("\n")
