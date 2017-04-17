import geneology_manager
import parameters
import time

NAME = "Test_Geneology"

GENERATIONS = 1500

CHILDREN_PER_GENERATION = 10

PARENTS_PER_PROCREATION = 2

# strength of trait over other traits
INHERITED_TRAIT_WEIGHTS = {
    "color": 1
}

AQUIRED_TRAIT_WEIGHTS = {
    "generation": 1,
    "children": 100
}

# strength of inherited trait values over other possible values
INHERITED_TRAIT_ADVANTAGES = {
    "color": {
        1: 1,
        2: 20
    }
}

def main():

    start_time = time.time()

    gen_man = geneology_manager.GeneologyManager()

    params = parameters.Parameters(NAME,GENERATIONS,CHILDREN_PER_GENERATION,PARENTS_PER_PROCREATION,INHERITED_TRAIT_WEIGHTS,AQUIRED_TRAIT_WEIGHTS,INHERITED_TRAIT_ADVANTAGES)
    gen_man.create(params)

    print("time: " + str(time.time()-start_time))
    print("gens: " + str(GENERATIONS))

main()