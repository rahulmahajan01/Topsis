from distutils.core import setup
setup(
  name = 'Rahul Mahajan',         
  packages = ['Topsis-Rahul-101803526'],  
  version = '0.1',     
  license='MIT',       
  description = 'Topsis project evaluation',   
  author = 'Rahul Mahajan',                   
  author_email = 'rmahajan1_be18@thapar.edu',     
  url = 'https://github.com/rahulmahajan01/Topsis/',   
  download_url = 'https://github.com/rahulmahajan01/Topsis/archive/v_01.tar.gz',    
  keywords = ['TOPSIS','IMPLEMENTATION','PYTHON'],   
  install_requires=[           
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6'
  ],
)