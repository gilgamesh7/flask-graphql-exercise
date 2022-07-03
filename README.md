# flask-graphql-exercise

## Youtube video by Arjan
https://youtu.be/7ccdWqGgHaM

## Flask Update Blog & Queries
- POST : http://127.0.0.1:5000/blogs/2
```
- Body (JSON) : 
{
    "author_id" : 2,
    "content" : "Content 2",
    "id" : 2,
    "title" : "I like this blog"
}
```
- GET Blogs : http://127.0.0.1:5000/blogs
- GET a Blog : http://127.0.0.1:5000/blogs/2
- GET authors : http://127.0.0.1:5000/authors
- GET an author : http://127.0.0.1:5000/authors/2

## GraphQL Queries
1. To get blogs with subset of field
```
query{
  blogs{
    id
    title
    content
  }
}
```
2. List of authors :
```
query{
  authors{
    id
    name
    }
  }
```
3. This will error out on author
```
query{
  blogs{
    id
    title
    content
    author
  }
}
```
4. Get author and Blog details
```
query{
  blogs{
    id
    title
    content
    author {
      id
      name
    }
  }
}

```
