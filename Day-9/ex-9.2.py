"""Dictionary in Lists"""

travel_log = [
    {
        "Country":"Germany",
        "cities visited":["Berlin","Hamburg"],
        "total visits":1
    },
    {
        "Country":"France",
        "cities visited":["Paris","Dijon","Lille"],
        "total visits":1
    }
]

def add_new_country(country_visited,times_visited,cities_visited):
    new_country = {}
    new_country["Country"] = country_visited
    new_country["cities visited"] = cities_visited
    new_country["total visits"] = times_visited
    travel_log.append(new_country)

country = input("Enter the country : ")
visits= int(input("Enter the no. of times you have visited it : "))
cities = input("Enter the cities you have been to in the country : ")

add_new_country(country,visits,cities)

print(travel_log)
