from typing import Generator, Tuple

from ._types import Packet, FlatPacket, LeafVal
from ._keys import flatten_key

"""
Yields (key, value) tuples like {}.items() where the keys are flattened.

This does a DFS into nested Dicts, yielding the non-Dict leaf values
with prefixed keys.
"""


def _gen_flattened_items(root: Packet) -> Generator[Tuple[str, LeafVal], None, None]:
    stack = [(None, root.items())]
    while stack:
        prefix, records = stack.pop()
        for key, val in records:
            flat_key = flatten_key(prefix, key)
            try:
                stack.append((flat_key, val.items()))
            except:
                yield (flat_key, val)


"""
Flattens a packet so that there are no nested dicts, but the 
keys still retain a "nested-like" syntax. Meaning that a key 
to a nested Dict will prefix the keys of the nested keys in 
the result, separated by a '.'

Keep in mind that '.' could exist in the keys of the original 
packet in which case, it will be 'escaped' using the char '|'
which will also be escaped if it was in the original packet keys.
"""


def flatten_packet(packet: Packet) -> FlatPacket:
    return {k: v for k, v in _gen_flattened_items(packet)}
