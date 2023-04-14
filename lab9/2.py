def get_info(dict_test):
    # List of team names
    global result_tuple
    info_list = ['Python', 'Java', 'SQL', 'JS']

    # Tuple of team countries
    info_tuple = {('DB', 'SQL'),
                  ('ML', 'Python'),
                  ('Java', 'Backend'),
                  ('JS', 'Frontend')}

    # Dictionary of team managers
    info_dict = {
        'DB': 'SQL',
        'ML': 'Python',
        'Java': 'Backend',
        'JS': 'Frontend'
    }

    list_len = len(info_list)

    tuple_len = len(info_tuple)

    del info_dict[dict_test]

    return list_len, tuple_len, info_dict


info_list, info_tuple, info_dict = get_info('JS')
print(info_list)
print(info_tuple)
print(info_dict)
