# (C) 2016, MIT License

import unittest
import itertools
from os import path
from bz2_rl import BZ2FileIter

CWD = path.dirname(path.realpath(__file__))


class TestConverter(unittest.TestCase):
    '''
    Run this using ./setup.py test. BZ2 files were compressed using:

        bzip2 -k -z -9 input_file.txt

    Both Unix and Windows linebreaks are tested.
    Note: this is by no means an exhaustive test, but it's a start.
    '''
    def _compare_files(self, txt, bz2de):
        '''
        Compares two text files to see if their contents are identical;
        one a plain text file, and one a BZ2 compressed file that will be
        processed with BZ2FileIter. This tests using self.assertEqual(),
        rather than returning True or False.

        :param txt: Text file path
        :param bz2de: BZ2FileIter instance with BZ2 compressed file
        '''
        with open(txt, 'r') as file_txt:
            lines_txt = itertools.chain(file_txt.readlines())

        for line in bz2de:
            if line == '':
                break
            txt_line = next(lines_txt)
            bz2_line = line
            self.assertEqual(txt_line, bz2_line)

    def test_bz2de_crlf(self):
        '''
        Tests BZ2FileIter behavior on files with CRLF linebreaks.
        '''
        path_txt = '{}/test_crlf.txt'.format(CWD)
        path_bz2 = '{}/test_crlf.txt.bz2'.format(CWD)
        bz2de = BZ2FileIter(path_bz2)

        self._compare_files(path_txt, bz2de)
        bz2de._close()

    def test_bz2de_lf(self):
        '''
        Tests BZ2FileIter behavior on files with Unix linebreaks.
        '''
        path_txt = '{}/test_lf.txt'.format(CWD)
        path_bz2 = '{}/test_lf.txt.bz2'.format(CWD)
        bz2de = BZ2FileIter(path_bz2)

        self._compare_files(path_txt, bz2de)

if __name__ == '__main__':
    unittest.main()
