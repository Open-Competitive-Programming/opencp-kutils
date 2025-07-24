import sys

from importlib.metadata import PackageNotFoundError, version


try:
    dist_name = "opencp-kutils"
    __version__ = version(dist_name)
except PackageNotFoundError:
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
