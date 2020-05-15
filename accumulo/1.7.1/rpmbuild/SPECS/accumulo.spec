%define _rpmfilename %%{NAME}-%%{VERSION}.3.1.4.0-315.%%{ARCH}.rpm
BuildRoot: /root/.tmp/rpmrebuild.73027/work/root
AutoProv: no
%undefine __find_provides
AutoReq: no
%undefine __find_requires
# Do not try autogenerate prereq/conflicts/obsoletes and check files
%undefine __check_files
%undefine __find_prereq
%undefine __find_conflicts
%undefine __find_obsoletes
# Be sure buildpolicy set to do nothing
%define __spec_install_post %{nil}
# Something that need for rpm-4.1
%define _missing_doc_files_terminate_build 0
#dummy
#dummy
#BUILDHOST:    ctr-e139-1542663976389-113618-01-000003.hwx.site
#BUILDTIME:    Fri Aug 23 05:14:28 2019
#SOURCERPM:    accumulo_3_1_4_0_315-1.7.0.3.1.4.0-315.src.rpm

#RPMVERSION:   4.11.3

#OS:           linux
#SIZE:           24215807
#ARCHIVESIZE:           24267280
#ARCH:         x86_64
BuildArch:     x86_64
Name:          accumulo_3_1_4_0_315
Version:       1.7.1
Release:       315
Summary:       Apache Accumulo is a distributed Key Value store based on Google's BigTable

License:       APL2 
Group:         Development/Libraries
URL:           http://accumulo.apache.org/
Source0:       accumulo-1.7.1-bin.tar.gz

Provides:      accumulo_3_1_4_0_315 = 1.7.1.3.1.4.0-315
Provides:      accumulo_3_1_4_0_315(x86-64) = 1.7.1.3.1.4.0-315
Provides:      config(accumulo_3_1_4_0_315) = 1.7.1.3.1.4.0-315
Provides:      libaccumulo.so()(64bit)  
Provides:      osgi(com.beust.jcommander) = 1.32.0
Provides:      osgi(com.google.gson) = 2.7.0
Provides:      osgi(com.google.guava) = 28.0.0
Provides:      osgi(com.google.protobuf) = 2.5.0
Provides:      osgi(javax.servlet-api) = 3.1.0
Provides:      osgi(jline) = 2.11.0
Provides:      osgi(org.apache.commons.cli) = 1.2
Provides:      osgi(org.apache.commons.codec) = 1.4
Provides:      osgi(org.apache.commons.collections) = 3.2.2
Provides:      osgi(org.apache.commons.configuration) = 1.10.0
Provides:      osgi(org.apache.commons.io) = 2.4.0
Provides:      osgi(org.apache.commons.lang) = 2.4
Provides:      osgi(org.apache.commons.math) = 2.1
Provides:      osgi(org.apache.commons.vfs) = 2.0
Provides:      osgi(org.apache.thrift) = 0.9.3-1
Provides:      osgi(org.eclipse.jetty.http) = 9.2.28
Provides:      osgi(org.eclipse.jetty.io) = 9.2.28
Provides:      osgi(org.eclipse.jetty.security) = 9.2.28
Provides:      osgi(org.eclipse.jetty.server) = 9.2.28
Provides:      osgi(org.eclipse.jetty.servlet) = 9.2.28
Provides:      osgi(org.eclipse.jetty.util) = 9.2.28
Provides:      osgi(slf4j.api) = 1.7.21
Provides:      osgi(slf4j.log4j12) = 1.7.21
Requires:      /bin/sh
Requires:      /sbin/chkconfig  
Requires:      /sbin/service  
Requires:      /usr/bin/env  
Requires:      /usr/sbin/useradd  
Requires:      config(accumulo_3_1_4_0_315) = 1.7.1.3.1.4.0-315
Requires:      coreutils  
Requires:      hadoop_3_1_4_0_315-hdfs  
Requires:      hdp-select >= 3.1.4.0-315
Requires:      libc.so.6()(64bit)  
Requires:      libc.so.6(GLIBC_2.2.5)(64bit)  
Requires:      libgcc_s.so.1()(64bit)  
Requires:      libgcc_s.so.1(GCC_3.0)(64bit)  
Requires:      libm.so.6()(64bit)  
Requires:      libstdc++.so.6()(64bit)  
Requires:      libstdc++.so.6(CXXABI_1.3)(64bit)  
Requires:      libstdc++.so.6(GLIBCXX_3.4)(64bit)  
Requires:      libstdc++.so.6(GLIBCXX_3.4.11)(64bit)  
Requires:      libstdc++.so.6(GLIBCXX_3.4.9)(64bit)  
Requires:      redhat-lsb  
#Requires:      rpmlib(CompressedFileNames) <= 3.0.4-1
#Requires:      rpmlib(FileDigests) <= 4.6.0-1
#Requires:      rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires:      rtld(GNU_HASH)  
Requires:      sh-utils  
Requires:      zookeeper_3_1_4_0_315  
#Requires:      rpmlib(PayloadIsXz) <= 5.2-1
#suggest
#enhance
%description
Apache Accumulo is a distributed key value store built on top of Apache Hadoop

