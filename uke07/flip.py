
def flip1(v):
    temp = v[0]
    v[0] = v[1]
    v[1] = temp

def flip2(v):
    v = [v[1], v[0]]


if __name__ == "__main__":
    v1 = [0, 1]

    flip2(v1)

    print(v1)
