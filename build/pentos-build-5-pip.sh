
pip install --upgrade --trusted-host pypi.python.org pip
pip install --upgrade setuptools
#pip3 install --upgrade --trusted-host pypi.python.org pip
#pip3 install --upgrade setuptools

# something wrong with pip compile environment
cp /usr/lib/python2.7/site-packages/packaging/requirements.py /usr/lib/python2.7/site-packages/packaging/requirements.py-orig
cp /opt/pentos/build/requirements.py /usr/lib/python2.7/site-packages/packaging/requirements.py

pip install --trusted-host pypi.python.org binwalk
pip install --trusted-host pypi.python.org incremental
pip install --trusted-host pypi.python.org awsscout2
pip install --trusted-host pypi.python.org crackmapexec
pip install --trusted-host pypi.python.org autopwn
pip install --trusted-host pypi.python.org trueseeing
pip install --trusted-host pypi.python.org harvester
pip install --trusted-host pypi.python.org scrapy
pip install --trusted-host pypi.python.org sslyze
pip install --trusted-host pypi.python.org olefile

# directory structure with multiple hooks
# need to test; nmap is failing
#pip install jarvis-pentest
#pip install jarvis

