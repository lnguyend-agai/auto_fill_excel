import re

def return_list_name(input_text):
    """
    Extracts names of people who liked a dish from a given menu.
    """
    lines = input_text.strip().split('\n')

    # Define a pattern to match various menu strings
    pattern = re.compile(r"menu\s*(thứ\s*\d+|t\d+)", re.IGNORECASE)

    # Find the index where the menu starts
    menu_start_idx = next((i for i, line in enumerate(lines) if pattern.search(line)), None)
    
    if menu_start_idx is None:
        raise ValueError("Menu not found in the input text")
    
    # Extract menu items
    menu_items = lines[menu_start_idx].replace("Menu thứ3; ", "").split(", ")
    menu_set = set(item.strip() for item in menu_items)  # Clean up any extra spaces
    
    # List to store the names of people who liked a dish from the menu
    liked_people = []
    
    # Process lines to find who liked which dish
    for i in range(menu_start_idx + 1, len(lines)):
        if 'like' in lines[i]:
            # Extract information
            name_line = lines[i - 2] if i - 2 >= 0 else ''
            dish_line = lines[i - 1] if i - 1 >= 0 else ''
            
            # Extract name
            name = name_line.split('] ')[1].strip() if ']' in name_line else ''
            # Extract dish
            dish = dish_line.strip()
            # Extract like value
            like = int(lines[i].split('like ')[1].strip())
            
            # Check if the dish is in the menu and if the like value is 1
            if like == 1 and dish in menu_set:
                first_name = name.split(' ')[-1]
                liked_people.append(first_name)
    
    # Remove duplicates (if any)
    return list(set(liked_people))