# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))