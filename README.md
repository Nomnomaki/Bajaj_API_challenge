# Bajaj API Challenge

This is a simple REST API built with **Flask** and deployed on **Vercel**.  
It takes in an array of values and returns the following:  

- API status  
- User ID (format: `full_name_ddmmyyyy`)  
- Email ID  
- College Roll Number  
- Array of even numbers  
- Array of odd numbers  
- Array of alphabets (converted to uppercase)  
- Array of special characters  
- Sum of all numeric values (returned as a string)  
- Concatenation of all alphabets in reverse order with alternating capitalization  

---

## Hosted API
**Endpoint:**  

https://bajaj-api-challenge-seven.vercel.app/bfhl


**Method:** `POST`  
**Content-Type:** `application/json`  

---

### Example Request
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}

```
### Example Response
```json
{
  "is_success": true,
  "user_id": "aniket_saxena_27082004",
  "email": "aniket.saxena2022a@vitstudent.ac.in",
  "roll_number": "22BRS1050",
  "even_numbers": ["334", "4"],
  "odd_numbers": ["1"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```
--- 

### Testing the API with curl

You can test the live API endpoint using curl:
Example 
```bash
curl -X POST https://bajaj-api-challenge-seven.vercel.app/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data":["a","1","334","4","R","$"]}'
  ```
