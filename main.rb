#!/usr/bin/env ruby

require 'docsplit'
require 'mongo'


file_dest = '/home/matej/develop/zeptat/texts'

# parse functionality
# usage:
# ruby main.rb parse input
# where input file contains a list of pdf files to parse into text
if ARGV[0] == "parse" then
  filelist = ARGV[1]
  file = File.new(filelist, "r")

  File.foreach(file).with_index do |line, line_num|
    current_file = line.chomp!
    print "Parsing file: ", current_file, "\n"
    Docsplit.extract_text(current_file, :output => file_dest)
  end

  # get rid of whitespace lines
  Dir["/home/matej/develop/zeptat/texts/*txt"].each { |f|
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

# upload functionality
# usage:
# ruby main.rb upload files_to_upload
# where files_to_upload is the list of text files to upload to database
#
if ARGV[0] == "upload" then
  filelist_name = ARGV[1]
  file = File.open(filelist_name) or die "Unable to open #{filelist_name}"
  files, file_names = [],[]
  file.each_line do |line|
    cline = line.chomp!
    files << cline
    file_names << cline.gsub(".txt","")
  end
  print "debug ", file_names, "\n"

  file_location ="/home/matej/develop/zeptat/texts"

  # temp clean db, todo move to clean
  client = Mongo::Client.new([ '127.0.0.1:27017' ], :database => 'zeptat_db')
  client.database.drop

  # fire up db..todo add check that mongod is up
  db = Mongo::Client.new([ '127.0.0.1:27017' ], :database => 'zeptat_db')
  coll = db["ebook_collection"] # get mongodb collection

  # finally, upload lines from each txt ebook
  files.each_with_index do |f, f_index|
    File.foreach(file_location+'/'+f).with_index do |line, index|
      cline = line.chomp!
      print "debugging ", index, " line ", line, "\n"
      doc = {"title" => file_names[f_index], "line" => "line number: " + index.to_s + " " + cline}
      coll.insert_one(doc) # insert this document into mongodb
    end
    # counting is redundant but want to make sure they are in database
    print "Lines added for ", file_names[f_index], " ", coll.find({"title": /#{file_names[f_index]}/i}).count , "\n"
  end

  # return some logistics
  print "Total items in zeptat database collection: ", coll.find().count, "\n"

end


# query functionality
# usage:
# ruby main.rb query query_list
# where query_list is the list of queries to make upon the database
#
if ARGV[0] == "query" then
  q_list_name = ARGV[1]
  file = File.open(q_list_name) or die "Unable to open #{q_list_name}"
  queries = []
  file.each_line do |line|
    queries << line.chomp!
  end

  db = Mongo::Client.new([ '127.0.0.1:27017' ], :database => 'zeptat_db')
  coll = db["ebook_collection"] # get mongodb collection

  queries.each {|search_term|
    finds = coll.find({"line": /#{search_term}/i })
    finds.each {|document|
      print document,"\n" #=> Yields a BSON::Document.
    }
    print "Total number of lines found: ", finds.count, "\n"
  }

end


# clean functionality
# usage:
# ruby main.rb drop databases_to_drop
# where databases_to_drop is the list of databases to drop
if ARGV[0] == "clean" then
  # temp clean db, todo move to clean
  client = Mongo::Client.new([ '127.0.0.1:27017' ], :database => 'zeptat_db')
  client.database.drop
end






