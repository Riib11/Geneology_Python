import geneology
import dot_creator

class GeneologyManager:
    def create(self,parameters):
        geneo = geneology.Geneology(parameters)

        # fill geneology with members
        geneo.create_geneology()

        dot_cre = dot_creator.DOTCreator(geneo)
        # display geneo info via dot graph
        dot_cre.create_dot()