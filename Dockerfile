# TODO: replace with Vforwater-test-suite image
FROM alpine:3.10

# copy entrypoint
COPY entrypoint.sh /entrypoint.sh

# run
ENTRYPOINT ["/entrypoint.sh"]
