import trait

class Parameters:
    """
    Parameters:
        - number of generations
        - children to create each generation
        - parents per procreation
        - way to calulate the advantage of a trait_value
        - number for important of a trait_type
    """
    def __init__(self,NAME,GENERATIONS,CHILDREN_PER_GENERATION,PARENTS_PER_PROCREATION,INHERITED_TRAIT_WEIGHTS,AQUIRED_TRAIT_WEIGHTS,INHERITED_TRAIT_ADVANTAGES):
        self.NAME = NAME
        self.GENERATIONS = GENERATIONS
        self.CHILDREN_PER_GENERATION = CHILDREN_PER_GENERATION
        self.PARENTS_PER_PROCREATION = PARENTS_PER_PROCREATION

        # dictionaries formatted: {"trait_type":wieght,...}
        # these are important for the user to enter
        self.AQUIRED_TRAIT_WEIGHTS = AQUIRED_TRAIT_WEIGHTS
        self.INHERITED_TRAIT_WEIGHTS = INHERITED_TRAIT_WEIGHTS

        # dictionaries formatted: {"trait_type:{"trait_value":advantage,...},..."}
        # these are the advantages of trait_values among the possisble trait_values of each trait_type respectively
        self.INHERITED_TRAIT_ADVANTAGES_BLUEPRINT = INHERITED_TRAIT_ADVANTAGES

        # functions defined below, because these won't be changing much
        self.INHERITED_TRAIT_ADVANTAGES = {}
        for tt in trait.INHERITED_TRAIT_TYPES:
            self.INHERITED_TRAIT_ADVANTAGES[tt] = create_inherited_trait_advantage(tt,self.INHERITED_TRAIT_ADVANTAGES_BLUEPRINT[tt])

        self.AQUIRED_TRAIT_ADVANTAGES = {
            "generation" : generation_advantage_function,
            "children" : children_advantage_function,
            "parents" : parents_advantage_function
        }

# Some functions to use - - - - - - - - - - - - - - - - - - #

# # Function factory for inherited trait advantages

def create_inherited_trait_advantage(t,ait):
    def f(trait_value):
        for tv in ait:
            if trait_value == tv:
                return ait[tv] # is a number
    return f

# # ADVANTAGE FUNCTIONS

def generation_advantage_function(trait_value):
    return float(1/float(trait_value))

def children_advantage_function(trait_value):
    # list of children, so return length
    return len(trait_value)

def parents_advantage_function(trait_value):
    # list of parents, so return length
    return len(trait_value)

# deprecated
def color_advantage_function(trait_value):
    if color == 1:
        return 3
    else:
        return 1