def tupleDescription():
    print("1. 튜플은 순서가 있는 시퀀스형 자료입니다")
    print("2. 튜플이 직접 참조하는, 튜블이 가지고있는 객체는 변경이 불가능합니다.")
    print("3. 하지만, 튜플이 참조하는  객체가 변경될수는 있습니다. 다시말해서 튜플은 변하지 않지만, 그 내부 구성요소가 변할수는 있습니다")
    print("4. 튜플은 중복을 허락합니다")
    print("5. 튜플은 변경불가능한 자료형이며, 무결성을 보장한다, 하지만 불변의 튜플 내부에 변경가능한 리스트가 끼어있다면 무결성이 꺠진다-이러면 튜플쓰는 의미가 없으므로 비추")


def tupleSample():
    t = (1,2,3,4,5)
    print(t[0])
    print(t[:3])

    tt = ([1,2,3],77,[4,5,6])
    print(tt)

    print(type(tt))
    print(dir(tt))

    t = tuple("dongDongKing")
    print(t)


if __name__ == "__main__" :
    tupleDescription()
    tupleSample()