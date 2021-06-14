 # Advanced Search Endpoint
 
### Instructions
- Generally we use `GET` method to filter some data and return the API response, 
  but this case is a bit different, Even though the endpoint gets data based on filters, 
  the method signature is `POST`. I did this because if we have a big filter string
  the standard size of URL (2048 characters) will be crossed, Using `POST` method 
  we dont have  any such restrictions as we send the filters in `POST` data.
- We need to use `%%` for `CONTAINS` operation because python already has `%` operator 

### Structure
- Good way to structure a project is to abstract into 
  different layers (example database layer, parser layer etc.).
- Here I used MVC design pattern by separating the contexts.  

### Sample 
#### Request
`curl -i -H "Content-Type: application/json; charset=utf-8" -X POST 
--data '{"filter":{"CONTAINS":{"message": "error"}}' 
127.0.0.1:5000/advanced-search/`

#### Response
Status Code | Description
--- | --- 
400 | Not a valid JSON
200 | SUCCESS
500 | FAILED

### Enhancements
- We have only primary key constraint on id from DB level. 
  If this is the case then all DB operations will be very slow once DB size increases. 
  We need to add indexing for columns based on the usage (separately or combined).
- We need to sanitize the inputs for security reasons.
