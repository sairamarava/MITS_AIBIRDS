class jacord:
    def __init__(self):
        return
    def jaccard_coefficient(self, set1, set2):
        set1=set(set1)
        set2=set(set2)
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union if union != 0 else 0
jac=jacord()
print(jac.jaccard_coefficient('sairem','sairam'))