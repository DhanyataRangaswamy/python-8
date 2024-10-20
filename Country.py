class India():
    def capital(self):
        print("Capital of India is New Delhi")

    def language(self):
        print("Hindi is a widely spoken language in India")

    def development(self):
        print("India is a developing country")

class USA():
    def capital(self):
        print("Capital of USA is Washington DC")

    def language(self):
        print("English is the primary language in USA")

    def development(self):
        print("USA is a developed country")

obj_ind=India()
obj_usa=USA()

for county in (obj_ind , obj_usa):
    county.capital()
    county.language()
    county.development()
