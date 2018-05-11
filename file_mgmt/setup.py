from setuptools import setup

setup(name='fd_file_mgmt',
      version='0.2.0',
      description='FreeDict file management utilities',
      author='The FreeDict Developers',
      author_email='freedict@freelists.org',
      url='https://github.com/freedict/tools',
      license='GPL3',
      py_modules=['fd_file_mgmt'],
      install_requires=[],
      entry_points={'console_scripts':
          ['fd_api=fd_api:main',
           'fd_file_mgr=fd_file_mgr:main']}
)
