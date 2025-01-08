import jmespath
import typing

def get_values_of_the_given_key(data: typing.Dict, key: str):
    response = jmespath.search(key, data)
    return response


data = {
  "ops": {
    "functionA": {"numArgs": 2},
    "functionB": {"numArgs": 3},
    "functionC": {"variadic": True},
    "funcD": [
      {
          "a": 123
      }
    ]
  }
}

# key = "ops.*.numArgs"
# key = "ops.*.variadic"
key = "ops.funcD[0].a"
print(get_values_of_the_given_key(data=data, key=key))

