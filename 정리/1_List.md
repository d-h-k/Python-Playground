# 파이썬 정리 - List 컬렉션


## 리스트 기초 연산
```python
def listBasic():
    a = [1, 2, 3, 4, 5]
    print(a)
    a[0] = 77
    print(a)
    # 바꿀수 있다
```
- 리스트는 이렇게 [] 꺽쇠괄호(대괄호)로 다루고 사용할 수 있습니다
- 원소 변경도 가능합니다



## 문자열을 리스트로 다루기
```python
def stringBasic():
    str = "hello hellworld"
    print(str)
    print(str[0])
    print( list(str))
    # str[0] = 'f'
    # 할당은 되지 않는다
```
- 당연히 문자열을 리스로도 변환할 수 있습니다


## 리스트의 연산
```python
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
```
- 리스트는 연산이 가능합니다. 덧셈 곱셈
- 뿐만 아니라 파이썬이 기본 지원하는 메서드들로 리스트를 조작할 수 있습니다

## 파이썬 리스트의 타입과 사용가능한 내장함수를 알아보기
```python
def typeStudy():
    a = [1, 2, 3]
    print(a)
    print("type : ")
    print(type(a))
    print("dir : " + dir(a).__str__())
```
- 위 함수들을 사용하면 내장함수들을 사용할 수 있습니다


## 파이썬의 깊은복사 얕은복사
```python
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
```
- 뒤에서도 계속 나오게 될 내용이지만, 파이썬은 기본적으로 모든것들을 객체로 처리합니다.
- 따라서 메모리 공간 낭비를 막기위해 단순대입연산시, 참조값만 복사되며 새로운 리스트가 생성되지는 않습니다.


## 리스트의 조작
```python
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
```
- 검색과 덧붙이기(append)가 가능합니다
```python
def mySort():
    a = [11, 12, 5, 8, 9, 1,3]
    print(a)
    a.sort()
    print(a)
```
- 정렬도 가능합니다

## 파이썬의 다차원  List구조
```python
def dimension():
    a = 0   # 상수 : 스칼라
    print(type(a))
    b = [1] # 2차원 : 벡터 Vector
    print(type(b))
    c = [[2]]  # 2차원 : 매트릭스 Matrix
    print(type(c))
    d = [[[3]]]  # 3차원 : 텐서 Tensor
    print(type(d))
    myMat = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    print(myMat)
    print(type(myMat))
```
- 다차원 자료구조를 사용해야하는 경우가 많은데요, 이때는 위 코드처럼 사용합니다.
- 또 단순값, 1차원, 2차원, 3차원마다 각각 벡터, 메트릭스, 텐서라는 닉네임이 붙어있습니다


## 런쳐
```python
if __name__ == "__main__":
    listBasic()
    stringBasic()
    listOperation()
    typeStudy()
    shallowCopyProblem()
    listAppendExtend()
    mySort()
    dimension()
```
- 위 모든 함수들을 기능적/단위적으로 테스트하기 위한 메인함수의 런쳐입니다.
- 각자 필요하신 부분만 스니핏으로 사용하시면 됩니다
- 원본 링크는 여기입니다 : 