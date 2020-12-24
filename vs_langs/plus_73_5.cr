puts "*****************Crystal************************"

def main()
        _start, _end = 0, 0
        #_start = Time.monotonic
        iplus, i = 0, 0
        elapsed_time = Time.measure do
                iplus, i = go()
        end
        #_end = Time.monotonic
        puts "loop result: #{i}"
        puts "pow result: #{iplus}"
        t_diff(_start, _end, elapsed_time)
end

def go()
        i = 0
        iplus = 73**5
        until i == iplus
                i += 1
        end
        {iplus, i}
end

def t_diff(_start, _end, elapsed_time)
        puts _end, _start, elapsed_time
        s = elapsed_time || _end - _start
        puts "all cost s: #{s},   u: <-"
end

main()
