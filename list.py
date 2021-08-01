def listBasic():
    a = [1, 2, 3, 4, 5]
    print(a)
    a[0] = 77
    print(a)
    # 바꿀수 있다


def stringBasic():
    str = "hello hellworld"
    print(str)
    print(str[0])
    # str[0] = 'f'
    # 할당은 되지 않는다


def listOperation():
    a = [1, 2, 4]
    print(a)

    a = [1, 2, 4]
    a = a + a
    print(a)

    # a + 3
    # 에러남

    # a = a - a
    # error

    a = [1, 2, 4]
    a = a * 4
    print(a)

    a = [1, 2, 4]
    a.append(10)
    print(a)

    a.clear()
    print(a)


def typeStudy():
    a = [1, 2, 3]
    print(a)
    print("type : ")
    print(type(a))
    print("dir : " + dir(a).__str__())


def shallowCopyProblem():
    a = [1, 2, 4]
    b = a
    c = a
    print("a : " + a.__str__())
    print("b : " + b.__str__())
    print("c : " + c.__str__())
    a.append(100)
    print("a : " + a.__str__())
    print("b : " + b.__str__())
    print("c : " + c.__str__())
    c[0] = 999
    print("a : " + a.__str__())
    print("b : " + b.__str__())
    print("c : " + c.__str__())


def listAppendExtend():
    a = [1, 2, 3, 4, 5]
    print(a)
    print(a.count(3))
    print(a.count('3'))
    a.extend([9, 8, 7, 6])
    print(a)
    a.append([10, 11, 12])
    print(a)
    # what the... f..? 2D array


def sort():
    a = [11, 12, 5, 8, 9, 1,3]
    print(a)
    a.sort()
    print(a)


if __name__ == "__main__":
    # listBasic()
    # stringBasic()
    # listOperation()
    # typeStudy()
    # shallowCopyProblem()
    #listAppendExtend()
    sort()