import math


def epl_protocol_alice(q1, q2, alice, socket):
    """
    Implements Alice's side of the EPL distillation protocol.
    This function should perform the gates and measurements for EPL using
    qubits q1 and q2, then send the measurement outcome to Bob and determine
    if the distillation was successful.
    
    :param q1: Alice's qubit from the first entangled pair
    :param q2: Alice's qubit from the second entangled pair
    :param alice: Alice's NetQASMConnection
    :param socket: Alice's classical communication socket to Bob
    :return: True/False indicating if protocol was successful
    """
    a = epl_gates_and_measurement_alice(q1, q2)
    alice.flush()

    a = int(a)
    a = str(a)

    # Write below the code to send measurement result to Bob, receive measurement result from Bob and check if protocol was successful
    socket.send(a)
    b = socket.recv()

    if (a+b) == "11":
        return True

    else:
        return False


def epl_gates_and_measurement_alice(q1, q2):
    """
    Performs the gates and measurements for Alice's side of the EPL protocol
    :param q1: Alice's qubit from the first entangled pair
    :param q2: Alice's qubit from the second entangled pair
    :return: Integer 0/1 indicating Alice's measurement outcome
    """
    q1.cnot(q2)
    m2 = q2.measure()


    # m2 = int(m2)
    return m2


def epl_protocol_bob(q1, q2, bob, socket):
    """
    Implements Bob's side of the EPL distillation protocol.
    This function should perform the gates and measurements for EPL using
    qubits q1 and q2, then send the measurement outcome to Alice and determine
    if the distillation was successful.
    
    :param q1: Bob's qubit from the first entangled pair
    :param q2: Bob's qubit from the second entangled pair
    :param bob: Bob's NetQASMConnection
    :param socket: Alice's classical communication socket to Bob
    :return: True/False indicating if protocol was successful
    """
    b = epl_gates_and_measurement_bob(q1, q2)
    bob.flush()

    b = int(b)
    b = str(b)
    # Write below the code to send measurement result to Alice, receive measurement result from Alice and check if protocol was successful
    socket.send(b)  # Needs to be a string
    a = socket.recv()

    if (a + b) == "11":
        return True

    else:
        return False

def epl_gates_and_measurement_bob(q1, q2):
    """
    Performs the gates and measurements for Bob's side of the EPL protocol
    :param q1: Bob's qubit from the first entangled pair
    :param q2: Bob's qubit from the second entangled pair
    :return: Integer 0/1 indicating Bob's measurement outcome
    """
    q1.cnot(q2)
    m2 = q2.measure()

    # m2 = int(m2)

    return m2

