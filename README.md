getcert
=======

About
-----

`getcert` is a simple Python script that allows you to determine the digests of
SSL certificates. It support MD5, SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512.
It might be useful when you want to check from a script whether someone is
running a [man in the middle attack][MITM].
[MITM]: https://secure.wikimedia.org/wikipedia/en/wiki/Man-in-the-middle_attack

Command Line Usage Examples
---------------------------

	$ ./getcert.py --md5 www.google.com
	C4:70:74:FB:69:F9:E3:94:7E:8B:28:A4:00:73:DE:01

	$ ./getcert.py -p 6697 irc.oftc.net
	97:86:48:39:4E:01:7B:B1:30:B7:00:32:40:07:56:95:EB:A0:59:96


Usage in Scripts
----------------

`getcert` supports both Python 2 and 3. Here is a riveting example:

	import getcert
	getcert.get_cert_digest('github.com')
