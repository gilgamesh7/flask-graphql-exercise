from graphql import GraphQLResolveInfo
from schema.types import query, mutation
from data import Blog, BlogPayLoad, all_blogs, get_blog, update_blog, get_author
from ariadne import ObjectType
from typing import Any

BLOGTYPE_DEF="""
    type Blog{
        id : ID!
        title: String!
        content: String!
        author: Author!
    }
    
    input BlogPayload{
        title: String!
        content: String!
    }

    type Mutation {
        update_blog(id: ID!, payload: BlogPayload!) : Blog
    }
    """

@query.field("blogs")
def resolve_blogs(_, info: GraphQLResolveInfo)-> list[Blog]:
    return all_blogs()

@query.field("blog")
def resolve_blogs(_, info: GraphQLResolveInfo, blog_id: int)-> list[Blog]:
    return get_blog(blog_id)

@mutation.field("update_blog")
def resolve_update_blog(_, info: GraphQLResolveInfo, id: str, payload: BlogPayLoad) -> Blog:
    return update_blog(int(id), payload)


