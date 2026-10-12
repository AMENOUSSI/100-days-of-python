capitals ={
    "France" : "Paris",
    "Germany": "Berlin"
}

# Nested list in Dictionary

travel_log ={
    "France": ["Paris","Lille", "Dijon"],
    "Germany": ["Berlin","Stuttgart"]
}

# Print Lille

print(travel_log["France"][1])
nested_list = ["A","B",["C","D"]]

# print out the letter D
print(nested_list[2][1])

travel_log ={
    "France": {
        "cities_visited": ["Paris","Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin","Stuttgart"],
        "total_visits": 8
    }
}

print(travel_log["Germany"]["cities_visited"][1])