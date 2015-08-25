#!/usr/bin/env ruby

require 'docsplit'

file_dest = 'texts'

# parse functionality
# usage:
# ruby main.rb parse input
# where input file contains a list of pdf files to parse into text

if ARGV[0] == "input" then
  filelist = ARGV[0]
  file = File.new(filelist, "r")

  File.foreach(file).with_index do |line, line_num|
    current_file = line.chomp!
    print "Parsing file: ", current_file, "\n"
    Docsplit.extract_text(current_file, :output => file_dest)
  end

  # get rid of whitespace lines
  Dir[file_dest+"/*.txt"].each { |f|
    puts "file : " + f
    lines = []
    # use this to avoid slurping whole file into memory
    File.foreach(f) do |line|
      current_line = line.chomp!
      if current_line =~ /\w+/
        current_line.gsub!("�","")
        current_line.gsub!('',"")
        current_line.gsub!('',"")
        lines << current_line
      end
    end
    lines << "\n"
    File.open(f, 'w') {|fi| fi.write lines.join("\n")}
  }
end







