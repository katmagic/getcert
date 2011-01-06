#!/usr/bin/env python
import hashlib
import socket
import ssl
import re

def get_cert_digest(domain, port=443, digest=hashlib.sha1):
	"""Get the SHA-1 fingerprint of an SSL certificate."""

	# Get a connection to domain:port.
	sock = socket.socket()
	sock.connect( (domain, port) )

	# Get the SSL certificate.
	ssock = ssl.SSLSocket(sock)
	cert = ssock.getpeercert(binary_form=True)

	# Close the connection.
	ssock.close()
	sock.close()

	# Hash the SSL certificate.
	digest = digest(cert).hexdigest()
	# Make the SSL certificate hash pretty.
	digest = re.sub('(..)', r'\1:', digest)[0:-1].upper()

	return digest
