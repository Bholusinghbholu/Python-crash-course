def describe_city(city,country="India"):
        """accept city and its country and describe it"""
        print(f"{city.title()} is in {country.title()}")

describe_city("delhi")        
describe_city("mumbai","india")        
describe_city("new york","USA")        
