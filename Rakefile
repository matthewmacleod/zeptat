require 'rake/testtask'
require 'fileutils'


Rake::TestTask.new do |t|
  t.libs.push "lib"
  t.test_files = FileList['test/*_test.rb']
  t.verbose = true
end

# parse pdfs in file named "input"
task :parse do
  puts "Parsing files..."
  start = Time.now
  output = `ruby main.rb parse input`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end

# upload files in file named "files_to_upload" to database
task :upload do
  puts "Uploading files to database..."
  start = Time.now
  output = `ruby main.rb upload files_to_upload`
  finish = Time.now
  diff = finish - start
  dm = diff.divmod(60)
  puts output
  puts "Finished, run time: " + dm[0].to_s + " minutes " + dm[1].round(1).to_s + " seconds."
end

#query the database for strings in file named "queries"
#task :find do
#end


