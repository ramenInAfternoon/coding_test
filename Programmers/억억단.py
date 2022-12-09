"""
s~e까지 수 중 가장 많이 등장한 수를 답해야한다.
입출력 예 설명을 통해, s~e까지 등장횟수를 나타내는건, 해당 수의 약수의 갯수라는걸 추론해내야함.
약수의 갯수인걸 알았다면, 약수를 구하는 최소의 시간복잡도를 구해야하는데,
여기선 int(num**0.5)+1 대신에 i씩 커지는 for loop을 돌린다. 이게 훨씬 시간복잡도가 낮던데
왜그런진 잘 모르겠음.

이렇게 각 숫자의 약수의 갯수를 구했다면,
어차피 끝은 e이기때문에, starts[i]에 대한 i~e까지 수 중 가장 많이 등장한 수를
찾으면 된다.
이것 또한, 그냥 통으로 다 구함.

여기서 정리할게,
arr[i] = i의 약수의 갯수
ans[i] = i~e까지 수 중 "약수의 갯수가 가장 많은 수"
고로, 비교해야하는게 arr[i]와 arr[ans[i]]와 비교해야하고
이걸 역으로 순회한다면, i+1~e까지 수에 대해선 가장 많은 약수의 갯수를 가진 수를 저장하며 오기때문에
arr[i]>=arr[ans[i+1]]만 비교하면, O(N)으로 비교가 가능.
=도 포함된건, 같은 약수의 갯수라면 작은수면 업데이트 해야하기때문

그래서 "i의 약수의 갯수"와 "i+1까지 최대 약수의 갯수를 가진 수"를 비교.

"""
def solution(e, starts):
    arr = [1]*(e+1)
    ans = [0]*(e+1)
    for i in range(2,e+1):
        for k in range(i*2,e+1,i):
            arr[k] += 1
    ans[e] = e
    for i in reversed(range(0,e)):
        if arr[i] >= arr[ans[i+1]]:
            ans[i] = i
        else:
            ans[i] = ans[i+1]
    
    return [ans[i] for i in starts]
