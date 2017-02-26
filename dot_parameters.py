import dot_colors

class DOTParameters:
    def __init__(self,dotcreator,geneology):
        self.dotcreator = dotcreator
        self.geneology = geneology

    # setup all basic attributes
    def config_graph(self):
        self.dotcreator.set_graph_label(self.dotcreator.name)
        
        self.dotcreator.set_graph_attribute("splines","splines")
        self.dotcreator.set_graph_attribute("nodesep","0.1")
        self.dotcreator.set_graph_attribute("ranksep",1)

        self.dotcreator.set_node_attribute("style","filled")
        self.dotcreator.set_node_attribute("fontcolor","white")
        self.dotcreator.set_node_attribute("fixedsize","true")

    def calculate_edge_color(self,parent,child):
        return dot_colors.num_to_color(parent.get_inherited_trait("color"))

    def calculate_edge_width(self,parent,child):
        total = float(len(self.geneology.past_members))
        percent_children = float(len(parent.get_aquired_trait("children"))) / total
        w = float(30) * percent_children
        if w < 0.5:
            w = 0.5 

        w = 8
        return w

    def calculate_member_color(self,m):
        return dot_colors.num_to_color(m.get_inherited_trait("color"))

    # all circles for now
    def calculate_member_shape(self,m):
        return "circle"

    # percent children * 100
    def calculate_member_width(self,m):
        total = float(len(self.geneology.past_members))
        percent_children = float(len(m.get_aquired_trait("children"))) / total
        w = float(10) * percent_children
        if w < 0.2:
            w = 0.2

        w = 1
        return w
    
    # width * 20
    def calculate_member_fontsize(self,m):
        return self.calculate_member_width(m) * float(20)