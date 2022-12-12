# Inheritance
from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

ChineseChef = ChineseChef()
ChineseChef.make_fried_rice()
ChineseChef.make_special_dish()