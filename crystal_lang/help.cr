require "option_parser"

OptionParser.parse do |parser|
  parser.banner = "Welcome to The Beatles App!" 
  
  parser.on "-h", "--help", "Show help" do
    puts parser
    exit
  end

  parser.on "-v", "--version", "Show version" do
    puts "version 1.0" 
    exit
  end
  
end
