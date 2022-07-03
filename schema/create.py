from ariadne import make_executable_schema
from graphql.type.schema import GraphQLSchema
from schema.types import MAIN_TYPEDEF, mutation, query
from schema.blog import BLOGTYPE_DEF, blog_query
from schema.author import AUTHOR_TYPEDEF

def create_schema() -> GraphQLSchema:
    return make_executable_schema([MAIN_TYPEDEF, BLOGTYPE_DEF, AUTHOR_TYPEDEF], [query, blog_query, mutation])

