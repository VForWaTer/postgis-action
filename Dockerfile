# TODO: replace with Vforwater-test-suite image
FROM: postgis/postgis:11-2.5-alpine

# copy entrypoint
COPY entrypoint.sh /entrypoint.sh

# run
ENTRYPOINT ["/entrypoint.sh"]
