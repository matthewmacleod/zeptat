#!/usr/bin/env ruby

require 'docsplit'


filename = ARGV[0]
file = File.new(filename, "r")
file_path = file.gets.chomp!

file_source = file_path
file_dest = '/home/matej/develop/efind/texts'

Docsplit.extract_text(file_source, :output => file_dest)

