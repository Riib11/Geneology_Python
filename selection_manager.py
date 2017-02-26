import trait
import random
random.seed()

# chooses parents based on traits
class SelectionManager:

    """
    Trait weight: how important a trait_type is compared to other trait_type (number)
    Trait advantage: how important a certain trait_value is compared to other trait_values of the same trait_type (function(trait_value))
    """

    def __init__(self,parameters):
        self.parameters = parameters

        self.inherited_traits_wieghts = self.parameters.INHERITED_TRAIT_WEIGHTS
        self.aquired_traits_wieghts = self.parameters.AQUIRED_TRAIT_WEIGHTS

        self.inherited_traits_advantages = self.parameters.INHERITED_TRAIT_ADVANTAGES
        self.aquired_traits_advantages = self.parameters.AQUIRED_TRAIT_ADVANTAGES

    # return an array of members
    def choose_parents(self,past_members,gen):
        # if there arent enought possible parents to account for probabilities
        if len(past_members) <= self.parameters.PARENTS_PER_PROCREATION:
            return past_members

        # otherwise:

        probabilities = []
        for m in past_members:
            probabilities.append(self.calculate_fitness(m,gen))

        # might be a more efficient way to do this...
        raw_total = 0
        for p in probabilities:
            raw_total += p

        parents = []
        parents_indexes = []
        for i in range(self.parameters.PARENTS_PER_PROCREATION):
            pi = self.get_random_index(raw_total,probabilities)
            while pi in parents_indexes:
                # chooes a pi
                pi = self.get_random_index(raw_total,probabilities)
            parents_indexes.append(pi)
            parents.append(past_members[pi])

        # array of members
        return parents

    # utility for above function
    def get_random_index(self,raw_total,probabilities):
        choice = float(random.random() * raw_total)

        running_total = 0
        for i in range(len(probabilities)):
            if probabilities[i] + running_total >= choice:
                return i
            else:
                running_total += probabilities[i]

    # member in question, and concerned generation (for purpose of determining age)
    # the fitness of this member is how likely it will be chosen for procreation
    def calculate_fitness(self,member,gen):
        # age is relative to current generation
        age = gen.gen_num - member.get_aquired_trait("generation")
        age_advantage = self.aquired_traits_advantages["generation"](age)
        age_weight = age_advantage * self.aquired_traits_wieghts["generation"]

        # number of children
        children = member.get_aquired_trait("children")
        children_advantage = self.aquired_traits_advantages["children"](children)
        children_weight = children_advantage * self.aquired_traits_wieghts["children"]

        # cycle through all inherited traits
        t_weights = []
        for t in trait.INHERITED_TRAIT_TYPES:
            t_advantage = self.inherited_traits_advantages[t](member.get_inherited_trait(t))
            t_weight = t_advantage * self.inherited_traits_wieghts[t]
            t_weights.append(t_weight)

        # total of all scores
        total = age_weight + children_weight
        for w in t_weights:
            total += w

        return total