#!/usr/bin/env ruby

require 'docsplit'
require 'mongo'


file_dest = '/home/matej/develop/zeptat/texts'

if ARGV[0] == "parse" then
  filelist = ARGV[1]
  file = File.new(filelist, "r")

  File.foreach(file).with_index do |line, line_num|
    current_file = line.chomp!
    Docsplit.extract_text(current_file, :output => file_dest)
  end

  # get rid of whitespace lines
  Dir["/home/matej/develop/zeptat/texts/*txt"].each { |f|
    puts "file : " + f
    lines = []
    fopen = File.open(f) or die "Unable to open file..."
    fopen.each_line do |line|
      #binding.pry
      current_line = line.chomp!
      #puts "current line: " + current_line
      if current_line =~ /\w+/
        current_line.gsub!("�","")
        current_line.gsub!('',"")
        current_line.gsub!('',"")
        lines << current_line
      end
    end
    File.open(f, 'w') {|fi| fi.write lines.join("\n")}
  }

end


if ARGV[0] == "upload" then
  filelist = ARGV[1]
  file = File.new(filelist, "r")

  db = Mongo::Client.new([ '127.0.0.1:27017' ], :database => 'zeptat_db')
  db.collection_names.each { |name| puts name }
  coll = db["Ebook_Collection"] # get mongodb collection

  File.foreach(file).with_index do |line, line_num|
    current_file = line.chomp!
    file_txt = File.open(file_dest+'/'+current_file, "rb")
    file_string = file_txt.read
    file_txt.close
    doc = {"name" => current_file, "content" => file_string}
    coll.insert(doc) # insert this document into mongodb
  end

end
