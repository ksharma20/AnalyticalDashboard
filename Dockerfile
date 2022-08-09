FROM python:bullseye
ENV PYTHONUNBUFFERED 1
RUN useradd -r kabir
WORKDIR /home/kabir/ksharma20/analyticsDashb
COPY requirements.txt /home/kabir/ksharma20/analyticsDashb
RUN pip install -r requirements.txt
USER kabir
COPY . .
