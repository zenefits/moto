from __future__ import unicode_literals
import logging
logging.getLogger('boto').setLevel(logging.CRITICAL)

__title__ = 'moto'
__version__ = '0.4.24.1'


from .swf import mock_swf  # flake8: noqa


try:
    # Need to monkey-patch botocore requests back to underlying urllib3 classes
    from botocore.awsrequest import HTTPSConnectionPool, HTTPConnectionPool, HTTPConnection, VerifiedHTTPSConnection
except ImportError:
    pass
else:
    HTTPSConnectionPool.ConnectionCls = VerifiedHTTPSConnection
    HTTPConnectionPool.ConnectionCls = HTTPConnection
