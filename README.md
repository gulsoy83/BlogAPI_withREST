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
![List of all posts](https://github.com/gulsoy83/BlogAPI_withREST/assets/46426033/d4b80279-76b1-4dad-8036-beef4b8e4598)
![View a specific post](https://github.com/gulsoy83/BlogAPI_withREST/assets/46426033/aaa5c4fd-0fd4-4fd6-b294-f7d9917c69bd)

Comment_api
![List of all comments](https://github.com/gulsoy83/BlogAPI_withREST/assets/46426033/f0646f0c-51ff-4dcd-8771-67a05a392c73)
![View a specific comment](https://github.com/gulsoy83/BlogAPI_withREST/assets/46426033/b71c7d2d-e411-4f68-a1f7-0ce6ba586c11)

User_api
![List of all users](https://github.com/gulsoy83/BlogAPI_withREST/assets/46426033/27c49fda-78d6-4dac-879f-e4396d462b57)
![View a specific user](https://github.com/gulsoy83/BlogAPI_withREST/assets/46426033/359a2680-a112-4348-9843-4b10ed370100)

