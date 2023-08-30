def create_nested_structure(site_id, path, categories, comment):
    nested_structure = {'siteId': site_id}
    
    if path:
        current_level = nested_structure
        for folder in path:
            current_level['site'] = {folder: {}}
            current_level = current_level['site'][folder]
    
    nested_structure['comment'] = comment
    nested_structure['categories'] = categories
    
    return nested_structure

# Example usage
# site_id = 'xn--golvlggare-u5a.net'
# path = ['Skane-lan', 'Malmo', 'Skanes-Parkettslip']
# categories = ['H6dsAI7l']
# comment = 'Imported 20210501 13:05 CET'

site_id = 'akua9394.com'
path = []  # Empty path
categories = ['Wu133hyG']
comment = 'imported 20230630 21:15 CET'

data = create_nested_structure(site_id, path, categories, comment)
print(data)