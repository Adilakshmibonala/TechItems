import jmespath
import typing

def get_values_of_the_given_key(data: typing.Dict, key: str):
    response = jmespath.search(key, data)
    return response


data = {
  "people": [
    {"first": "James", "last": "d"},
    {"first": "Jacob", "last": "e"},
    {"first": "Jayden", "last": "f"},
    {"missing": "different"}
  ],
  "foo": {"bar": "baz"}
}
# key = "people[*].first"
# key = "people[*].missing"
key = "people[:2].first"
print(get_values_of_the_given_key(data=data, key=key))

