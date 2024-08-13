import utils

keys, values = utils.get_population()
print(keys, values)

data = [
    {
        "Country" : "Colombia",
        "population" : 300
    },
    {
        "Country" : "Bolivia",
        "population" : 200
    }
]

country = input("Type Country => ")

result = utils.population_by_country(data, "Colombia")
print(result)
