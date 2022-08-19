class ArchiveNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ZIPError(Exception):
    def __init__(self, message):
        super().__init__(message)
