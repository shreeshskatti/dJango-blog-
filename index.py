class Human:
    def __init__(self, name, job, address):
        self.name = name
        self.job = job
        self.address = address

    def display_info(self):
        print(f"name:{self.name}")
        print(f"job:{self.job}")
        print(f"address:{self.address}")

sherlock = Human("sherlock", "detective","221B Baker Street")
shreesh = Human("shreesh","programmer","India")
sudeep = Human("sudeep","coder","India")
sultan = Human("sultan","tester","India")
sherlock.display_info()
shreesh.display_info()
sudeep.display_info()
sultan.display_info()