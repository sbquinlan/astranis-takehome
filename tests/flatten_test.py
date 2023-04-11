from flatten import flatten_packet

def test_defaults(defaults):
  assert all(flatten_packet(original) == flattened for original, flattened in defaults)

def test_numbers():
  packet = {
    1: 1,
    2: 2,
    3: {
      3: 3,
      4: {
        4: 4
      },
      5: 5
    }
  }
  assert flatten_packet(packet) == {'1': 1, '2': 2, '3.3': 3, '3.4.4': 4, '3.5': 5}