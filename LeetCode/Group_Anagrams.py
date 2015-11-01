class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs.sort()
        d = {}
        for str in strs:
            if "".join(sorted(str)) not in d:
                d["".join(sorted(str))] = [str]
            else:
                d["".join(sorted(str))].append(str)
                
        res = []
        for key, value in d.items():
            res.append(value)
        return res