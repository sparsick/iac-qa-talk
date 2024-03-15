def test_openjdk_is_installed(host):
    openjdk = host.package("openjdk-17-jdk")
    assert openjdk.is_installed

def test_tomcat_catalina_script_exist(host):
    assert host.file("/opt/tomcat/bin/catalina.sh").exists
