#!/usr/bin/env python
import hashlib
import ssl
import re

def get_cert_digest(domain, port=443, digest=hashlib.sha1):
	"""Get the SHA-1 fingerprint of an SSL certificate."""

	# Get the SSL certificate.
	try:
		ssock = ssl.SSLSocket(ssl_version=ssl.PROTOCOL_TLSv1)
		ssock.connect( (domain, port) )
		cert = ssock.getpeercert(binary_form=True)
	finally:
		ssock.close()

	# Hash the SSL certificate.
	digest = digest(cert).hexdigest()
	# Make the SSL certificate hash pretty.
	digest = re.sub('(..)', r'\1:', digest)[0:-1].upper()

	return digest
