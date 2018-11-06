import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from faker import Faker

from shop.models import Store, Item

fake = Faker()

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
    items.append(store);

print("\nStore:")
for i in Store.objects.all():
    print(i)

print("\nItem:")
for i in Item.objects.all():
    print(i)
