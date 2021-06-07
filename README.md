# iac-qa-talk
Slides and sample code from my workshop "Continuous Integration für Infrastructure as Code" at API Summit Remote at 9th June 2021.

All code samples are in `samples`.

There are three samples chapter, one for Ansible, Docker and Helm Charts.


## Samples for Ansible
The code samples `samples/ansible` are tested with Ansible 2.9.6  and Vagrant 2.2.14.

Following test tools are used:
- Ansible-lint 4.3.7
- Testinfra 6.1.0

### Setup Test Infrastructure
I prepare some Vagrantfiles for the setup of the test infrastructure if necessary.
The only prerequires are that you have to install VirtualBox and Vagrant on your machine.
Then follow these steps:

1. Open a CLI and go to the location of the file `Vagrantfile`.
2. Call `vagrant up`. Vagrant will download the necessary image for VirtualBox. That will take some times.

Hint: Public and private keys can be generated with the following command: `ssh-keygen`


### Ansible Playbooks
Ansible playbook samples are in `samples`.
This is also the location for the next CLI calls.

- Code quality check for Ansible playbooks with Ansible-lint: `ansible-lint *.yml`
- Running ansible playbooks against the test infrasructure (see chapter 'Setup Test Infrastructure' above):
```
ansible-playbook -i inventories/test setup-tomcat.yml
```
- Running testinfra tests against a provisioned VM:
```
py.test --connection=ansible --ansible-inventory inventory/test -v tests/*.py
```

## Samples for Docker
The code samples `samples/docker` are tested with Docker 20.10.3.

Following test tools are used:
- Haskell Dockerfile Linter (hadolint) 1.22.1-no-git
- Container Structure Test 1.10.0

### Docker Linting

```shell
cd samples/docker
hadolint Dockerfile
```

### Docker Structure Tests

```shell
cd samples/docker

docker build -t sparsick/spring-boot-demo:latest .
container-structure-test test --image sparsick/spring-boot-demo:latest --config spring-boot-test.yaml
```


## Samples for Helm Charts
The code samples `samples/helm-charts` are tested with Helm Chart 3.5.2 and Minikube 1.17.1 (uses Kubernetes )

Following test tools are used:
- terratest 0.32.3

### Setup Test Infrastructure

```shell
cd samples/helm-charts
minikube start --addons=ingress
helm upgrade -i spring-boot-demo-instance spring-boot-demo -f local-values.yaml
```
Call `minikube ip` to find out the IP address of your Minikube cluster and add it in your `/etc/hosts`


```shell
// /etc/hosts
192.168.49.2    spring-boot-demo.local
```
then you can see the application in your browser with http://spring-boot-demo.local/hero

### Helm Charts Linting

```shell
cd samples/helm-charts
helm lint spring-boot-demo -f local-values.yaml
```

### Helm Charts Tests with Terratest

The tests are located in `samples/helm-charts/test`. If you want to run the test, you need a running minikube and Golang on your machine.

```shell
cd samples/helm-charts/test
go test . -v
```
