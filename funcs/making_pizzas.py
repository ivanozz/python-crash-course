# импортирование всего модуля
import pizza

# импортирование функции модуля
from pizza import make_pizza as mp

pizza.make_pizza('sous', 'mushrooms')

make_pizza('sous', 'mushrooms')

mp('sous', 'mushrooms')

# импортирование всех функций модуля
from pizza import *
