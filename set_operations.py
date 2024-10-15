customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def remove_duplicates():
    id_set = set(customer_ids)
    sorted_ids = sorted(id_set)
    return sorted_ids

print(remove_duplicates())