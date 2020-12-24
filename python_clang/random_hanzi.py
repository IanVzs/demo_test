import random
import hashlib

def unicode_name(user_id):
    m = hashlib.md5()
    m.update(user_id.encode())
    smd5 = m.hexdigest()
    sint = [i for i in smd5 if i in '1234567890']
    user_info = []
    name_list = []
    for i in sint:
        if len(name_list) < 4:
            name_list.append(i)
            continue
        elif len(name_list) == 4:
            sint = ''.join(name_list)
            iint = int(sint)
            print(iint)
            name_list = []
            info = {"user_name": chr(20000+iint)+chr(30000-iint), "user_id": iint}
            if info not in user_info:
                user_info.append(info)
    return user_info

def random_words(num):
    words = []
    for i in range(num):
        val = random.randint(0x4e00, 0x9fbf)
        words.append(chr(val))
    return ''.join(words)

if __name__ == "__main__":
    user_id = "23"
    print(unicode_name(user_id))
    print(random_words(7))
