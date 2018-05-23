FROM vistalab/mcr-v90

RUN apt-get update && apt-get install -y python-dev python-pip

ADD ./ /site
RUN cd /site && python setup.py install

RUN mv /site/run.py /run.py

CMD ["python", "run.py"]
