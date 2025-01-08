import jmespath
import typing

def get_values_of_the_given_key(data: typing.Dict, key: str):
    response = jmespath.search(key, data)
    return response


data = {
  "machines": [
    {"name": "a", "state": "running"},
    {"name": "b", "state": "stopped"},
    {"name": "c", "state": "running"}
  ]
}
key = "machines[?name=='a']"
response = get_values_of_the_given_key(data=data, key=key)
print(response)


"""
Pipe Expressions
"""

data = {
  "people": [
    {"first": "James", "last": "d"},
    {"first": "Jacob", "last": "e"},
    {"first": "Jayden", "last": "f"},
    {"missing": "different"}
  ],
  "foo": {"bar": "baz"}
}
key = "people[*].first | [0]"
response = get_values_of_the_given_key(data=data, key=key)
print(response)
