# Leftover5 - Down the Aisle - Fall 2018

# Overview of Application
Our application "Down the Aisle" effectively will allow users to login, select the store they want to make a shopping list for, be able to search for the items they want, put them into their cart, and finally generate a map showing where each item is and the fastest route to get it. What we implemented includes loading mock users that are able to login and view data related to that user as well as modifying data. For our application, we updated how some of the functionality of the search bar works and various other little changes to accommodate the implementation of user authentication and user interaction. Everything we outlined in the previous submission is still the same, including our intention of not fully implementing creating a user generated map.

# Team Members
* Mina Bruso, minaalexandra96
* Harold Rubio, haroldrubio
* Harmon Lau, hungrygiraffe
* Kiyanna Sully, leftover5-ksully
* Evan Geremia, egeremia

# User Interface
## Homepage - the glue that connected the application together
![homepage](imgs/homepage-UI.png)

## Profile Page - has user settings and favorites
![profile](imgs/profile-UI.png)

## User Preferences - contains password reset and other user settings
![user preferences](imgs/password-reset-UI.png)

## Favorite Items - contains a user's favorite items
![favorite items](imgs/favorite-item-UI.png)

## Favorite Cart - contains a user's favorite cart
![favorite cart](imgs/favorite-cart-UI.png)

## Add Item to Favorites - allows a user with special permissions to add an item to their favorite items list
![add item](imgs/add-to-faves-UI.png)

## Login Error - error page if permissions or login is required to view a page
![error](imgs/page-error-UI.png)

## Add Item Success - success page to let user know the item was actually added to their favorite items list
![add item success](imgs/success-UI.png)

## Store Select - list of stores for user to shop from 
![store select](imgs/store-select-UI.png)

## Items / Cart - displays all items in store and cart so far
![items/cart](imgs/item-cart-UI.png)

## Map - the main point of the app - displays the mapped route based on the user's cart
![map](imgs/map_screen-UI.png)


# Design Overview
We implemented simple login functionality. When the user is logged in, they will have access to "My Profile" and "Logout" on the navbar at the top. "My Profile" has general user data such as username and password, and some statistics about their favorite stores and shopping lists.

We also added the admin group and admin django page. We ensured that only admin users had access to this page - not the general users - and that when we changed the data on the page, it was displayed properly on the main website. To get to the admin page, we have to manually navigate to `localhost:8080/admin` in the address bar. 

We also have a third user group that contains 1 general user and the admins. This group has access to the "Add Item to Favorites" tab on the navbar, which takes the user to a form to add items to their favorites list under the "Profile" tab. Right now it's setup so that the user types in the item they want to add to their list, but ideally we would have it so that the user can select the item from a store to add to their list. This can be polished up later.


# Problems/Successes
Getting the data to be unique for each user was difficult to implement and get working properly. The user interatction part was also difficult and there were a lot of road blocks that presented themselves when trying to makes sure each user can modify data. It all came together in the end though and we are all sataisfied with it. In addition, we ran into some issues involving having enough time to complete what we want to complete with the break happening right before the submission. However, we were able to successfully implement what was required and have all the functionality working. A good amount of the time we felt rushed and time crunched but it worked out in the end and everyone worked well together. For the last stretch of the semester, we all will need to make sure that we will have enough time to finalize the application.

# Team Choice
Our team choice was a password reset. There is a link to password reset/user preferences on the user profile page. 
