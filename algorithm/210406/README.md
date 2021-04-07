### 1. 직사각형 퍼즐 문제

적절한 풀이보다는, 모든 케이스를 직접 그려서 카운팅 하다가 피보니치 수열과 유사하다는 걸 깨닫고 DP를 사용해서 구현해보니 통과가 되었습니다.

```python
def solution(n):
    if n < 3:
        return n
    i, j = 1, 2
    for _ in range(n-2):
        i, j = j, i+j
    return j%1000000007
```

### 2. 도둑질 문제

다양한 방법으로 시도해 봤지만 접근이 어려워 인터넷을 참고하여 풀었습니다. 로직의 큰 원리는 파악했지만 묘사적인 부분에 있어 더 깊은 이해가 필요할 것 같아 꾸준히 복습해야 할 것 같습니다.

```python
def solution(money):
    # 첫번째 집을 터는 경우
    dp1 = [0]*len(money)
    dp1[1] = dp1[0] = money[0]  # 첫번째 집을 털면 두번째 집은 고려하지 않아도 된다
    for i in range(2, len(money)-1):  # 첫번재 집을 털면 마지막 집을 못털기 때문에 -1
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])

    # 첫번째 집을 안터는 경우
    dp2 = [0]*len(money)
    dp2[1] = money[1]  # 첫번째 집을 안털면, 두번째 집을 털거나 털지 않는다
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])

    return max(dp1+dp2)
```
