import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
# #from django.contrib.auth.models import User

from faker import Faker
from django.contrib.auth.models import User
from shop.models import Item, List, Store, UserModel

fake = Faker()


userList = List(listname="userList")
store = Store(storename="defaultStore")
userList.save()
store.save()
# Create stores
for i in range(0, 20):
    storename = fake.text(20)
    storeStore = Store(
        storename=storename
    )
    storeStore.save()


# Create items and add to lists
items = []
for i in range(0, 100):
    i_name = fake.text(10)
    i_quantity = fake.random_int(100)
    i_aisle = fake.random_int(10)
    i_price = fake.random_int(50)
    item = Item(
        name=i_name, quantity=i_quantity, aisle=i_aisle, price=i_price
    )
    item.save()
    store.items.add(item)
    if i < 50:
        userList.item.add(item)
    items.append(item)


# Take the first 50 items and put it into a list of
user = UserModel(username="defaultUser", favoriteCart=userList)
user.save()
# Make 10 favorite items
for i in range(0, 10):
    i_name = fake.text(10)
    i_quantity = fake.random_int(100)
    i_aisle = fake.random_int(10)
    i_price = fake.random_int(50)
    item = Item(
        name=i_name, quantity=i_quantity, aisle=i_aisle, price=i_price
    )
    item.save()
    user.favoriteItems.add(item)
    user.save()

for g in user.favoriteItems.all():
    print(g)


username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:

  username: {username}
  password: {password}
  email: {email}

You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

  $ python3 manage.py runserver 0.0.0.0:8080"
====================================================================
"""
print(message)