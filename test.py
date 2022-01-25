class comp:
    
    def __init__(self) -> None:
        self.element_composition = "hallo"

composition = comp()
print(*composition.element_composition)
# from matminer.featurizers import composition as cf

# elem = cf.ElementProperty.from_preset("magpie")

# feat = elem.featurize(composition)
# print(feat)