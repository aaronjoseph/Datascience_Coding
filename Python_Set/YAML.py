import yaml

def sort_yaml(data):
    """
    Recursively sort dictionaries by keys and sort lists if possible.
    """
    if isinstance(data, dict):
        # Create a new dict with keys sorted alphabetically.
        sorted_dict = {}
        for key in sorted(data):
            sorted_dict[key] = sort_yaml(data[key])
        return sorted_dict
    elif isinstance(data, list):
        # Recursively sort each element in the list.
        sorted_list = [sort_yaml(item) for item in data]
        # Attempt to sort the list itself if its elements are directly comparable.
        try:
            return sorted(sorted_list)
        except TypeError:
            # If elements cannot be compared (e.g., dicts), return as-is.
            return sorted_list
    else:
        # For scalars, just return the data.
        return data

# Example YAML content with nested dictionaries and a list.
example_yaml = '''
z: 3
a: 1
m:
  y: 2
  x: 1
list:
  - banana
  - apple
  - orange
nested:
  sub:
    b: 2
    a: 1
'''

# Load the YAML content.
data = yaml.safe_load(example_yaml)

# Recursively sort the data.
sorted_data = sort_yaml(data)

# Dump the sorted data back to YAML.
# Note: We set sort_keys=False because our function already sorts the keys.
sorted_yaml = yaml.dump(sorted_data, sort_keys=False)
print(sorted_yaml)
