# Trait Types - - - - - - - - - - - - - - - - - - - - - - - - - #

INHERITED_TRAIT_TYPES = ["color"]

# number of possible values for trait
INHERITED_TRAIT_VALUE_RANGES = [1]

AQUIRED_TRAIT_TYPES = ["generation","children","parents"]

# Trait Containers - - - - - - - - - - - - - - - - - - - - - - - #

# contains a dictionary organized by: trait_type, [trait_values]
class InheritedTraitContainer:
    def __init__(self):
        self.traits = {}
        # setup an array for each trait that it will have
        for t in INHERITED_TRAIT_TYPES:
            self.traits[t] = None

    def set(self,trait_type,trait_value):
        self.traits[trait_type] = trait_value

    def get(self,trait_type):
        return self.traits[trait_type]

class AquiredTraitContainer:
    def __init__(self,gen_num):
        self.traits = {}
        # setup an array for each trait that it will have
        self.traits["generation"] = gen_num
        self.traits["children"] = []
        self.traits["parents"] = []

    def set(self,trait_type,trait_value):
        self.traits[trait_type] = trait_value

    def append(self,trait_type,trait_value):
        self.traits[trait_type].append(trait_value)

    def get(self,trait_type):
        return self.traits[trait_type]

# Traits - - - - - - - - - - - - - - - - - - - - - - - - - - #

# generic trait class
class Trait:
    def __init__(self,trait_type,trait_value):
        self.trait_type = trait_type
        self.trait_value = trait_value

# a traits inherited from parents
# these are set when the member is first born
class InheritedTrait(Trait):
    def __init__(self,trait_type,trait_value):
        super(trait_type,trait_value)

# a trait having to do with the memebers actual, individual life
# (aquired, so to speak)
# these are anytime after the member is born, and they can also change
class AquiredTrait(Trait):
    def __init__(self,trait_type,trait_value):
        super(trait_type,trait_value)