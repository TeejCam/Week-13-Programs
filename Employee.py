class Employee:
    def __init__(self, name="", id=0, department="", position=""):
        self.name = name
        self.id = id
        self.department = department
        self.position = position

    @classmethod
    def nameAndId(cls, name, id):
        return cls(name, id, "", "")

    @classmethod
    def default(cls):
        return cls("",0,"","")

    # Accessors
    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getDepartment(self):
        return self.department

    def getPosition(self):
        return self.position

    # Mutators
    def setName(self, name):
        self.name = name

    def setId(self, id):
        self.id = id

    def setDepartment(self, department):
        self.department = department

    def setPosition(self, position):
        self.position = position

    def fullname(self):
        return '{}'.format(self.name)
