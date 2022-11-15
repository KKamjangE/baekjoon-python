# 자료형을 정하지 않은 리스트 원소 확인하기

import copy # deepcopy를 사용하기 위한 copy 모듈 임포트

x = [15, 64, 7, 3.14, [32, 55], 'ABC']
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
    
a = [[1,2,3], [4,5,6]]
b = a.copy() # x를 y로 얕은 복사
a[0][1] = 9
print(a)
print(b)
# 리스트의 얕은 복사를 수행하기 때문에 y도 동일하게 업데이트

c = [[1,2,3],[4,5,6]]
d = copy.deepcopy(c)
c[0][1] = 9
print(c)
print(d)
# 리스트의 원소뿐만 아니라 구성원소(원소의 원소)도 복사
# 따라서 c[0][1]이 참조하는곳을 업데이트해도 d[0][1]이 참조하는곳은 업데이트X