rule = None
s_list = [1,3,4,6,9]
r_list = [8,6,5,4,3,2,1]
sort_list = []

def check_low(_s_list, _r_list, _i_s, _i_r, long_out) -> (int, int):
    # print(_i_s, _i_r)
    if long_out or _s_list[_i_s] < _r_list[_i_r]:
        return 1, 0
    else:
        return 0, 1

_i_r = -1
_i_s = 0
out_1 = False
out_2 = False
while 1:
    _s, _r = check_low(s_list, r_list, _i_s, _i_r, out_2)
    if _s:
        sort_list.append(s_list[_i_s])
        if _i_s == len(s_list) - 1:
            out_1 = True
        else:
            _i_s += 1
    elif _r:
        sort_list.append(r_list[_i_r])
        if 0 - _i_r == len(r_list):
            out_2 = True
        else:
            _i_r -= 1
    if out_2 and out_1:
        break
print(sort_list)
