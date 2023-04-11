from pytest import fixture

@fixture(scope='module')
def example():
  return [
    {
      'a': 1,
      'b': 2,
      'c': {
        'd': 3,
        'e': {
          'f': 4
        },
        'g': 5
      },
    },
    {
      'a': 1, 
      'b': 2, 
      'c.d': 3, 
      'c.e.f': 4, 
      'c.g': 5
    }
  ]

@fixture(scope='module')
def empty():
  return [{}, {}]

@fixture(scope='module')
def empty_key():
  return [{'': { '': 'a' }}, {'.': 'a'}]

@fixture(scope='module')
def escaped_key():
  return [{'.': { '|' : 'a' }}, {'|..||': 'a'}]

@fixture(scope='module')
def complex_keys():
  return [{'.||.|': { '.||' : 'a', '|.|' : '||||' }}, {'|.|||||.||.|.||||': 'a', '|.|||||.||.|||.||': '||||'}]

@fixture(scope='module')
def defaults(example, empty, empty_key, escaped_key, complex_keys):
  return [example, empty, empty_key, escaped_key, complex_keys]