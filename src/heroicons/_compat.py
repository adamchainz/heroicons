import sys

if sys.version_info < (3, 9):

    def str_removeprefix(self: str, prefix: str) -> str:
        if self.startswith(prefix):
            return self[len(prefix) :]
        else:  # pragma: no cover
            return self[:]


else:
    str_removeprefix = str.removeprefix
