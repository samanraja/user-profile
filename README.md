# user-profile-api
Basic CRUD API based on user and user-profile.



## API Reference

#### Create User

```http
  POST /api/user/create
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your username |
| `email` | `string` | **Required**. Your email |
| `password` | `string` | **Required**. Your password |


```http
  POST /api/user/login
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your username |
| `email` | `string` | **Required**. Your email |
| `password` | `string` | **Required**. Your password |



#### Update User Profile

```http
  PUT user/profile/update
```
Needs Token <token> obtained after login in header.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `phone` | `string` | **Required**. Phone Number |
| `default_address` | `dictionary` | **Required**. Default Address Details |
| `password` | `string` | **Required**. Your password |
| `profile_picture` | `string` | **Required**. address of profile_picture |
| `hobbies` | `list` | **Required**. List of Hobbies ID |

#### default_address Field Description
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | **Required**. ID of address |
| `address` | `string` | **Required**. Address |
| `is_default` | `boolean` | **Required**. true/false|

#### Add Address

```http
  POST /user/address/create/
```
Needs Token <token> obtained after login in header.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `address`      | `string` | **Required**. New Address |
| `is_default`      | `boolean` | **Required**. true/false |


#### Add Address

```http
  DELETE /user/delete/<int:id>/
```
Needs Token <token> obtained after login in header.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. ID of user |


