# Overview of Application
Our application "Down the Aisle" effectively will allow users to login, select the store they want to make a shopping list for, be able to search for the items they want, put them into their cart, and finally generate a map showing where each item is and the fastest route to get it. Our layout will be designed so that the navigation bar is simple and gets you where you need to go. Selecting what store you want then loading the item data for that store will be simple, smooth, and easy process for the user. Moving items to your cart will provide easy flexibility and usability (when dealing with multiple of the same item, deleting items from cart, etc.). Checking out and getting a map based on your shopping cart will be very useful and one of the main attractions to our application for users. Although this is a cool feature, we are unsure if we will be able to implement it with the time we have, so that might have to be implemented, for now, in a really basic form.

# Team Members
* Mina Bruso, minaalexandra96
* Harold Rubio, haroldrubio
* Harmon Lau, hungrygiraffe
* Kiyanna Sully, leftover5-ksully
* Evan Geremia, egeremia


# Video Link
Here is our youtube link to our demo video: https://youtu.be/SQGc5OGcEoQ

# Design Overview
We implemented Item, List, UserModel, and Store in our models.py file which each represent a part of our data model we drew. The Item model defines an item that will be displayed after clicking a store. It has its own atributes that define what it is and what price it is. A Store model has a name and Item models associated with it that will be displayed to the user. The List model has many Item models associated with it and will be displayed to the user when they want to see their shopping cart. Finally, the UserModel model has a username and their favorite store and favorite cart as attributes. Our major urls inlcude the four buttons on our navbar: Login, Stores, Map, MyProfile. There is also a shopping cart logo that takes you to the homepage where you can select a store. Also, in MyProfile, the urls for the user's favorite cart and items fucntion and display mock data.

# Problems/Successes
We have run into some coordination issues trying to get everyone together to work on the project submission. This is due to the time of year being very busy for everyone and it's hard for schedules to line up. However, we were able to successfully implement a django project using the example in class as a guideline and going from there. There were a lot of times where everyone felt lost but we leaned on each other for support and helped each other deepen their understanding. In the future, we all will need to put more priority on this project as it will require even more time and effort to get it into a presentable form.
