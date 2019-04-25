from distutils.core import setup, Extension
import sys
import platform

linux_module = Extension('_posixshmem',
                    define_macros = [('HAVE_SHM_OPEN', '1'), ('HAVE_SHM_UNLINK', '1'), ('HAVE_SYS_MMAN_H', '1')],
                    libraries = ['rt'],
                    sources = ['posixshmem.c'])
darwin_module = Extension('_posixshmem',
                    define_macros = [('HAVE_SHM_OPEN', '1'), ('HAVE_SHM_UNLINK', '1'), ('HAVE_SYS_MMAN_H', '1')],
                    sources = ['posixshmem.c'])

setup (name = 'shared-memory-backport',
       version = '1.1',
       description = 'Simple backport of the multiprocessing.shared_memory module freshlay landed in python 3.8',
       py_modules = ['shared_memory'],
       ext_modules = [linux_module] if platform.system() == 'Linux' else [darwin_module] if platform.system == 'Darwin' else []
       )
