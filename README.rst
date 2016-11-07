==========================
ckanext-userautoaddtogroup
==========================

CKAN plugin to add new users to an existing group automatically. This takes care of the 
scenario that users should be able to add datasets to any group.

This plugin implements the ``user_create`` action to add users to an existing
group with a given role (both specified in the configuration - See Config
Settings below).

------------
Requirements
------------

Tested with CKAN v2.6

------------
Installation
------------


To install ckanext-userautoaddtogroup:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-userautoaddtogroup Python package into your virtual environment::

     pip install ckanext-userautoaddtogroup

3. Add ``userautoaddtogroup`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

::

    # The group to which new users are added
    ckan.userautoaddtogroup.group_name = my_organization

    # The role the new users will have
    ckan.userautoaddtogroup.group_role = editor


------------------------
Development Installation
------------------------

To install ckanext-userautoaddtogroup for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/aptivate/ckanext-userautoaddtogroup.git
    cd ckanext-userautoaddtogroup
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.userautoaddtogroup --cover-inclusive --cover-erase --cover-tests


----------------------------------------------
Registering ckanext-userautoaddtogroup on PyPI
----------------------------------------------

ckanext-userautoaddtogroup should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-userautoaddtogroup. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


-----------------------------------------------------
Releasing a New Version of ckanext-userautoaddtogroup
-----------------------------------------------------

ckanext-userautoaddtogroup is availabe on PyPI as https://pypi.python.org/pypi/ckanext-userautoaddtogroup.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags

-----
About
-----
This is a minor modification of the CKAN Extension userautoadd:
Copyright (c) 2016 `MapAction <http://mapaction.org>`_. Developed by `Aptivate <http://aptivate.org>`_.

Development of v1 of this plugin was funded by `ECHO <http://ec.europa.eu/echo>`_.

.. image:: http://www.echo-visibility.eu/wp-content/uploads/2014/02/EU_Flag_HA_2016_EN-300x272.png
   :alt: "Funded by European Union Humanitarian Aid"
