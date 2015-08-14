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

# MongoDB testing

# upload files in file named "files_to_upload" to database
# might want to do this since there is a lot of output
# rake upload > out
task :upload do
  puts "Uploading files to Zeptat Mongo database..."
  start = Time.now
  output = `ruby main.rb upload files_to_upload true`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end

# find ie, query the database for strings in file named "queries"
# rake query
task :query do
  puts "Quering the Zeptat Mongo database..."
  start = Time.now
  output = `ruby main.rb query query_list true | grep -v ^D`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end

# find ie, query the database for strings in file named "queries"
# rake query_count
task :query_count do
  puts "Getting query counts in the Zeptat Mongo database..."
  start = Time.now
  output = `ruby main.rb query_count query_list | grep -v ^D`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end

task :drop do
  puts "Removing Zeptat Mongo database"
  start = Time.now
  output = `ruby main.rb clean`
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



