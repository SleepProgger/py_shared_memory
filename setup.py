from distutils.core import setup, Extension
import sys

module1 = Extension('_posixshmem',
                    define_macros = [('HAVE_SHM_OPEN', '1'), ('HAVE_SHM_UNLINK', '1'), ('HAVE_SYS_MMAN_H', '1')],
                    libraries = ['rt'],
                    sources = ['posixshmem.c'])

setup (name = 'Shared memory backport',
       version = '1.0',
       description = 'Simple backport of the multiprocessing.shared_memory module freshlay landed in python3.8',
       py_modules = ['shared_memory'],
       ext_modules = [module1] if not sys.platform.startswith("win") else []
       )
