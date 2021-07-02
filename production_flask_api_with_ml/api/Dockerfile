FROM python:3.8


RUN python -m pip install --upgrade pip


ADD requirements.txt /tmp/requirements.txt
RUN cd /tmp && pip install --no-cache-dir -r requirements.txt --src /usr/local/src && \
    apt-get purge -y --auto-remove build-essential git && \
    apt-get clean && \
    rm -rf \
        /usr/share/doc/* \
        /usr/share/locale/* \
        /usr/share/man/* \
        /var/tmp/*

COPY  . .