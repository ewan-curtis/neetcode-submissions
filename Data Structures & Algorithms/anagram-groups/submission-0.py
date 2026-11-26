class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in anagramMap:
                anagramMap[sorted_string].append(string)
            else:
                anagramMap[sorted_string] = [string]

        output = []
        for _, values in anagramMap.items():
            output.append(values)
        
        return output