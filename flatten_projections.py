import jmespath
import typing

def get_values_of_the_given_key(data: typing.Dict, key: str):
    response = jmespath.search(key, data)
    return response


data = {
  "reservations": [
    {
      "instances": [
        {"state": "running"},
        {"state": "stopped"}
      ]
    },
    {
      "instances": [
        {"state": "terminated"},
        {"state": "running"}
      ]
    }
  ]
}
key = "reservations[*].instances[*].state[]"
response = get_values_of_the_given_key(data=data, key=key)
print(response)


data = [
  [0, 1],
  2,
  [3],
  4,
  [5, [6, 7]]
]
key = "[][]"
response = get_values_of_the_given_key(data=data, key=key)
print(response)