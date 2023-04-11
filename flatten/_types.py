from typing import Dict, Union

LeafVal = Union[str, int, float]
FlatPacket = Dict[str, LeafVal]
Packet = Dict[str, Union[LeafVal, "Packet"]]
