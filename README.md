# Django Rest Framework Assignment with Signals

## Project Overview
Task is creating a Django Rest Framework (DRF) application that allows users to create, read, update, and delete (CRUD) posts. The application should have the following functionality:
1. The user should be able to create a post by providing a title, body, and author.
2. The user should be able to retrieve a list of all posts, or a specific post by ID.
3. The user should be able to update or delete their own posts.
4. Whenever a new post is created, an email should be sent to the author with a notification of the creation.

## Requirements
1. The application should have an authentication system using Django's built-in User model.
2. The Post model should have the following fields:
   - **title** (CharField): The title of the post.
   - **body** (TextField): The body of the post.
   - **author** (ForeignKey to User model): The user who wrote the post.
3. The API endpoints should follow RESTful conventions:
   - **GET /api/posts/**: Returns a list of all posts.
   - **POST /api/posts/**: Creates a new post owned by the authenticated user.
   - **GET /api/posts/<int:pk>/**: Returns a single post by ID.
   - **PUT /api/posts/<int:pk>/**: Updates a single post owned by the authenticated user.
   - **DELETE /api/posts/<int:pk>/**: Deletes a single post owned by the authenticated user. (delete should work as soft delete)
4. Create an API where one user can block another user (Blocked User functionality)
   - **GET api/get-blocked-user/**: return the user data whom you have blocked
   - **POST :api/block-user/**: user 1 can block user 2
   - **DELETE: api/unblock-user/**: user1 can unblock the user 2
5. The user should only be able to CRUD their own posts.
6. All API endpoints should return JSON responses.
7. You should use DRF's Generic APIView or APIVIEW and serializers whenever possible.(DO NOT USE generics.ListCreateAPIView or generics.RetrieveUpdateDestroyAPIView)
8. You should use DRF's authentication and permission classes to enforce authentication and ownership of posts.
9. Whenever a new post is created, an email should be sent to the author notifying them of the creation.
10. You should use Django signals to trigger the email notification whenever a new post is created. Advanced Permissions
    - Implement custom permissions to allow superusers to have full access to all posts and update or delete any post regardless of ownership.
    - Non-superuser regular users should only be able to CRUD their own posts.

## Advanced Serializers:
1. Implement a nested serializer to include the author's username and email when retrieving a single post. The author's full details should not be displayed on the list of all posts.

## Requirements (IMP):
1. Allow users to filter posts by title, body, and author using query parameters on the GET /api/posts/ endpoint.
2. Implement pagination for the GET /api/posts/ endpoint.
3. Implement rate limiting to prevent abuse of the API.
4. Create get api for filtering post by author. Get author id and filter that author’s post
5. Add search feature in (get all post api) that user can search from author’s name and post title .(It should contain OR condition by using Q object)
6. Add support for categorizing posts using tags or categories. You can create endpoints for adding, retrieving, and managing tags or categories associated with posts.
7. Create one api that i can retrieve the post through categories.
