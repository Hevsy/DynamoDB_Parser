def create_nested_structure(site_id, path, categories, comment):
    nested_structure = {'siteId': {'S': site_id}}
    
    current_level = nested_structure
    for folder in path:
        current_level['site'] = {'M': {folder: {'M': {}}}}
        current_level = current_level['site']['M'][folder]['M']
    
    current_level['comment'] = {'S': comment}
    current_level['categories'] = {'L': [{'S': cat} for cat in categories]}
    
    return nested_structure

# Example usage
site_id = 'xn--golvlggare-u5a.net'
path = ['Skane-lan', 'Malmo', 'Skanes-Parkettslip']
categories = ['H6dsAI7l']
comment = 'Imported 20210501 13:05 CET'

data = create_nested_structure(site_id, path, categories, comment)
print(data)