from three_to_one import three_to_one_protocol_bob
from netqasm.sdk import EPRSocket
from netqasm.sdk.external import NetQASMConnection, Socket, get_qubit_state

def main(app_config=None):

    # Create a socket for classical communication
    socket = Socket("bob", "alice")
    print("socket created bob")

    # Create a EPR socket for entanglement generation
    epr_socket = EPRSocket("alice")

    # Initialize Bob's NetQASM connection
    bob = NetQASMConnection(
        app_name=app_config.app_name,
        epr_sockets=[epr_socket]
    )

    # Create Bob's context, initialize EPR pairs inside it and call Bob's EPL method. Finally, print out whether or not Bob successfully created an EPR Pair with Alice.

    with bob:
        # print("Now running with Bob")
        epr1 = epr_socket.recv()[0]
        epr2 = epr_socket.recv()[0]
        epr3 = epr_socket.recv()[0]

        result = three_to_one_protocol_bob(epr1, epr2, epr3, bob, socket)
        # print("Bob received result.")

        with open("filename.txt", "r") as f:
            filename_for_results = f.read().strip()  # Remove any extra whitespace or newline characters
            results_file_path = os.path.join("data", filename_for_results)
            # print(filename_for_results)

        # Write the result to a text file
        with open(results_file_path, "a") as f:
            if result:
                print("An EPR Pair was successfully created with Alice!")
                f.write("1\n")
            else:
                print("The protocol was not successful and no EPR Pair was created with Alice.")
                f.write("0\n")

if __name__ == "__main__":
    main()
