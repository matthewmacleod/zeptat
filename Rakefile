require 'rake/testtask'
require 'fileutils'


Rake::TestTask.new do |t|
  t.libs.push "lib"
  t.test_files = FileList['test/*_test.rb']
  t.verbose = true
end

# parse pdfs in file named "input"
# rake parse
task :parse do
  puts "Parsing files for Zeptat database..."
  start = Time.now
  output = `ruby lib/parse.rb input`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end


### Mongo testing ###

# upload files in file named "files_to_upload" to database
# rake upload_mongo
task :upload do
  puts "Uploading files to Zeptat Mongo database..."
  start = Time.now
  output = `python3 lib/mongo_zeptat.py upload`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end

# search for query term based on titles in "files_to_upload" to database
# rake query
task :query do
  puts "Searching files in Zeptat Mongo database..."
  start = Time.now
  output = `python3 lib/mongo_zeptat.py query`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end

# count query hits based on titles named "files_to_upload" in zeptat database
# rake query_count
task :query_count do
  puts "Searching files in Zeptat Mongo database..."
  start = Time.now
  output = `python3 lib/mongo_zeptat.py query_count`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end


# query a specific file in  "files_to_upload" in zeptat database
# rake query_title name='title'
task :query_title do
  puts "Searching title in Zeptat Mongo database..."
  title = ENV['name']
  start = Time.now
  output = `python3 lib/mongo_zeptat.py query_title #{title}`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end


# return all lines
# rake query_lines
task :query_lines do
  puts "Searching titles in Zeptat Mongo database..."
  start = Time.now
  output = `python3 lib/mongo_zeptat.py query_lines`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end

# to remove ebook database
# rake drop
task :drop do
  puts "Removing Zeptat Mongo database..."
  start = Time.now
  output = `python3 lib/mongo_zeptat.py drop`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end




### Cassandra testing ###

# upload files in file named "files_to_upload" to database
# rake upload_cassandra > out
task :upload_cassandra do
  puts "Uploading files to Zeptat Cassandra database..."
  start = Time.now
  output = `python lib/cassandra_zeptat.py upload`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end

# query uploaded files from file named "files_to_upload" to database
# query term is based on those in query_list file
task :query_cassandra do
  puts "Searching Zeptat Cassandra database..."
  start = Time.now
  output = `python lib/cassandra_zeptat.py query`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end


### PostgreSQL testing ###

# upload files in file named "files_to_upload" to database
# rake upload_postgres
task :upload_postgres do
  puts "Uploading files to Zeptat PostgreSQL database..."
  start = Time.now
  output = `python lib/postgres_zeptat.py upload`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end

# query uploaded files from file named "files_to_upload" to database
# query term is based on those in query_list file
# rake query_postgres
task :query_postgres do
  puts "Searching Zeptat PostgreSQL database..."
  start = Time.now
  output = `python lib/postgres_zeptat.py query`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end



