from distutils.core import setup
setup(
  name = 'sitemappy',         # How you named your package folder
  packages = ['sitemappy'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A package for the generation and analyis of sitemaps',   # Give a short description about your library
  author = 'Jack Tilley',                   # Type in your name
  author_email = 'tilley.e.jack@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Jack-Tilley/sitemappy',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Jack-Tilley/sitemappy/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['python3', 'webscrape', 'sitemap', 'network'],   # Keywords that define your package best
  install_requires=[            
          'selenium',
          'beautifulsoup4',
          'requests',
          'webscraping_tools'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
  ],
)