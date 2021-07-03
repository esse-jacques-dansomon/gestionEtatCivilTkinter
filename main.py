# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from database import DataBase as db
from dao import userDao

userModel = userDao.UserDao()
print(userModel.loginAndPasswordExist('gator@junior.com', '1234'))


