class Student:
    def __init__(self,name,house):
    # def __init__(self,name,house,patronus):
        
        self.name=name
        self.house=house
        # self.patronus=patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter    
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name=name

    @property   #for- Getter
    def house(self):
        return self._house     
    #We put "_" because we can't have both instatisation name and   function name same (it will confuse whihch one to invoke)
    
    @house.setter   #for- Setter
    def house(self,house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house


    ## making it a class function to solve problem (the chicken and egg problem)
    @classmethod
    def get(cls):
        name=input("Name: ")
        house=input("House: ")
        # patronus=input("Patronus: ")
        # student = Student(name,house,patronus)
        return cls(name,house)
         

        # name=input("Name: ")
        # house=input("House: ")
        # return {"name":name, "house":house}

    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🤔"
    #         case "Otter":
    #             return "🦦"
    #         case "Jack Russell Terrier":
    #             return "☠️"
    #         case _:
    #             return "🤣"
def main():
    student=Student.get()
    # if student["name"]=="Padma":
    #     student["house"]="RavenClaw"
    # print(f"{student.name} from {student.house}")
    # print("Expecto Patronum!")
    # print(student.charm())
    # student.house="Number Four, Privet Drive"      #For checking
    # student._house="Number Four, Privet Drive"      
        # #WTF! using _ was just a honor system(convention) we can still change the instance variable

    print(student)


if __name__ == "__main__":
    main()