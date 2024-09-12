# variables naming
from traceback import print_tb

# 1, 2, 5 can not be triangle

from datetime import *  # okay
from datetime import timedelta  # better idea

a,b,c = 1,2,5
s = (a + b + c) / 2
p = s * (s - a) * (s - b) * (s - c)

side_a, side_b, side_c = 3, 4, 5
area = (side_a + side_b + side_c) / 2
perimeter = area * (area - side_a) * (area - side_b) * (area - side_c)









user = "user"
password = "password"

user_name = "user_name_123"  # snake_case - variable names
userName = "user_name_123"   # camelCase  - we do not use that in python
UserName = "user_name_123"   # CamelCase  - We use them for Class names
RETENTION_DAYS = 90   # We use such style for constants

class UserName:
    pass


