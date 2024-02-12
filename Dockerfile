FROM ubuntu:jammy

WORKDIR /srv
ADD . .

# Build the image
# ===
RUN apt-get update && apt-get install --no-install-recommends --yes python3-pip
RUN pip3 install -r requirements.txt

# Set revision ID
ARG BUILD_ID
ENV TALISKER_REVISION_ID "${BUILD_ID}"
