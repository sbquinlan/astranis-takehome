from flatten import unflatten_packet


def test_defaults(defaults):
    assert all(
        original == unflatten_packet(flattened) for original, flattened in defaults
    )


def test_number_keys():
    original = {"1": 1, "2": 2, "3": {"3": 3, "4": {"4": 4}, "5": 5}}
    assert (
        unflatten_packet({"1": 1, "2": 2, "3.3": 3, "3.4.4": 4, "3.5": 5}) == original
    )
