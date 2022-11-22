class School:
    def __init__(self,university, location):
        self.university = university 
        self.location = location
        self.num_students = 0
        self.num_teachers = 0
        self.project = ""
        self.category = ""
    
    def Details(self, num_students, num_teachers):
        self.num_students = num_students
        self.num_teachers = num_teachers
    
    def Projects(self, project_name, category):
        self.project = project_name
        self.category = category


XYZUniv = School("XYZ University", "Pune")
XYZUniv.Details(60,10)
XYZUniv.Projects("Solar Windmill", "Environmental Science")

print(f"Universiy Name: {XYZUniv.university}\nLocation : {XYZUniv.location}")
print(f"Number of Students: {XYZUniv.num_students}\nNumber of Teachers : {XYZUniv.num_teachers}")
print(f"Qualified Project Name: {XYZUniv.project}\nProject Category : {XYZUniv.category}")
