import yaml
import json
class Students:
    def __init__(self, name, age, nomer):
        self.name = name
        self.age = age
        self.nomer = nomer
    def __repr__(self):
        return "(name=%r, age=%r, nomer=%r)" %  (self.__class__.__name__, self.name, self.hp, self.sp)

s1 = Students("Goshko", 15, 8)
convert = json.dumps(s1.__dict__)
print(convert)
convert2 = yaml.dump(yaml.safe_load(convert))
print(convert2)
