def quick_sort(x, left=0, right=None):  # 최초 생성시에는 배열의 시작부터 끝을 지정
    if right == None:
        right = len(x)  # 최초 실행시에는 배열의 끝을 최우단으로 지정
    if right-left < 1:  # 배열의 길이가 1이하가 되면 분할 종료
        return
    i = left+1  # 탐색 시작점 지정
    pivot_idx = left  # 피봇 지정
    while i < right:  # 탐색이 최우단 지점까지 가면 탐색종료
        if x[pivot_idx] <= x[i]:  # 기준값보다 비교값이 크거나 같으면
            i += 1  # 이미 기준값보다 오른쪽에 있는것이므로 다음 값을 비교하러 이동
        else:  # 기준값보다 비교값이 작으면
            x[left:i+1] = [x[i]] + x[left:i]  # 최좌단 지점에 삽입 후 밀어내기
            pivot_idx += 1  # 밀렸기 때문에 피봇도 +1
            i += 1  # 다음 값 탐색
    # 피봇점을 기준으로 작은값은 좌측, 큰 값은 우측으로 나뉨
    # 최좌단과 최우단(피봇이 밀려난 곳 까지)을 지정해준다 -> 분할한 부분에서 작은 부분을 재귀함수로 정렬
    quick_sort(x, left, pivot_idx)
    quick_sort(x, pivot_idx+1, right)  # 최좌단(피봇의 다음부터)과 최우단을 지정해준다
    # 모든 정렬이 끝나면 정렬된 배열을 반환
    return x


print(quick_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(quick_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(quick_sort([5, 5, 4, 4, 7, 7, 2, 2, 8, 8, 1, 1]))
print(quick_sort([1, 5, 3, 7, 1, 5, 3, 8]))
