#!/usr/bin/env ruby
regex = /^[0-9]{10}$/
read = ARGV[0].scan(regex)
for a in read do
 print(a)
end
print("\n")
