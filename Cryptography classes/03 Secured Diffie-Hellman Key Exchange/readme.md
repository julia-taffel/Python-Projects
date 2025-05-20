Implement and Visualize a Secured Diffie-Hellman Key Exchange

Goal:
Implement a secure version of the Diffie-Hellman (DH) key exchange, protected against man-in-the-middle (MITM) attacks, and visualize the flow of secrets, keys, and public data exchanged between the parties.
Subtasks:

Basic Version (Unauthenticated DH):

     Implement classic DH over a finite field (e.g., 2048-bit prime modulus).

     Show how Alice and Bob independently compute the same shared secret.

Secured Version (Authenticated DH):

      Add digital signatures (e.g., RSA or ECDSA) to authenticate each party's public key.

      Alternatively, implement HMQV or SIGMA protocol if you want to go further.

      Simulate and detect MITM attacks (e.g., Mallory replaces keys mid-exchange).

Do the Visualization:

      Generation and exchange of public keys.

      Shared secret derivation.

      Flow of authentication (e.g., signature validation).

      An MITM scenario vs a protected one.