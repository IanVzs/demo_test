channel = Channel(Int32).new
total_lines = 0
files = Dir.glob("*.cr")

files.each do |f|
    spawn do
        lines = File.read_lines(f)
        puts "#{f} lines: #{lines.size}"
        channel.send lines.size
    end
end

files.size.times do
    total_lines += channel.receive
end

puts "", "all file lines: #{total_lines}"
