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
