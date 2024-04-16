# APIs

### What are APIs? How are they used and why are they so popular?

API stands for application programming interface.

APIs are a way for two or more computer programs or components to communicate with each other. It is a type of 
software interface, offering a service to other pieces of software.

They communicate to each other in a similar fashion to the image below.

![api_comms.svg](Markdown_Images%2Fapi_comms.svg)

### What is a REST API? 

A REST API is an application programming interface that conforms to the constraints 
of REST architecture.

![rest_arch.png](Markdown_Images%2Frest_arch.png)

### What makes an API RESTful?

A RESTful API is an architectural style for an application program interface (API) that uses HTTP requests 
to access and use data. That data can be used to GET, PUT, POST and DELETE data types, which refers to the 
reading, updating, creating and deleting of operations concerning resources.

### What are the REST API guidelines?

REST API guidelines are a set of best practices and conventions for designing and developing RESTful APIs. These 
guidelines ensure consistency, reliability, and scalability of APIs.

Here are some key REST API guidelines:

* Use Descriptive and Meaningful URIs: URIs (Uniform Resource Identifiers) should reflect the resources they represent in a clear and meaningful way. They should use nouns instead of verbs and follow a hierarchical structure.
* Use HTTP Methods Correctly: HTTP methods (GET, POST, PUT, DELETE, etc.) should be used as per their intended purpose. For example, use GET for retrieving resources, POST for creating resources, PUT/PATCH for updating resources, and DELETE for deleting resources.
* Use HTTP Status Codes Properly: Use standard HTTP status codes to indicate the outcome of API requests. For example, 200 for successful responses, 201 for resource creation, 400 for client errors, and 500 for server errors.
* Versioning: APIs should be versioned to ensure backward compatibility and allow for changes without breaking existing clients. Versioning can be done in the URI (e.g., /v1/resource) or through headers.
* Request and Response Formats: Use consistent request and response formats, such as JSON or XML. JSON is widely preferred due to its simplicity and readability.
* Use Pagination for Large Data Sets: When returning large collections of resources, use pagination to improve performance and reduce the load on the server.
* Security: Implement proper authentication and authorization mechanisms to protect sensitive data and resources. Use HTTPS for secure communication.
* Error Handling: Provide informative error messages in case of failures, including details about the error, possible causes, and how to resolve them.
* Documentation: Provide comprehensive documentation for the API, including endpoints, request/response formats, authentication methods, and usage examples.
* Rate Limiting: Implement rate limiting to prevent abuse and ensure fair usage of the API by clients.
* Caching: Use caching headers (e.g., Cache-Control, ETag) to improve performance and reduce server load by allowing clients to cache responses.
* HATEOAS (Hypermedia as the Engine of Application State): Optionally, include hypermedia links in API responses to provide navigation links to related resources, enabling clients to discover and interact with the API dynamically.

### What is HTTP? (What does it stand for? What is HTTPS?)

"The Hypertext Transfer Protocol is an application layer protocol in the Internet protocol suite model for distributed, 
collaborative, hypermedia information systems."

In layman terms HTTP is a protocol used for sharing and accessing information on the internet, enabling communication
between web servers and clients to retrieve web pages and other resources.

HTTPS (Hypertext Transfer Protocol Secure) is a secure version of HTTP that encrypts data exchanged between a web browser and a server, ensuring privacy and security for online communication and transactions.

### HTTP request structure

![HTTP_request.png](Markdown_Images%2FHTTP_request.png)

The picture above shows the HTTP request structure. It needs a verb/method which could be GET (Read), PUT (Update), POST (Create) or DELETE (Delete) to indicate the action being performed. A URL specifying the targeted resource.
A head expanding on additional information about the request. Then a body containing the data to be sent over used within a PUT or POST request.

### HTTP response structure

![HTTP_response.png](Markdown_Images%2FHTTP_response.png)

The picture above shows the HTTP response structure. It contains a response code that shows the outcome of the request some example of this are 404 not found and 200 OK. Headers again providing any additional information. The HTTP version showing what version of the HTTP protocol is being used for either the request or response. Finally, a optional body containing any data sent back to the client from the server usually in either JSON or HTML.

### What are the 5 HTTP verbs? And what does each do?

Here are 5 HTTP verbs and what each does.

* GET: The method used to request data from a specified resource. Some examples are web pages, images or files.
* POST: The method used to submit data to be processed to a specific resource. Could be adding a new image or file.
* PUT: The method used to update or replace an existing resource. PUT requests are idempotent, meaning that performing the same request multiple times has the same effect as performing it once.
* DELETE: The method used to delete a resource identified by a specific URL. DELETE requests are also idempotent, meaning that deleting a resource multiple times has the same effect as deleting it once.
* PATCH: The method used to apply partial modifications to a resource identified by a specific URI. It is commonly used when you want to update a part of a resource without replacing the entire resource. PATCH requests are also idempotent, meaning that performing the same request multiple times has the same effect as performing it once.

### What is "statelessness"?

If a HTTP protocol is stateless that means that every HTTP request the server receives is independent and does not relate to requests that came prior to it.

![state_stateless.png](Markdown_Images%2Fstate_stateless.png)

### Stateful Example:

In a stateful scenario, the server maintains the state of the shopping cart for each user session.

#### User Adds Items to Cart:
* User sends a POST request to the server to add an item to their shopping cart.
* Server updates the user's shopping cart in its memory/database.

#### User Views Cart:
* User sends a GET request to view their shopping cart.
* Server retrieves the user's shopping cart from its memory/database and sends it back to the user.

#### User Checks Out:
* User sends a POST request to the server to check out.
* Server processes the order, updates inventory, and sends a confirmation to the user.

In this scenario, the server maintains the state of the shopping cart for each user session, which requires keeping track of user sessions and their associated data.

### Stateless Example:

In a stateless scenario, the server does not maintain any client state between requests.

#### User Adds Items to Cart:
* User sends a POST request to the server to add an item to their shopping cart, including all necessary information in the request (e.g., user ID, item ID, quantity).
* Server processes the request, updates the shopping cart in its memory/database, and sends back a success response.

#### User Views Cart:
* User sends a GET request to view their shopping cart, including their user ID in the request.
* Server retrieves the user's shopping cart from its memory/database based on the provided user ID and sends it back to the user.

#### User Checks Out:
* User sends a POST request to the server to check out, including their user ID and shopping cart contents in the request.
* Server processes the order, updates inventory, and sends a confirmation to the user.

In this scenario, the server does not maintain any client state between requests. Each request from the user must include all necessary information for the server to process it, making it stateless.

### What is caching?

Caching is storing frequently used data in a temporary storage to speed up access and reduce the need to fetch data repeatedly from its original source. It helps improve performance by retrieving data quickly from the cache instead of fetching it from the server or database every time a request is made.