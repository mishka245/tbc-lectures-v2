
def create_profile(**kwargs):
    name = kwargs.get("name")
    age = kwargs.get("age")
    city = kwargs.get("city")
    print(f"Create account for {name}. City: {city}, Age: {age}")


# create_profile()
# create_profile(name="Tite")
# create_profile(name="Nugzar", age="19")
# create_profile(name="Ketevan", age="24", city="Tbilisi")
create_profile(city="Tbilisi", name="Ketevan", age="24")
create_profile("test", city="Tbilisi", name="Ketevan", age="24")

