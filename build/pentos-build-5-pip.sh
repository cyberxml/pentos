
pip install --upgrade pip
pip3 install --upgrade pip

# something wrong with pip compile environment
cp /usr/lib/python2.7/site-packages/packaging/requirements.py /usr/lib/python2.7/site-packages/packaging/requirements.py-orig
cp /opt/pentos/build/requirements.py /usr/lib/python2.7/site-packages/packaging/requirements.py

pip install binwalk
pip install awsscout2
pip install crackmapexec
pip install autopwn
pip install trueseeing
pip install harvester
pip install scrapy
pip install sslyze

# directory structure with multiple hooks
pip install jarvis-pentest

