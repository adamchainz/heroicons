import sys

if sys.version_info < (3, 9):

    def str_removeprefix(self, prefix):
        if self.startswith(prefix):
            return self[len(prefix) :]
        else:
            return self[:]


else:
    str_removeprefix = str.removeprefix
