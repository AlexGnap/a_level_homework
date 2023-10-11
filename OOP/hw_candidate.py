class Candidate:
    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f"{self.first_name} + ‘ ‘ + {self.last_name}"

    @classmethod
    def generate_candidate(cls, file_path):
        candidates = []
        with open(file_path, 'r') as file:
            for line in file:
                next(file)
                line_part = line.strip().split(',')
                full_name = line_part[0].split()
                email = line_part[1]
                tech_stack = line_part[2].split('|')
                main_skill = line_part[3]
                main_skill_grade = line_part[4]
                candidates.append(cls(full_name[0], full_name[1], email, tech_stack, main_skill, main_skill_grade))
        return candidates


cand = Candidate('John', 'Malkovich', 'johnmalk@email.com', ['Python', 'Django'], 'Python', 'Mid')
print(cand.full_name)

cand_list = Candidate.generate_candidate('candidate_file.txt')
print(cand_list)
