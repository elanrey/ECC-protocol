#include "ecc.c"
#include "aes256.c"
#include "sha256.c"
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

struct EccPoint publicK;
uint8_t data[] = {};
uint8_t ere[NUM_ECC_DIGITS];
uint8_t ese[NUM_ECC_DIGITS];
uint8_t publicKx[NUM_ECC_DIGITS];
uint8_t publicKy[NUM_ECC_DIGITS];
uint8_t privateK[NUM_ECC_DIGITS];
uint8_t randomN[NUM_ECC_DIGITS];
uint8_t hashN[NUM_ECC_DIGITS];
uint8_t i;

void setData(uint8_t input[], int len)
{
	for(i=0; i<len; i++)
	{
		data[i] = input[i];
	}
}

void getRandom()
{
	int file = open("/dev/urandom", O_RDONLY);
	read(file, &randomN, sizeof(randomN));
	close(file);
}

void getHash(int len)
{
	SHA256_CTX ctx;
	sha256_init(&ctx);
	sha256_update(&ctx, data, len);
	sha256_final(&ctx, hashN);
}

void makeKeys()
{
	ecc_make_key(&publicK, privateK, randomN);
	for(i=0; i<NUM_ECC_DIGITS; i++)
	{
		publicKx[i] = publicK.x[i];
		publicKy[i] = publicK.y[i];
	}	
}

void encrypt()
{
	aes256_context ctx;
	aes256_init(&ctx, privateK);
	aes256_encrypt_ecb(&ctx, data);
	aes256_done(&ctx);
}

void decrypt()
{
	aes256_context ctx;
	aes256_init(&ctx, privateK);
	aes256_decrypt_ecb(&ctx, data);
	aes256_done(&ctx);
}

uint8_t sign()
{
	return ecdsa_sign(ere, ese, privateK, randomN, hashN);
}

uint8_t verify()
{
	return ecdsa_verify(&publicK, hashN, ere, ese);
}