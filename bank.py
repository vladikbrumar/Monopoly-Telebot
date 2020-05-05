import properties
import player


class Bank(player.Player):
    propers = properties.properties.copy()

    def __init__(self):
        super().__init__('Bank', 1000000, self.propers)

    # def remove_property(self, property_name):
    #     del self.properties[property_name]
    #
    # def return_property(self, property_name, property_obj):
    #     self.properties[property_name] = property_obj

