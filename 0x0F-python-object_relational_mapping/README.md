## Object Relational Mapping
> Each file in this repository holds code that illustrates an essential concept of programming,
> specific to databases and uses MySQLdb and sqlAlchemy with Python scripts

### Resources
[ORMs](https://www.fullstackpython.com/object-relational-mappers-orms.html), [SQLAlchemy](https://www.fullstackpython.com/sqlalchemy.html), [MySQLdb documentation](https://mysqlclient.readthedocs.io/), [Python MySQL documentation](http://www.mikusa.com/python-mysql-docs/index.html), [SQLAlchemy documentation](http://docs.sqlalchemy.org/en/latest/orm/tutorial.html), [prevent SQL injections](http://bobby-tables.com/python)

### Environment
* Language: Python 3.8.x
* Databases: MySQL 8.x, MySQLdb v2.0.3, sqlAlchemy v1.4.22
* OS: Ubuntu 20.04 LTS
* Compiler: python3
* Style guidelines: [PEP 8 (version 1.7) for Python 3.5](https://www.python.org/dev/peps/pep-0008/) || [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

MySQLdb
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.verion_info
(2, 0, 3, 'final', 0)
```
SQLAlchemy
```
$ pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```
