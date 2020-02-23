# Rest API

- Rest is a way of thinking about how a web server responds to your requests
- It doesn't respond with just data
- It responds with resources
- similar to object-oriented programming. Think of the server as having resources, and each is able to interact with the pertinent request.
- can GET, POST, PUT, DELETE '/item/chair' (Item resource). Get /items would be ItemList resource.

## Stateless

- Another key feature is that REST is supposed to be stateless
- This means one request cannot depend on any other requests
- The server only knows about the current request, and not any previous requests
- for example: POST /item/chair creates an item
  - the server does not know the item now exists
  - GET /item/chair then goes to the database and checks to see if the item is there
  - to get an item you do not need to have created an item before--the item could be in the database from previously
- Another example: a user logs in to a web application
  - The web server does not know the user is logged in (since it does not remember any state)
  - The web application must send enough data to identify the user in every request, or else the server won't associate the request with the user.
