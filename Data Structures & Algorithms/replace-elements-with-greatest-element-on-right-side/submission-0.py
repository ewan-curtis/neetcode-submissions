class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arrLen = len(arr)
        maxRightElement = arr[arrLen - 1]
        arr[arrLen - 1] = -1
        for i in range(arrLen - 2, -1, -1):
            currentVal = arr[i]
            arr[i] = maxRightElement
            if currentVal > maxRightElement:
                maxRightElement = currentVal
        return arr