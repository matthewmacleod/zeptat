#!/usr/bin/env ruby

require 'docsplit'
require 'mongo'


file_dest = '/home/matej/develop/efind/texts'

filelist = ARGV[0]
file = File.new(filelist, "r")

File.foreach(file).with_index do |line, line_num|
  current_file = line.chomp!
  Docsplit.extract_text(current_file, :output => file_dest)
end


