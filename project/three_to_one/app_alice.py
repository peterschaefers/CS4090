from three_to_one import three_to_one_protocol_alice
from netqasm.sdk import EPRSocket
from netqasm.sdk.external import NetQASMConnection, Socket


def main(app_config=None):
    # Create a socket for classical communication
    socket = Socket("alice", "bob")

    # Create a EPR socket for entanglement generation
    epr_socket = EPRSocket("bob")

    # Initialize Alice's NetQASM connection
    alice = NetQASMConnection(
        app_name=app_config.app_name,
        epr_sockets=[epr_socket]
    )

    with alice:
        epr1 = epr_socket.create()[0]
        epr2 = epr_socket.create()[0]
        epr3 = epr_socket.create()[0]

        result = three_to_one_protocol_alice(epr1, epr2, epr3, alice, socket)

if __name__ == "__main__":
    main()