prefix: %{buildroot}/usr/hdp/3.1.4.0-315/accumulo

%pre 
#!/bin/sh
getent group accumulo >/dev/null || groupadd -r accumulo

# Create an accumulo user if one does not already exist.
getent passwd accumulo >/dev/null || /usr/sbin/useradd --comment "accumulo" --shell /bin/bash -M -r -g accumulo -G accumulo --home /var/lib/accumulo accumulo

if [[ ! -e "/var/log/accumulo" ]]; then
    /usr/bin/install -d -o accumulo -g accumulo -m 0755 /var/log/accumulo
fi

if [[ ! -e "/var/run/accumulo" ]]; then
    /usr/bin/install -d -o accumulo -g accumulo -m 0755 /var/run/accumulo
fi

%global debug_package %{nil}

%prep

%setup -q -n accumulo-1.7.1

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/hdp/3.1.4.0-315/accumulo/bin
mkdir -p %{buildroot}/usr/hdp/3.1.4.0-315/accumulo/lib
mkdir -p %{buildroot}/usr/hdp/3.1.4.0-315/accumulo/doc
mkdir -p %{buildroot}/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist
mkdir -p %{buildroot}/usr/hdp/3.1.4.0-315/etc/default

cp -a %{_sourcedir}/accumulo/lib/ %{buildroot}/usr/hdp/3.1.4.0-315/accumulo/
cp -a %{_sourcedir}/accumulo/bin/ %{buildroot}/usr/hdp/3.1.4.0-315/accumulo/
\cp %{_sourcedir}/accumulo/bin/accumulo /root/rpmbuild/BUILD/accumulo-1.7.1/bin/accumulo
\cp %{_sourcedir}/accumulo/etc/accumulo %{buildroot}/usr/hdp/3.1.4.0-315/etc/default/accumulo
cp -a %{_builddir}/accumulo-%{version}/bin/ %{buildroot}/usr/hdp/3.1.4.0-315/accumulo/
cp -a %{_builddir}/accumulo-%{version}/lib/ %{buildroot}/usr/hdp/3.1.4.0-315/accumulo/
#cp -a %{_builddir}/accumulo-%{version}/conf/ %{buildroot}/usr/hdp/3.1.4.0-315/accumulo/
cp -a %{_builddir}/accumulo-%{version}/logs/ %{buildroot}/usr/hdp/3.1.4.0-315/accumulo/
cp -R %{_builddir}/accumulo-%{version}/docs/. %{buildroot}/usr/hdp/3.1.4.0-315/accumulo/doc
cp -a %{_builddir}/accumulo-%{version}/conf/examples/ %{buildroot}/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/
cp -a %{_builddir}/accumulo-%{version}/conf/templates/ %{buildroot}/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/
\cp %{_builddir}/accumulo-%{version}/conf/accumulo.policy.example %{buildroot}/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/accumulo.policy.example

# create sym links
ln -s /root/rpmbuild/BUILD/accumulo-1.7.1/conf %{buildroot}/usr/hdp/3.1.4.0-315/accumulo/conf

