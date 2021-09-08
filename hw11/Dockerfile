FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -yq openssh-server whois netcat

RUN useradd -m -p $(mkpasswd -m sha-512 password) -s /bin/bash user

RUN mkdir /var/run/sshd
    
EXPOSE 22 25565

CMD ["/usr/sbin/sshd", "-D"]