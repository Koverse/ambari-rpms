# ambari-rpms
spec files and sources for building rpms

Steps to create an rpm of a new version of an HDP service
-------

Note: Building rpms should be done on a linux OS

1. Run `yum install rpm-build rpmrebuild rpmdevtools`
2. Run `rpmdev-setuptree`
3. Download rpm for HDP 3.1.4.0 version of service https://docs.cloudera.com/HDPDocuments/Ambari-2.7.3.0/bk_ambari-installation/content/hdp_31_repositories.html
4. Download the tar.gz for the service and version you will be building an rpm for
5. Run `rpmrebuild -e -p <rpm_file>` and when the editor opens save the spec file to /root/rpmbuild/SPECS directory ex. :w /root/rpmbuild/SPECS/<filename>
6. Modify spec file as needed (this will likely be significant, accumulo specs can be used as examples)
7. When you are ready to test run `rpmbuild -ba <spec_filename>`
8. The rpm will be available in /root/rpmbuild/RPMS directory
9. Test the rpm by running a `yum localinstall <rpm_name>`

Steps to test an rpm on ambari
-------

1. Run `createrepo /root/rpmbuild/RPMS`, a repodata folder will be created in RPMS directory
2. Upload the rpm and repodata directory to a folder in S3
3. On a docker image with ambari installed, add the url to the S3 folder to /var/lib/ambari-server/resources/stacks/HDP/3.1/repos/repoinfo.xml
4. Update the service version in /var/lib/ambari-server/resources/stacks/HDP/3.1/services/metainfo.xml
5. Restart ambari-server and ambari-agent
6. Login to ambari and create a cluster selecting your sevice and all dependency services

