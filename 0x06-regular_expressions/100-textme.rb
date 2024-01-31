#!/usr/bin/env ruby
regex = /(from:)(\+?[A-Za-z0-9]+)(...)(to:)(\+?[A-Za-z0-9]+)(...)(flags:)((-?[0|1]:?)+)/
read = ARGV[0].scan(regex)
print(read[0][1] + "," + read[0][4] + "," + read[0][7])
print("\n")!/usr/bin/en rube
