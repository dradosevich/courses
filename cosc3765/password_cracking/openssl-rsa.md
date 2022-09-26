
## Generate the private key
`openssl genrsa -out key.pem 2048`

## Generate the public key
`openssl rsa -in key.pem -out key.pub -pubout`

## Encrypt the file
`openssl pkeyutl -in secret.txt -out secret.enc -pubin -inkey key.pub -encrypt`

## Decrypt the file
`openssl pkeyutl -in secret.enc -out secret.out -inkey key.pem -decrypt`

## Cat the file to standard out
`cat secret.out`