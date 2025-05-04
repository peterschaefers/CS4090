import math


def three_to_one_protocol_alice(q1, q2, q3, alice, socket):
    """
    Implements Alice's side of the BBPSSW distillation protocol.
    This function should perform the gates and measurements for 3->1 using
    qubits q1 and q2, then send the measurement outcome to Bob and determine
    if the distillation was successful.
    
    :param q1: Alice's qubit from the first entangled pair
    :param q2: Alice's qubit from the second entangled pair
    :param q3: Alice's qubit from the third entangled pair
    :param alice: Alice's NetQASMConnection
    :param socket: Alice's classical communication socket to Bob
    :return: True/False indicating if protocol was successful
    """

    # print("Running 321 protocol Alice")
    outcome1, outcome2 = three_to_one_gates_and_measurement_alice(q1, q2, q3)
    # print("Ran measurements alice")
    alice.flush()

    # print("Flushing")
    print(outcome1)

    outcome1 = int(outcome1)
    outcome1 = str(outcome1)

    outcome2 = int(outcome2)
    outcome2 = str(outcome2)

    a = outcome1 + outcome2

    socket.send(a)
    b = socket.recv()

    if a == b:
        return True

    else:
        return False


def three_to_one_gates_and_measurement_alice(q1, q2, q3):
    """
    Performs the gates and measurements for Alice's side of the 3->1 protocol
    :param q1: Alice's qubit from the first entangled pair
    :param q2: Alice's qubit from the second entangled pair
    :param q3: Alice's qubit from the third entangled pair
    :return: A pair of integer 0/1 indicating Alice's measurement outcomes from measuring the qubits
    """

    q3.cnot(q2)
    q1.cnot(q3)

    #We need to measure q1 and q2 in the bell basis, so we apply cnot + H
    q1.cnot(q2)
    q1.H()

    m1 = q1.measure()
    m2 = q2.measure()

    return m1, m2
def three_to_one_protocol_bob(q1, q2, q3, bob, socket):
    """
    Implements Bob's side of the 3->1 distillation protocol.
    This function should perform the gates and measurements for 3->1 using
    qubits q1 and q2, then send the measurement outcome to Alice and determine
    if the distillation was successful.
    
    :param q1: Bob's qubit from the first entangled pair
    :param q2: Bob's qubit from the second entangled pair
    :param q3: Bob's qubit from the third entangled pair
    :param bob: Bob's NetQASMConnection
    :param socket: Alice's classical communication socket to Bob
    :return: True/False indicating if protocol was successful
    """
    # print("Running 321 protocol bob")
    outcome1, outcome2 = three_to_one_gates_and_measurement_bob(q1, q2, q3)
    # print("Ran 321 gates bob")
    bob.flush()

    outcome1 = int(outcome1)
    outcome1 = str(outcome1)

    outcome2 = int(outcome2)
    outcome2 = str(outcome2)

    b = outcome1 + outcome2

    socket.send(b)
    a = socket.recv()

    if b == a:
        return True

    else:
        return False

def three_to_one_gates_and_measurement_bob(q1, q2, q3):
    """
    Performs the gates and measurements for Bob's side of the 3->1 protocol
    :param q1: Bob's qubit from the first entangled pair
    :param q2: Bob's qubit from the second entangled pair
    :param q3: Bob's qubit from the third entangled pair
    :return: A pair of integer 0/1 indicating Bob's measurement outcomes from measuring the qubits
    """
    q3.cnot(q2)
    q1.cnot(q3)

    # We need to measure q1 and q2 in the bell basis, so we apply cnot + H
    q1.cnot(q2)
    q1.H()

    m1 = q1.measure()
    m2 = q2.measure()

    return m1, m2

