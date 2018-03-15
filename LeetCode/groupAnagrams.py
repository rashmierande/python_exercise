# Time:  O(n * glogg), g is the max size of groups.
# Space: O(n)
#
# Given an array of strings, return all groups of strings that are anagrams.
#
# Note: All inputs will be in lower-case.
#
import collections

def groupAnagrams(strs):
    """
        :type strs: List[str]
        :rtype: List[List[str]]
    """
    anagrams_map = collections.defaultdict(list)
    result= []

    for s in strs:
        sorted_str = ("").join(sorted(s))
        # print(sorted_str, s)
        anagrams_map[sorted_str].append(s)
        # print(anagrams_map)
    for anagram in anagrams_map.values():
        anagram.sort()
        result.append(anagram)
    return result


result = groupAnagrams(["cat", "dog", "act", "mac"])
print (result)
