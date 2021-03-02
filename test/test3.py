# xyz
import sys
n = 0
content = ''
if len(sys.argv) > 1:
    n = int(sys.argv[1])
if len(sys.argv) > 2:
    content = sys.argv[2]

def append(l: list, s: str, n: int):
    _d = 1
    for i, v in enumerate(l):
        if v:
            if len(l[i]) < n:
                l[i] += s
        elif _d:
            l[i] += s
            _d = 0
        else:
            break
    print(l)


def print_xyz(n: int):
    list_all = ['']*len(content)
    for i in content:
        if i in "xyz":
            append(list_all, i, n)
    print(content)
    print([i for i in list_all if len(i) == n])


if __name__ == "__main__":
    print_xyz(n)
