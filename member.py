import trait
import random
random.seed()

# a member of the geneology
class Member:
    def __init__(self,gen):
        self.inherited_traits = trait.InheritedTraitContainer()
        self.aquired_traits = trait.AquiredTraitContainer(gen.gen_num)
        self.name = ""

    # INHERITED TRAITS - - - - - - - - - - - - - - - - - - - - #

    def set_inherited_trait(self,trait_type,trait_value):
        self.inherited_traits.set(trait_type,trait_value)

    # returns a dictionary
    def get_inherited_trait(self,trait_type):
        return self.inherited_traits.get(trait_type)

    # AQUIRED TRAITS - - - - - - - - - - - - - - - - - - - - - #

    def set_aquired_trait(self,trait_type,trait_value):
        self.aquired_traits.set(trait_type,trait_value)

    def append_aquired_trait(self,trait_type,trait_value):
        self.aquired_traits.append(trait_type,trait_value)

    # returns a dictionary
    def get_aquired_trait(self,trait_type):
        return self.aquired_traits.get(trait_type)

# for use of creating the first generation
def create_random_member(gen):
    member = Member(gen)

    # gives random values for each trait
    for i in range(len(trait.INHERITED_TRAIT_TYPES)):
        tt = trait.INHERITED_TRAIT_TYPES[i]
        vr = trait.INHERITED_TRAIT_VALUE_RANGES[i]
        # gives random value in range: 1 <= v <= vr
        tv = random.randint(1,vr)
        member.set_inherited_trait(tt,tv)

    return member