import property as prop

properties = {
    'Home': prop.Property('Home', 200, 10, 100),
    'Store': prop.Property('Store', 400, 20, 200),
    'Shop': prop.Property('Shop', 150, 8, 75),
    'School': prop.Property('School', 300, 15, 150),
    'Park': prop.Property('Park', 100, 5, 50)
}


def get_by_name(property_name):
    for prop_item in properties.values():
        if prop_item.name == property_name:
            return prop_item
