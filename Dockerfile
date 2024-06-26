FROM python:3.10-alpine as base
FROM base as builder

# Install requirements
COPY requirements.txt /requirements.txt
RUN pip install --user -r /requirements.txt

FROM base

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local /root/.local
COPY src /app
WORKDIR /app

# update PATH environment variable
ENV PATH=/home/app/.local/bin:$PATH

CMD ["python", "main.py"]