FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN mkdir -p /work/Machines/ImportedVM /work/oracle /lab

COPY poc.py /lab/poc.py

WORKDIR /work
CMD ["python3", "/lab/poc.py"]
