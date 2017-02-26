import member
import trait
import random
random.seed()

# creates children based on parents
class ProcreationManager:
    def __init__(self,parameters):
        self.parameters = parameters

    # creates a new member, from the given parents
    # does not get any aquired traits yet
    def create_child(self,parents,gen):
        m = member.Member(gen)

        # chooses from parent's traits randomly
        for trait_type in trait.INHERITED_TRAIT_TYPES:
            possible_trait_values = []
            for p in parents:
                possible_trait_values.append(p.get_inherited_trait(trait_type))
            
            choice = random.choice(possible_trait_values)

            m.set_inherited_trait(trait_type,choice)

        # log relationship in parents and child
        for p in parents:
            p.append_aquired_trait("children",m)
            m.append_aquired_trait("parents",p)

        return m