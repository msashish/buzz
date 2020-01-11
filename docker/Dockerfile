FROM centos:7

LABEL description="A simple Test Runner"
LABEL maintainer="Ashish"
LABEL version="0.0.1"

ENV PYTHONUNBUFFERED=1
ENV USER=docker
ENV UID=1000
ENV GID=1000

# install centos 7
RUN yum -y update && \
    yum -y install yum-utils && \
    yum -y groupinstall development && \
    yum -y install https://centos7.iuscommunity.org/ius-release.rpm

ENV LD_LIBRARY_PATH=/usr/lib/oracle/18.3/client64/lib/:$LD_LIBRARY_PATH
ENV ORACLE_HOME=/usr/lib/oracle/18.3/client64

# install python and pip
RUN yum -y install python36u python36u-pip && \
    yum clean all

# Create the non-root user using root.
RUN set -Eeuxo pipefail \
    && groupadd --gid ${GID} ${USER} \
    && adduser \
    --gid ${USER} \
    --home-dir /home/${USER} \
    --create-home \
    --uid ${UID} \
    ${USER}

# now, switch to docker user
USER docker

ENV PATH /home/${USER}/.local/bin:${PATH}

COPY requirements.txt .

RUN pip3.6 install --user  -r requirements.txt

# Application will be bind mounted at runtime for this image to be useful
VOLUME [ "/opt/buzz" ]
WORKDIR /opt/buzz

COPY run_tests.sh /run_tests.sh
CMD ["/run_tests.sh"]