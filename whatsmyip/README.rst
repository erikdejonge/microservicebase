whatsmyip
=====

Start manually
--------------

In this current folder, launch: `api_hour -ac whatsmyip:Container`

Deploy using Ansible
--------------------

#. `ansible-playbook ansible/install.yml -i ansible/inventory`
#. Customize config files in /etc/whatsmyip/
#. Merge rsyslog config file
#. service whatsmyip start

Deploy new version using Ansible
--------------------------------

#. `ansible-playbook ansible/update.yml`

Manual install
--------------

#. Follow pythonz install doc: https://github.com/saghul/pythonz
#. pythonz install 3.4.3
#. cd /opt
#. Git clone your app here
#. cd /opt/whatsmyip/
#. /usr/local/pythonz/pythons/CPython-3.4.3/bin/pyvenv pyvenv
#. . pyvenv/bin/activate
#. pip install -r requirements.txt
#. cd /etc/init.d/ && ln -s /opt/whatsmyip/etc/init.d/whatsmyip
#. To define right boot order for your daemon (for example, your daemon needs PostgreSQL), customize file header of: /opt/whatsmyip/etc/default/whatsmyip
#. cd /etc/default/ && ln -s /opt/whatsmyip/etc/default/whatsmyip
#. update-rc.d whatsmyip defaults
#. cp -a /opt/whatsmyip/etc/whatsmyip /etc/
#. Adapt rsyslog and logrotate
#. For logrotate config file, apply the access rights: rw-r--r--
#. service whatsmyip start

To restart automatically daemon if it crashes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. apt-get install monit
#. cd /etc/monit/conf.d/ && ln -s /opt/whatsmyip/etc/monit/conf.d/whatsmyip
#. service monit restart
