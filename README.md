# iac-qa-talk
Slides and sample code from my talk "Infastructure as Code - Muss man nicht testen, Hauptsache es läuft" at embarc Architektur-Punsch at 17h December 2020.

All code samples are in `samples`.
The code samples are tested with Ansible 2.9.6  and Vagrant 2.2.14.

Following test tools are used:
- Ansible-lint 4.3.7
- Testinfra 6.1.0

## Setup Test Infrastructure
I prepare some Vagrantfiles for the setup of the test infrastructure if necessary.
The only prerequires are that you have to install VirtualBox and Vagrant on your machine.
Then follow these steps:

1. Open a CLI and go to the location of the file `Vagrantfile`.
2. Call `vagrant up`. Vagrant will download the necessary image for VirtualBox. That will take some times.

Hint: Public and private keys can be generated with the following command: `ssh-keygen`


## Ansible Playbooks
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
