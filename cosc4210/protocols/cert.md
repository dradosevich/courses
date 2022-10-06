mkdir -p ./{recipe-api,shared}/tls
openssl req -nodes -new -x509 -keyout recipe-api/tls/basic-private-key.key -out shared/tls/basic-cert.cert