# Threaded-Comments-API-Server
Comment Thread API Server using Django and DRF

### Functionalities

- Get all the comments and their respective replies on a page
- Add a comment or a reply (sub comment)
- Edit a comment or a reply
- Delete a comment or the whole thread. (The whole thread gets deleted if the parent comment is deleted)

### Technologies used
- Framework: Django
- Rest API: Django Rest Framework
- database: PostgresSql

### Endpoint for different functionalities
#### Get all comments: http://localhost:8000 or http://localhost:8000/get_all_comments 
#### Create a new comment: http://localhost:8000/create_comment/
  - Create a new comment: 
```
# input
{ 
    "comment_body": "hello",
    "is_sub_comment": 0,  # Boolean (Only True when comment is a reply)
    "parent_id": -1    # if the comment itself is the parent, set parent_id = -1

}
```
   - Add a reply:
```
# input
{ 
    "comment_body": "hello",
    "is_sub_comment": 1,
    "parent_id": 3  # the ID of the parent comment

}
```
#### Edit a comment:  http://localhost:8000/edit_comment/
 ```
 # input
{
  "comment_id": 5,
  "comment_body": "hello2",
}
```
#### Delete a comment: http://localhost:8000/delete_comment/
```
# input
{
  "comment_id": 5
}
```


