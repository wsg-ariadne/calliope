FROM python:3.8-slim AS dependencies

# Install pip requirements under virtualenv
RUN pip install --upgrade pip wheel
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
COPY requirements.txt .
RUN pip install -r requirements.txt


FROM python:3.8-slim AS main
COPY --from=dependencies /opt/venv /opt/venv
LABEL maintainer="Jared Dantis <jareddantis@gmail.com>"

# Copy bot files and run app
COPY . /opt/app
WORKDIR /opt/app
ENV PATH="/opt/venv/bin:${PATH}"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
CMD ["python3", "api.py"]
