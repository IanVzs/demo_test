puts nil
puts true, false
puts 12, -21, 19_i64, 34_u32, 64_u8
puts 1.0, 1.0_f32, 1e1
puts 'a', '\n', '换'
puts "字符串们🚪"
puts "#{:symbol}, #{:"foo bar"}"
puts "#{[1,2,3]}, #{[3,2,1] of Int32}Int32"
_set = Set{5,6,7}
puts "set: Array-like#{_set}"
puts "range: #{1..9} to_a: #{(1..9).to_a}, #{1...10}: to_a: #{(1...10).to_a}"


puts ""
aaa = {"one" => 1, "two" => 2}
puts "key-value Hash Type: aaa: #{aaa}, aaa[\"one\"]: #{aaa["one"]}"



puts ""
puts "2==1 -> #{2 == 1}"
puts "2&&1 -> #{2 && 1}"
puts "2||1 -> #{2 || 1}"
