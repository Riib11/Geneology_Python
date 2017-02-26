class Generation:
    def __init__(self,gen_num):
        self.gen_num = gen_num
        self.members = []
        self.member_count = 0

    def add_member(self,member):
        # this is where member name is set
        member.name = str(self.gen_num) + "." + str(self.member_count)
        self.member_count += 1
        self.members.append(member)