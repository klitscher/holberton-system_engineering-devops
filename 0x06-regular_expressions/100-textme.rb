#!/usr/bin/env ruby
puts ARGV[0].scan(/.*from:(\W?\w+).*to:(\W?\w+).*flags:([\W\d:?][^\[^\]]*)/).join(',')
