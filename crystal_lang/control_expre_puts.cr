a = 0
puts "Input a is #{a}"
if a > 0
    a = 1
elsif a == 0
    # 可类型转换诶....
    a = "Yeah"
else
    a = 0
end
puts a


a = 1 > 2 ? 3 : 4
puts "1 > 2 ? 3 : 4  -> #{a}"
a = 1 < 2 ? 3 : 4
puts "1 < 2 ? 3 : 4  -> #{a}"


case a
when 3, 2
    puts "a in [3, 2]"
when 4
    puts "a is 4"
else
    puts "a not in [2, 3, 4]"
end
