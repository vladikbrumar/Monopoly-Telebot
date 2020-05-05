import property as prop
import properties as props


class Player:

    def __init__(self, name, money, properties):
        self.name = name
        self.money = money
        self.properties = properties

    # current player buy Property with property_name from player
    def buy(self, player, property_name):
        # get current property
        curr_property = props.get_by_name(property_name)

        # little money transaction
        if self.money <= curr_property.price:
            return 'у тебя нима деняк'
        else:
            self.money -= curr_property.price
            player.money += curr_property.price
            # change owner of property
            self.properties[property_name] = curr_property
            del player.properties[property_name]

    # self pay rent to player for prop_name
    def pay_rent(self, player, property_name):
        rent_amount = props.get_by_name(property_name).mortage
        if self.money <= rent_amount:
            return 'у тебя нема деняк'
        self.money -= rent_amount
        player.money += rent_amount

    # if you have no money, you should go to bank and sell some property to bank
    # with mortage price
    def sell_to_bank(self, player_bank, property_name):
        curr_property = props.get_by_name(property_name)
        player_bank.money -= curr_property.mortage
        self.money += curr_property.mortage
        del self.properties[property_name]
        player_bank.properties[property_name] = curr_property

    def get_properties_stat(self):
        list_of_properties = ''
        if self.properties:
            for prop_obj in self.properties.values():
                list_of_properties += prop_obj.name + '\n'
        else:
            list_of_properties = 'No properties yet'

        return list_of_properties;
