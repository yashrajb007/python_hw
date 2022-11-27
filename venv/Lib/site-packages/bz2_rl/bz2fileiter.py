# (C) 2016, MIT license

'''
BZ2 compressed text file streamer, iterator version. Yields full lines only.
'''
import os
from bz2 import BZ2Decompressor

SYSLB = os.linesep.encode('utf-8')
CRLF = b'\r\n'
LF = b'\n'
EOF = b''


class BZ2FileIter:
    '''
    Iterates through a bzip2 compressed text file, decoding as it goes along
    and yielding lines one by one until the end of the file. Since the file
    is not completely contained in memory, it can be used to decode
    and process very large text files line-by-line efficiently.

    Usage is very simple: make an instance with at least the path to the file
    as argument, then iterate over it. For example:

        sql_lines = BZ2FileIter(sql_path)
        for line in sql_lines:
            # ...

    The file is closed automatically after the last line. If you don't need
    to iterate over the file anymore, simply delete the BZ2FileIter instance
    to close the file.
    '''
    def __init__(self, bz2_file=None, encoding='utf-8', read_size=512,
                 linebreak=None, _cvlb=SYSLB):
        '''
        Sets up the streamer and opens the file. If no file path is passed,
        the consumer can open the file manually with self.set_file() later.

        :param bz2_file: path to the bzip2 compressed file, or None
        :param encoding: Text encoding
        :param read_size: Number of bytes to read at a time
        :param linebreak: Force linebreak type (auto-detected if None)
        '''
        self.file = None
        self.encoding = encoding
        self.read_size = read_size
        self.linebreak = linebreak

        self._lb = _cvlb  # All linebreaks are converted to system default.
        self._bz2de = BZ2Decompressor()

        if bz2_file is not None:
            self.file = open(bz2_file, 'rb')

    def _find_linebreak(self, buffer):
        '''
        Checks a byte buffer to see if a linebreak can be found.
        If a linebreak is found, it is saved as self.linebreak
        (either Windows CRLF or Unix LF), and True is returned.
        If no linebreak is found in the buffer, False is returned.

        :param buffer: Byte string from the stream
        :return: True if linebreak is identified, False otherwise
        '''
        if CRLF in buffer:
            self.linebreak = CRLF
        elif LF in buffer:
            self.linebreak = LF
        else:
            return False

        return True

    def set_file(self, file):
        '''
        Sets the file stream manually, in case you prefer to open the file
        yourself.
        '''
        self.file = file

    def _close(self):
        '''
        Closes the file.
        '''
        if self.file is not None:
            self.file.close()

    def __del__(self):
        '''
        Ensures that the file is closed on destruction.
        '''
        self._close()

    def __iter__(self):
        '''
        Iterator that runs through the compressed file and yields only
        full lines explicitly terminated by a linebreak.
        '''
        # String buffer that will contain decompressed text.
        buffer = b''

        while True:
            # Read a series of compressed bytes.
            file_bytes = self.file.read(self.read_size)

            if file_bytes == EOF:
                # File has reached EOF, so close it and stop iteration
                # after yielding the remaining line of the file.
                yield buffer.decode(self.encoding)
                self._close()
                return

            # Decompress bytes and interpret using the correct encoding.
            buffer += self._bz2de.decompress(file_bytes)

            # Detect linebreak style if we don't know yet.
            if self.linebreak is None:
                # If we can't find a linebreak, continue seeking the file.
                if not self._find_linebreak(buffer):
                    continue

            # Yield lines if we have any; put the remainder back in the buffer.
            if self.linebreak in buffer:
                lines = buffer.split(self.linebreak)

                for line in lines[:-1]:
                    yield (line + self._lb).decode(self.encoding)

                buffer = lines[-1]
