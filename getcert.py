#!/usr/bin/env python
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or distribute
# this software, either in source code form or as a compiled binary, for any
# purpose, commercial or non-commercial, and by any means.
#
# In jurisdictions that recognize copyright laws, the author or authors of this
# software dedicate any and all copyright interest in the software to the public
# domain. We make this dedication for the benefit of the public at large and to
# the detriment of our heirs and successors. We intend this dedication to be an
# overt act of relinquishment in perpetuity of all present and future rights to
# this software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>
#
# Oodles of love,
# katmagic

"""Get the digest of a host's SSL certificate."""

from __future__ import print_function
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

if __name__ == '__main__':
	import optparse

	op = optparse.OptionParser(
		usage='%prog [options] host',
		description="Get the digest of a host's SSL certificate.",
		version="0.1",
	)

	op.add_option(
		"-p",
		"--port",
		type=int,
		default=443,
		help="the port we should connect to (default: %default)"
	)

	digests = optparse.OptionGroup(op, "Digest Choices (default: sha1)")
	for dgst in ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'):
		digests.add_option(
			"--"+dgst,
			dest='digest',
			action='store_const',
			const=getattr(hashlib, dgst)
		)
	op.add_option_group(digests)
	op.set_default('digest', hashlib.sha1)

	try:
		(opts, (host,)) = op.parse_args()
	except ValueError:
		op.print_help()
		exit(1)

	try:
		digest = get_cert_digest(host, port=opts.port, digest=opts.digest)
	except socket.gaierror:
		exit("We couldn't connect to {0}:{1}".format(host, opts.port))
	except ssl.SSLError:
		exit("The remote host dosn't support SSL.")

	print(digest)
