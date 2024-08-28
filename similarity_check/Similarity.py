class Similarity:
    def __init__(self):
        return
    def jaccard_coefficient(self, str1, str2):
        set1=set(str1)
        set2=set(str2)
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union if union != 0 else 0
    def overlap_coefficient(self, str1, str2):
        set1=set(str1)
        set2=set(str2)
        intersection = len(set1.intersection(set2))
        smaller_set_size = min(len(set1), len(set2))
        return intersection / smaller_set_size if smaller_set_size > 0 else 0
    def hamming_distance(self,str1, str2):
        if len(str1) != len(str2):
            return -1
        distance = sum(el1 != el2 for el1, el2 in zip(str1, str2))
        return distance
