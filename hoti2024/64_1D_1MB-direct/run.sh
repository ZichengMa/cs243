# #!/bin/bash
# # Absolue path to this script
# SCRIPT_DIR=$(dirname "$(realpath $0)")
# # Absolute paths to useful directories
# ASTRA_SIM_DIR="${SCRIPT_DIR:?}"/../astra-sim
# NS3_DIR="${ASTRA_SIM_DIR:?}"/extern/network_backend/ns-3
# # Inputs - change as necessary.
# WORKLOAD="${SCRIPT_DIR:?}"/../../extern/graph_frontend/chakra/one_comm_coll_node_allgather
# SYSTEM="${SCRIPT_DIR:?}"/inputs/Ring.json
# MEMORY="${SCRIPT_DIR:?}"/inputs/RemoteMemory.json
# LOGICAL_TOPOLOGY="${ASTRA_SIM_DIR:?}"/inputs/network/ns3/sample_8nodes_1D.json
# # Note that ONLY this file is relative to NS3_DIR/simulation
# NETWORK="../../../ns-3/scratch/config/config.txt"

#!/bin/bash
set -e

# Path
SCRIPT_DIR=$(dirname "$(realpath $0)")
ASTRA_SIM_BUILD_DIR=${SCRIPT_DIR}/../astra-sim/extern/network_backend/ns-3/build/scratch/
ASTRA_SIM=./ns3.42-AstraSimNetwork-default

# Run ASTRA-sim
(
cd ${ASTRA_SIM_BUILD_DIR}
${ASTRA_SIM} \
    --workload-configuration=${SCRIPT_DIR}/allreduce_64/allreduce \
    --system-configuration=${SCRIPT_DIR}/inputs/Collective_Algo_sys.json \
    --remote-memory-configuration=${SCRIPT_DIR}/inputs/RemoteMemory.json \
    --logical-topology-configuration=${SCRIPT_DIR}/inputs/logical_64nodes_1D.json \
    --network-configuration=../../../ns-3/scratch/config/config_64_nodes_32_switch_topology.txt \
    --comm-group-configuration=\"empty\"
)
