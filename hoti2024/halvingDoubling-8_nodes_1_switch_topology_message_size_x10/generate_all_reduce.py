import os

from chakra.third_party.utils.protolib import encodeMessage as encode_message
from chakra.et_def.et_def_pb2 import (
    Node as ChakraNode,
    BoolList,
    GlobalMetadata,
    AttributeProto as ChakraAttr,
    COMM_COLL_NODE,
    ALL_REDUCE,
)


def main() -> None:
    # create directories
    if not os.path.exists("./allreduce"):
        os.makedirs("./allreduce")
    

    # metadata
    npus_count = 8  # 8 NPUs
    coll_size = 10_485_760  # 10 MB

    for npu_id in range(npus_count):
        output_filename = f"allreduce/allreduce.{npu_id}.et"
        with open(output_filename, "wb") as et:
            # Chakra Metadata
            encode_message(et, GlobalMetadata(version="0.0.4"))

            # create Chakra Node
            node = ChakraNode()
            node.id = 1
            node.name = "All-Reduce"
            node.type = COMM_COLL_NODE

            # assign attributes
            node.attr.append(ChakraAttr(name="is_cpu_op", bool_val=False))
            node.attr.append(ChakraAttr(name="comm_type", int64_val=ALL_REDUCE))
            node.attr.append(ChakraAttr(name="comm_size", uint64_val=coll_size))
            node.attr.append(ChakraAttr(name="involved_dim", bool_list=BoolList(values=[True])))

            # store Chakra ET file
            encode_message(et, node)


if __name__ == "__main__":
    main()