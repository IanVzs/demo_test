def test():
    print("generator start")
    n = 1
    while True:
        yield_value = yield n
        print(f"yield_value: {yield_value}")
        n+=1
        if n > 2:
            n = "666" # 重赋值生成器返回值

generator = test()

next_value = generator.__next__()
print(f"next: {next_value}")


send_666 = generator.send("hello_yield")# 赋值给yield_value hello_yield
send_666_next = generator.__next__()    # 赋值给yield_value None
print(f"send_666: {send_666}, next: {send_666_next}")
