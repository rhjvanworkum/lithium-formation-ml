class comp:
    
    def __init__(self, comp) -> None:
        self.element_composition = comp

composition = comp({"Li": 1, "O": 4})

from matminer.featurizers import composition as cf

elem = cf.ElementProperty.from_preset("magpie")

feat = elem.featurize(composition)
print(feat)