FROM python:bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN useradd -r kabir
WORKDIR /home/kabir/ksharma20/analyticsDashb
COPY requirements.txt /home/kabir/ksharma20/analyticsDashb
RUN pip install -r requirements.txt
USER kabir
COPY . .
