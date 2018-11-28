import textwrap
from datetime import timedelta

#from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from faker import Faker
from django.contrib.auth.models import User
from shop.models import Item, List, Store, UserModel

fake = Faker()

consumer, created = Group.objects.get_or_create(name='consumer')
ct = ContentType.objects.get_for_model(UserModel)
can_add_items = Permission.objects.create(codename='can_add_items', name='Can Add Items', content_type=ct)
consumer.permissions.add(can_add_items)

userList = List(listname="userList")
userList.save()

#Create stores
stores = []
for i in range(1, 10):
    s_name = fake.text(50)
    s_location = fake.text(10)
    store = Store(name=s_name,
                  location=s_location
                  )
    store.save()
    stores.append(store);

#Create items
items = []
for i in range(1, 10):
    i_name = fake.text(50)
    i_store = stores[fake.random_int(0, len(stores))-1]
    i_price = fake.random_int(1,100)
    i_aisle = fake.random_int(1,26)
    i_short_description = fake.text(150)
    i_item_number = fake.random_int(1,126)
    item = Item(name = i_name,
                store = i_store,
                price = i_price,
                aisle = i_aisle,
                short_description = i_short_description,
                item_number = i_item_number,
                )
    item.save()
    userList.item.add(item)
    items.append(store);

print("\nStore:")
for i in Store.objects.all():
    print(i)

print("\nItem:")
for i in Item.objects.all():
    print(i)


username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuserM = UserModel(user=adminuser, favoriteCart=userList)
adminuserM.save()
consumer.user_set.add(adminuser)
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

users = []
userOuter = []
for i in range(0, 10):
    firstname = fake.first_name()
    lastname = fake.last_name()
    username = firstname.lower()[0] + lastname.lower()
    email = f"{username}@326.edu"
    password = lastname
    user = User.objects.create_user(username, email, password)
    user.first_name = firstname
    user.last_name = lastname
    #user.user_permissions.add(can_add_items)
    if(i == 9):
        consumer.user_set.add(user)
    user.save()
    users.append(user)
    userOuter = UserModel(user=user, favoriteCart=userList)
    userOuter.save()
    print(f"  username: {username}, password: {password}")

# Take the first 50 items and put it into a list of
print('^ This user can modify his/her own favorite items list')
# Make 10 favorite items

for i in range(0, 10):
    i_name = fake.text(50)
    i_store = stores[fake.random_int(0, len(stores))-1]
    i_price = fake.random_int(1,100)
    i_aisle = fake.random_int(1,26)
    i_short_description = fake.text(150)
    i_item_number = fake.random_int(1,126)
    item = Item(name = i_name,
                store = i_store,
                price = i_price,
                aisle = i_aisle,
                short_description = i_short_description,
                item_number = i_item_number,
                )
    item.save()
    userOuter.favoriteItems.add(item)
    userOuter.save()
