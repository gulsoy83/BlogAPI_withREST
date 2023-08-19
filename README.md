# BlogAPI_withREST
This API consists of three parts, post_api, comment_api and user_api.
When accessed, the main urls; "/api_basic/comment_api", "/api_basic/post_api", "/api_basic/user_api" automatically redirect you to /list path. 
(e.g. /api_basic/XXXX_api/list/) There, you can view all instances of that type.

To create a new instance for comment or post model, head to the "/api_basic/post_api/create/" or "/api_basic/comment_api/create/".
To delete an instance of comment or post model, head to the "/api_basic/post_api/delete/<slug>" or "/api_basic/comment_api/delete/<int:pk>".
To update an instance of comment or post model, head to the "/api_basic/post_api/update/<slug>" or "/api_basic/comment_api/update/<int:pk>".
To view an instance of comment or post model, head to the "/api_basic/post_api/list/<slug>" or "/api_basic/comment_api/list/<int:pk>".
(Post objects can be accessed by their unique slugs (e.g. <slug>), in the other hand, user and comment objects can be accessed by their unique integer ID's (e.g. <int:pk>).)

! Creating a new user requires the use of django admin panel.

Only logged users can create posts, comments.
A post or comment can only be updated/deleted by it's owner or by supervisors.
A comment instance must have a masterPost. 
A comment can be written under another comment. In this scenerio, it will have both masterPost and masterComment instance.

Post_api 
![List of all posts](https://github.com/gulsoy83/BlogAPI_withREST/assets/46426033/ffc04c33-be0a-410d-8e1d-46674db81878)
![View a specific post](https://github.com/gulsoy83/BlogAPI_withREST/assets/46426033/a3d1caf1-fdd4-4435-9cc6-549a3441b346)

Comment_api
![List of all comments](https://github.com/gulsoy83/BlogAPI_withREST/assets/46426033/cd3c771b-9140-4a1b-97f7-c5707bc481cf)
![View a specific comment](https://github.com/gulsoy83/BlogAPI_withREST/assets/46426033/18f9d7a4-211d-43f5-8e6a-c44454a7f743)

User_api
![List of all users](https://github.com/gulsoy83/BlogAPI_withREST/assets/46426033/2433fc59-d32b-4c33-86f2-d6de9c99023b)
![View a specific user](https://github.com/gulsoy83/BlogAPI_withREST/assets/46426033/8888c9c7-57ea-4dca-90a5-1060b848ec3c)


