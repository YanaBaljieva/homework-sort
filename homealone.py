import yaml
import json
class Students:
    def __init__(self, name, age, nomer):
        self.name = name
        self.age = age
        self.nomer = nomer
    def __repr__(self):
        return "(name=%r, age=%r, nomer=%r)" % (self.name, self.age, self.nomer)
p1 = Students("Ivan", 16, 12)

convert = yaml.dump(p1.__dict__)
print(convert)
convert2 = json.dumps(yaml.safe_load(convert))
print(convert2)



