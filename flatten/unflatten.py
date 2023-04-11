from typing import List

from ._types import Packet, FlatPacket
from ._keys import unflatten_key

"""
Walks a list of keys into a packet, returning the value.
"""


def _walk(result: Packet, keys: List[str]) -> Packet:
    for key in keys:
        if key not in result:
            result[key] = {}
        result = result[key]
    return result


"""
Takes a flattened packet and reconstructs the nested objects
that were flattened, unescaping any escape sequences as it goes.
"""


def unflatten_packet(flat: FlatPacket) -> Packet:
    result = {}
    for key, val in flat.items():
        key_chain = unflatten_key(key)
        prefix, last = key_chain[:-1], key_chain[-1]
        sub_record = _walk(result, prefix)
        sub_record[last] = val
    return result
