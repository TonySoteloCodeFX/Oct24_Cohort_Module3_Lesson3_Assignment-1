our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def common_destinations():
    in_common = our_routes.intersection(competitor_routes)
    print("-" * 50)
    print("Common Destinations")
    for index, destination in enumerate(in_common):
            print(f"#{index + 1}: {destination}")
    return "-" * 50

def our_destination():
    only_ours = our_routes.difference(competitor_routes)
    print("-" * 50)
    print("Exclusive To Us")
    for index, destination in enumerate(only_ours):
            print(f"#{index + 1}: {destination}")
    return "-" * 50

def proprietary_destinations():
    ours = our_routes.difference(competitor_routes)
    thiers = competitor_routes.difference(our_routes)
    print("-" * 50)
    print("Exclusive To Us")
    for index, destination in enumerate(ours):
          print(f"#{index + 1}: {destination}")
    print("Exclusive To Competitor")
    for index, destination in enumerate(thiers):
          print(f"#{index + 1}: {destination}")
    return "-" * 50
          


print(common_destinations())
print(our_destination())
print(proprietary_destinations())