%files
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/LogForwarder.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/accumulo"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/accumulo.distro"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/accumulo_watcher.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/bootstrap_config.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/bootstrap_hdfs.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/build_native_library.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/check-slaves"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/config-server.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/config.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/generate_monitor_certificate.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/start-all.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/start-here.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/start-server.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/stop-all.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/stop-here.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/stop-server.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/tdown.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/tool.sh"
%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/bin/tup.sh"
#%attr(0777, root, root) "/usr/hdp/3.1.4.0-315/accumulo/conf"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/accumulo_user_manual.html"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/administration.html"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/bulkIngest.html"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/combiners.html"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/config.html"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/constraints.html"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/distributedTracing.html"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/documentation.css"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.batch"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.bloom"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.bulkIngest"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.classpath"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.client"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.combiner"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.constraints"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.dirlist"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.export"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.filedata"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.filter"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.helloworld"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.isolation"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.mapred"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.maxmutation"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.regex"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.reservations"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.rgbalancer"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.rowhash"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.shard"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.tabletofile"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.terasort"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/examples/README.visibility"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/index.html"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/isolation.html"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/lgroups.html"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/metrics.html"
%doc %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/doc/timestamps.html"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/VERSIONS"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-core.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-examples-simple.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-fate.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-gc.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-master.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-minicluster.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-monitor.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-native.tar.gz"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-proxy.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-server-base.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-shell.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-start.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-test.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-trace.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-tracer.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/accumulo-tserver.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/commons-cli.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/commons-codec.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/commons-collections.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/commons-configuration.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/commons-io.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/commons-lang.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/commons-logging.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/commons-math.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/commons-vfs2.jar"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/ext"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/gson.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/guava.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/htrace-core.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/htrace-core4.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/javax.servlet-api.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/jcommander.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/jetty-http.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/jetty-io.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/jetty-security.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/jetty-server.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/jetty-servlet.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/jetty-util.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/jline.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/libthrift.jar"
#%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/native"
#%attr(0755, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/native/libaccumulo.so"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/protobuf-java.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/slf4j-api.jar"
%attr(0644, root, root) "/usr/hdp/3.1.4.0-315/accumulo/lib/slf4j-log4j12.jar"
#%attr(0777, root, root) "/usr/hdp/3.1.4.0-315/accumulo/logs"
#%dir %attr(0775, root, root) "/usr/hdp/3.1.4.0-315/accumulo/walog"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/accumulo.policy.example"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/accumulo-env.sh"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/accumulo-metrics.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/accumulo-site.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/accumulo.policy.example"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/auditLog.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/gc"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/generic_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/generic_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/hadoop-metrics2-accumulo.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/log4j.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/masters"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/monitor"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/monitor_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/monitor_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/slaves"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/native-standalone/tracers"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/accumulo-env.sh"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/accumulo-metrics.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/accumulo-site.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/accumulo.policy.example"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/auditLog.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/gc"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/generic_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/generic_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/hadoop-metrics2-accumulo.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/log4j.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/masters"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/monitor"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/monitor_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/monitor_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/slaves"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/1GB/standalone/tracers"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/accumulo-env.sh"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/accumulo-metrics.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/accumulo-site.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/accumulo.policy.example"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/auditLog.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/gc"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/generic_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/generic_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/hadoop-metrics2-accumulo.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/log4j.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/masters"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/monitor"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/monitor_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/monitor_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/slaves"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/native-standalone/tracers"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/accumulo-env.sh"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/accumulo-metrics.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/accumulo-site.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/accumulo.policy.example"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/auditLog.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/gc"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/generic_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/generic_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/hadoop-metrics2-accumulo.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/log4j.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/masters"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/monitor"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/monitor_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/monitor_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/slaves"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/2GB/standalone/tracers"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/accumulo-env.sh"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/accumulo-metrics.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/accumulo-site.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/accumulo.policy.example"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/auditLog.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/gc"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/generic_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/generic_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/hadoop-metrics2-accumulo.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/log4j.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/masters"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/monitor"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/monitor_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/monitor_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/slaves"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/native-standalone/tracers"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/accumulo-env.sh"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/accumulo-metrics.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/accumulo-site.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/accumulo.policy.example"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/auditLog.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/gc"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/generic_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/generic_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/hadoop-metrics2-accumulo.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/log4j.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/masters"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/monitor"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/monitor_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/monitor_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/slaves"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/3GB/standalone/tracers"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/accumulo-env.sh"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/accumulo-metrics.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/accumulo-site.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/accumulo.policy.example"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/auditLog.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/gc"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/generic_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/generic_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/hadoop-metrics2-accumulo.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/log4j.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/masters"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/monitor"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/monitor_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/monitor_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/slaves"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/native-standalone/tracers"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/accumulo-env.sh"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/accumulo-metrics.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/accumulo-site.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/accumulo.policy.example"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/auditLog.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/gc"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/generic_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/generic_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/hadoop-metrics2-accumulo.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/log4j.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/masters"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/monitor"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/monitor_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/monitor_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/slaves"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/512MB/standalone/tracers"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/crypto"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/crypto/README"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/crypto/accumulo-site.xml"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/vfs-classloader"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/examples/vfs-classloader/accumulo-site.xml"
%dir %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/accumulo-env.sh"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/accumulo-metrics.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/accumulo-site.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/accumulo.policy.example"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/auditLog.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/gc"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/generic_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/generic_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/hadoop-metrics2-accumulo.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/log4j.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/masters"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/monitor"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/monitor_logger.properties"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/monitor_logger.xml"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/slaves"
%config %attr(0755, root, root) "/usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/templates/tracers"
%config %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/etc/default/accumulo"
#%config %attr(0644, root, root) "/usr/hdp/3.1.4.0-315/etc/security/limits.d/accumulo.nofiles.conf"

%post 
#!/bin/sh

/usr/bin/hdp-select --rpm-mode set accumulo-client 3.1.4.0-315
/usr/bin/hdp-select --rpm-mode set accumulo-gc 3.1.4.0-315
/usr/bin/hdp-select --rpm-mode set accumulo-master 3.1.4.0-315
/usr/bin/hdp-select --rpm-mode set accumulo-monitor 3.1.4.0-315
/usr/bin/hdp-select --rpm-mode set accumulo-tablet 3.1.4.0-315
/usr/bin/hdp-select --rpm-mode set accumulo-tracer 3.1.4.0-315
if [ !  -e "/etc/accumulo/conf" ]; then
    rm -f /etc/accumulo/conf
    mkdir -p /etc/accumulo/conf
    cp -rp /usr/hdp/3.1.4.0-315/etc/accumulo/conf.dist/* /etc/accumulo/conf
fi

# create sym links
ln -s /etc/accumulo/3.1.4.0-315/0 /usr/hdp/3.1.4.0-315/accumulo/conf
ln -s /var/log/accumulo /usr/hdp/3.1.4.0-315/accumulo/logs

localedef -i en_US -f UTF-8 en_US.UTF-8

%changelog

