# [Leiland - Medium Article](https://medium.com/@lejiend/create-sftp-container-using-docker-e6f099762e42)
FROM ubuntu:16.04

RUN apt-get update && apt-get install -y openssh-server

# configure sftp user
RUN useradd -rm -d /home/sftp_user -s /bin/bash -G sudo -u 10001 sftp_user
RUN echo "sftp_user:SFTPUSERPASSWORDHERE" | chpasswd

# necessary sshd file
RUN mkdir /var/run/sshd

# SSH login fix (Keeping Session Alive). If not, user will be kick off after ssh
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"

RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 80 22 443
CMD ["/usr/sbin/sshd", "-D"]

#setup directory for sftp
RUN mkdir -p /var/sftp/uploads
RUN chown root:root /var/sftp
RUN chmod 755 /var/sftp
RUN chown sftp_user:sftp_user /var/sftp/uploads

# update to only allow sftp and not ssh tunneling to limit the non-necessary activity
RUN echo '\n\
Match User sftp_user  \n\
ForceCommand internal-sftp \n\
PasswordAuthentication yes \n\
ChrootDirectory /var/sftp \n\
PermitTunnel no  \n\
AllowAgentForwarding no \n\
AllowTcpForwarding no \n\
X11Forwarding no ' >> /etc/ssh/sshd_config



# # Install nginx
# RUN apt-get update \
#     && apt-get install -y supervisor \
#     && apt-get install -y nginx \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
#     && echo "daemon off;" >> /etc/nginx/nginx.conf

# RUN mkdir -p /var/log/supervisor
# COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# CMD ["/usr/bin/supervisord"]