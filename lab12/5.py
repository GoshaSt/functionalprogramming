
def read_infection_data_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        infection_data = [line.strip().split(', ') for line in file.readlines()]
    return infection_data

def find_regions_with_most_cases(infection_data):
    max_cases = max(int(data[1]) for data in infection_data)
    regions_with_most_cases = [data[0] for data in infection_data if int(data[1]) == max_cases]
    return regions_with_most_cases

filename = 'infection_file.txt'
infection_data = read_infection_data_from_file(filename)

regions_with_most_cases = find_regions_with_most_cases(infection_data)
print(f'Регионы с наибольшим количеством случаев заболеваний:')
for region in regions_with_most_cases:
    print(region)
