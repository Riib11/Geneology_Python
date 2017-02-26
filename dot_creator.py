import file_manager
import dot_parameters

class DOTCreator:
    def __init__(self,geneology):
        self.name = geneology.parameters.NAME
        self.geneology = geneology

    def create_dot(self):
        # first couple of lines
        self.dot_file = file_manager.FileManager("outputs",self.name+".dot")
        self.dot_file.write("graph " + self.name + "{")

        self.generations_labels = []

        # setup the dot parameters (to do lots of things)
        self.dot_params = dot_parameters.DOTParameters(self,self.geneology)

        # create the dot stuff
        self.dot_params.config_graph()
        self.create_generations_labels()
        self.create_generations()
        self.create_member_attributes()
        self.create_relations()

        self.finish()

    def set_graph_label(self,s):
        self.dot_file.write("   label=<<FONT POINT-SIZE='50'>" + s + "</FONT>>;")
        self.dot_file.write("   labelloc=tp;")

    def set_graph_attribute(self,attr,val):
        self.dot_file.write("   graph [" + str(attr) + "=" +  str(val) + "];")

    def set_node_attribute(self,attr,val):
        self.dot_file.write("   node [" + str(attr) + "=" +  str(val) + "];")

    def set_edge_attribute(self,attr,val):
        self.dot_file.write("   edge [" + str(attr) + "=" + str(val) + "];")

    def create_generations_labels(self):
        self.dot_file.write("   subgraph generations_labels {")
        self.dot_file.write("       node[color=grey style=filled fontsize=12 shape=cds fontcolor=black fixedsize=false];edge[style=invis]")
        s = ""
        # for each generation
        for i in range(len(self.geneology.generations)):
            lab = "Gen" + str(i)
            self.generations_labels.append(lab)
            s += lab + " -- "
        s = s[:-4]
        self.dot_file.write("      " + s + ";")
        self.dot_file.write("   }")

    def create_generations(self):
        j = 0
        for g in self.geneology.generations:
            s = "   {rank=same;" + self.generations_labels[j] + ";"
            j+=1
            for i in range(len(g.members)):
                s += g.members[i].name + ";"
            s += "}"
            self.dot_file.write(s)

    def create_relations(self):
        # for all the members
        for m in self.geneology.past_members:
            # list of children
            for child in m.get_aquired_trait("children"):
                s = "   " + m.name + " -- " + child.name
                
                edge_color = self.dot_params.calculate_edge_color(m,child)
                pen_width = self.dot_params.calculate_edge_width(m,child)
                s += " ["
                s += "color=" + str(edge_color)
                s += " penwidth=" + str(pen_width)
                s += "];"

                self.dot_file.write(s)

    def create_member_attributes(self):
        for m in self.geneology.past_members:
            color = self.dot_params.calculate_member_color(m)
            shape = self.dot_params.calculate_member_shape(m)
            width = self.dot_params.calculate_member_width(m)
            fontsize = self.dot_params.calculate_member_fontsize(m)
            s = "    " + m.name + " ["
            s += "color=" + str(color)
            s += " shape=" + str(shape)
            s += " width=" + str(width)
            s += " fontsize=" + str(fontsize)
            s += "];"
            self.dot_file.write(s)

    def finish(self):
        self.dot_file.write("}")
        self.dot_file.close()