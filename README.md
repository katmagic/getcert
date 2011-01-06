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

By default, `getcert` will show you the SHA1 digest of the certificate. Use the
`-c` option to print the certificate, or the `--md5` (or `--sha224`, ...)
options to change the type of the certificate digest.

	$ ./getcert.py --md5 www.google.com
	C4:70:74:FB:69:F9:E3:94:7E:8B:28:A4:00:73:DE:01

	$ ./getcert.py -p 6697 irc.oftc.net
	97:86:48:39:4E:01:7B:B1:30:B7:00:32:40:07:56:95:EB:A0:59:96

	$ ./getcert.py -p 6697 -c irc.oftc.net
	-----BEGIN CERTIFICATE-----
	MIIEWDCCA0CgAwIBAgIBPDANBgkqhkiG9w0BAQUFADCBkjErMCkGA1UEChMiT3Bl
	biBhbmQgRnJlZSBUZWNobm9sb2d5IENvbW11bml0eTEoMCYGA1UECxMfY2VydGlm
	aWNhdGlvbiBhdXRob3JpdHkgZm9yIGlyYzEYMBYGA1UEAxMPaXJjLmNhLm9mdGMu
	bmV0MR8wHQYJKoZIhvcNAQkBFhBzdXBwb3J0QG9mdGMubmV0MB4XDTEwMDYyNTIy
	MTE0NloXDTExMDYyNTIyMTE0NlowGzEZMBcGA1UEAxMQb3Ntb3RpYy5vZnRjLm5l
	dDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAM0FY4X79WpY2B859TFl
	HoUxvhYdj9jDwj4jcxsTm7L5IHlb4NebfeJuN6y2tDvJrrNszlbOD8HCE8+4VNvO
	CL+FvJlHwq1vHOpsS1ugTFnBIcxzSmiXQguPdlLWoJAROutPgyEjDyyBhVEUHHyt
	sT4H4V0X+XRI5pSCHl63awUimjVKhMKi+rbm56yl5okUx79e/SD7G11ffSNlt3h/
	PAoUh0ftZ+N+Jx11tKCaHlKJhlhgaqUTVCO71ac2gJip4mc55KYdouJaYlj+MvQ2
	2/vDRy24IvP/X5RME8qrCEe+z0IXCdvTJrJWTzCDs2bQq1JHZKHDBLgrOidKTgI8
	dSMCAwEAAaOCAS0wggEpMAkGA1UdEwQCMAAwHQYDVR0OBBYEFHQaWCzzxnE4549k
	stF5QkwOP2aWMIGzBgNVHSMEgaswgaiAFD4msTg6Kk2C8rmG4OFx7V6LhwfPoYGM
	pIGJMIGGMSswKQYDVQQKEyJPcGVuIGFuZCBGcmVlIFRlY2hub2xvZ3kgQ29tbXVu
	aXR5MSAwHgYDVQQLExdDZXJ0aWZpY2F0aW9uIEF1dGhvcml0eTEUMBIGA1UEAxML
	Y2Eub2Z0Yy5uZXQxHzAdBgkqhkiG9w0BCQEWEHN1cHBvcnRAb2Z0Yy5uZXSCAQMw
	RwYDVR0RBEAwPoIMaXJjLm9mdGMubmV0gg1pcmM2Lm9mdGMubmV0gg1pcmNzLm9m
	dGMubmV0ghBvc21vdGljLm9mdGMubmV0MA0GCSqGSIb3DQEBBQUAA4IBAQAo/IAT
	CHNWaTiRLEEGisHL7E7t1lqiHTDKB6M9I7UFdXL6QWfCPAJ+4h19GIBZLjJ3iI8I
	3aeRwTwSXmJH0WWpbPEgwEyaeKW/b4i6ijyNlEqf/OR5LM99Ot7GPQgl/KbIjhvQ
	lmoWRa1v0Zb0xXH8DMfuTPxBMbKdL0RGl4TZ1g/9SAukTo/mYBflrxBFu/s+T/g/
	3Ia3Vbvhby2QbTYL4GLCHt+yVySgxXAfgJlo1kt7wBGp4mRxBsuhk1H/Jr0fGJDH
	vgEc4EWX9Ck4NGFdrSTLyV2DlMESN7Qs7fCN94yRcnsp2D8w9lcyyd4krbHlK2eR
	kecxIMRXbGRfNEkf
	-----END CERTIFICATE-----

Usage in Scripts
----------------

`getcert` supports both Python 2 and 3. Here is a riveting example:

	import getcert
	getcert.get_cert_digest('github.com')
