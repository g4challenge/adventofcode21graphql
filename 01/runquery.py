from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://graphql88.stepzen.net/api/88912f9ae4a47ecd9418a11864ca75fb/__graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Unsplash "Mock Query"
query_mock = gql(
    """
    query UnsplashQueries {
  unsplash_Stats_Month {
    new_developers
    new_requests
  }
  unsplash_Collections {
    curated
    featured
    id
    private
  }
  unsplash_Stats {
    applications
    downloads
    developers
  }
  unsplash_Search(query: "red") {
    results
  }
}

    """
)
query_real = gql(
    """
    query UnsplashQueries(
  $unsplash_clientId: !Secret
) {
  unsplash_Stats_Month(
    unsplash_clientId: $unsplash_clientId
  ) {
    new_developers
    new_requests
  }
  unsplash_Collections(
    unsplash_clientId: $unsplash_clientId
  ) {
    curated
    featured
    id
    private
  }
  unsplash_Stats(
    unsplash_clientId: $unsplash_clientId
  ) {
    applications
    downloads
    developers
  }
  unsplash_Search(
    query: "red"
    unsplash_clientId: $unsplash_clientId
  ) {
    results
  }
}
    """)

result = client.execute(query_real)
print(result)