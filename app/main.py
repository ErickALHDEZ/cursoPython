import utils

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

def run():

    keys, values = utils.get_population()
    print(keys, values)

    country = input("Type Country => ")

    result = utils.population_by_country(data, "Colombia")
    print(result)

if __name__ == "__main__":

    run()