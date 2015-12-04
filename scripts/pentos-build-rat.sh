# CIS Router

yum -y install perl-YAML
yum -y install perl-CPAN

echo #======================================
echo download file to /root/Downloads
echo close Firefox window when you have completed
echo #======================================
echo
 
firefox https://benchmarks.cisecurity.org/downloads/form/index.cfm?download=rat.unix.253 

# assume that file is in /root/Downloads
cd /opt
unzip /root/Downloads/rat-2.5.3.zip 

perl -MCPAN -e 'my $c = "CPAN::HandleConfig"; $c->load(doit => 1, autoconfig => 1); $c->edit(prerequisites_policy => "follow"); $c->edit(build_requires_install_policy => "yes"); $c->commit'


perl -MCPAN -e 'install Net::Telnet'
#perl -MCPAN -e 'install Term::ReadKey'
perl -MCPAN -e 'install Test::Simple'
perl -MCPAN -e 'install Net::Telnet:Cisco'

cd /opt/rat
perl Makefile.PL
make
make install
