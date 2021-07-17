from query_api import QueryAPI

q = input('What would you like me to search?')
query = QueryAPI()
res = query.make_request(user_query=q, endpoint='search')
print(f'You can find the answer to your question here: { res }')


