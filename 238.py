class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        front = [1]
        back = [1]
        for i in range(n):
            front.append(front[i]*nums[i])
        for i, j in zip(range(n), reversed(range(n))):
            back.append(back[i]*nums[j])
        back = back[1:][::-1] + [1]

        answer = []
        for i in range(n):
            answer.append(front[i] * back[i+1])
        return answer
