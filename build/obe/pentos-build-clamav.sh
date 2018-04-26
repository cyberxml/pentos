
echo "[dag]" > /etc/yum.repos.d/dag.repo
echo "name=Dag RPM Repository for Red Hat Enterprise Linux" >> /etc/yum.repos.d/dag.repo
echo "baseurl=http://apt.sw.be/redhat/el6/en/x86_64/dag/" >> /etc/yum.repos.d/dag.repo
echo "gpgcheck=1" >> /etc/yum.repos.d/dag.repo
echo "gpgkey=http://dag.wieers.com/packages/RPM-GPG-KEY.dag.txt" >> /etc/yum.repos.d/dag.repo
echo "enabled=1" >> /etc/yum.repos.d/dag.repo

yum -y install clamd
