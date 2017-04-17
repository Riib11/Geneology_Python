import generation
import member
import selection_manager
import procreation_manager
from tqdm import tqdm

class Geneology:
    def __init__(self,parameters):
        self.parameters = parameters
        self.name = parameters.NAME
        self.selection_manager = selection_manager.SelectionManager(self.parameters)
        self.procreation_manager = procreation_manager.ProcreationManager(self.parameters)
        self.generations = []
        # filled after the generation is finished being created
        self.past_members = []

    def create_geneology(self):
        # create GENERATIONS generations
        for i in tqdm(range(self.parameters.GENERATIONS)):
            # create an empty generation
            gen = generation.Generation(i)
            if i == 0:
                self.populate_first_generation(gen)
            else:
                # fill the generation (create children from parents in previous generations)
                self.populate_generation(gen)

            self.add_generation(gen)

    def add_generation(self,gen):
        self.generations.append(gen)
        self.past_members += gen.members

    # create random first gen
    def populate_first_generation(self,gen):
        for i in range(self.parameters.CHILDREN_PER_GENERATION):
            gen.add_member(member.create_random_member(gen))

    # fill later generations, based on previous generations
    def populate_generation(self,gen):
        # create this many children in this generation
        for i in range(self.parameters.CHILDREN_PER_GENERATION):
            parents = self.selection_manager.choose_parents(self.past_members,gen)
            child = self.procreation_manager.create_child(parents,gen)
            gen.add_member(child)