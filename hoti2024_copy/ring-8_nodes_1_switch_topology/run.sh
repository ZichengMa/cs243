#!/bin/bash
set -e

# Path
SCRIPT_DIR=$(dirname "$(realpath $0)")
ASTRA_SIM_BUILD_DIR=${SCRIPT_DIR}/../astra-sim/extern/network_backend/ns-3/build/scratch/
ASTRA_SIM=./ns3.42-AstraSimNetwork-default

# Run ASTRA-sim
(
cd ${ASTRA_SIM_BUILD_DIR}
# echo "${ASTRA_SIM} \
#     --workload-configuration=${SCRIPT_DIR}/../demo1/allreduce/allreduce \
#     --system-configuration=${SCRIPT_DIR}/inputs/Ring_sys.json \
#     --remote-memory-configuration=${SCRIPT_DIR}/inputs/RemoteMemory.json \
#     --logical-topology-configuration=${SCRIPT_DIR}/inputs/logical_8nodes_1D.json \
#     --network-configuration=${SCRIPT_DIR}/../astra-sim/extern/network_backend/ns-3/scratch/config/config_8_nodes_1_switch_topology.txt \
#     --comm-group-configuration=\"empty\""
${ASTRA_SIM} \
    --workload-configuration=${SCRIPT_DIR}/../demo1/allreduce/allreduce \
    --system-configuration=${SCRIPT_DIR}/inputs/Ring_sys.json \
    --remote-memory-configuration=${SCRIPT_DIR}/inputs/RemoteMemory.json \
    --logical-topology-configuration=${SCRIPT_DIR}/inputs/logical_8nodes_1D.json \
    --network-configuration=${SCRIPT_DIR}/../astra-sim/extern/network_backend/ns-3/scratch/config/config_8_nodes_1_switch_topology.txt \
    --comm-group-configuration=\"empty\"
)


