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

class CertificateChecker(object):
	@staticmethod
	def get_cert(domain, port=443):
		"""Get the (binary) SSL certificate of domain:port."""

		# Get a connection to domain:port.
		sock = socket.socket()
		sock.connect( (domain, port) )

		# Get the SSL certificate.
		ssock = ssl.SSLSocket(sock)
		cert = ssock.getpeercert(binary_form=True)

		# Close the connection.
		ssock.close()
		sock.close()

		return cert

	@staticmethod
	def digest(data, digest=hashlib.sha1):
		"""Return a pretty-printed digest like they show in browser certificate
		information dialogs."""

		# Hash data.
		digest = digest(data).hexdigest()
		# Prettify it.
		return re.sub('(..)', r'\1:', digest)[0:-1].upper()

	@classmethod
	def get_cert_digest(cls, domain, port=443, digest=hashlib.sha1):
		"""Get the fingerprint of a domain:port's SSL certificate."""

		return cls.digest(cls.get_cert(domain, port), digest)

if __name__ == '__main__':
	import optparse
	CC = CertificateChecker

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

	op.add_option(
		'-c',
		'--show-cert',
		dest='show',
		action='store_const',
		const='certificate',
		help='show the received SSL certificate'
	)
	op.add_option(
		'-d',
		'--show-digest',
		dest='show',
		action='store_const',
		const='digest',
		help="show the digest of the received SSL certificate (default)"
	)
	op.set_default('show', 'digest')

	try:
		(opts, (host,)) = op.parse_args()
	except ValueError:
		op.print_help()
		exit(1)

	try:
		if opts.show == 'digest':
			digest = CC.get_cert_digest(host, port=opts.port, digest=opts.digest)
			print(digest)

		elif opts.show == 'certificate':
			certificate = ssl.get_server_certificate( (host, opts.port) ).rstrip()
			print(certificate)

	except socket.gaierror:
		exit("We couldn't connect to {0}:{1}".format(host, opts.port))
	except socket.error:
		exit("The remote host refused to establish a connection with us. Meanies!")
	except ssl.SSLError:
		exit("The remote host dosn't support SSL.")
	except KeyboardInterrupt:
		exit("")
