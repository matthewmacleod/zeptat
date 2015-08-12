require 'rake/testtask'
require 'fileutils'


Rake::TestTask.new do |t|
  t.libs.push "lib"
  t.test_files = FileList['test/*_test.rb']
  t.verbose = true
end

# parse pdfs in file named "input"
task :parse do
  puts "Parsing files for Zeptat database..."
  start = Time.now
  output = `ruby main.rb parse input`
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

task :clean do
  puts "Removing Zeptat Mongo database"
  start = Time.now
  output = `ruby main.rb clean`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end

# Cassandra testing
# upload files in file named "files_to_upload" to database
# might want to do this since there is a lot of output
# rake upload > out
task :upload_cassandra do
  puts "Uploading files to Zeptat Cassandra database..."
  start = Time.now
  output = `python zeptat.py`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end

# find ie, query the database for strings in file named "queries"



# PostgreSQL testing


