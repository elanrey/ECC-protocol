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
uint8_t randomNum[NUM_ECC_DIGITS];
uint8_t hashNum[NUM_ECC_DIGITS];
uint8_t i;

void setData(uint8_t input[], uint8_t ini, uint8_t fin)
{
	uint8_t num = fin - ini;
	for(i=0; i<num; i++)
		data[i] = input[ini+i];
}

void getRandom()
{
	int file = open("/dev/urandom", O_RDONLY);
	read(file, &randomNum, sizeof(randomNum));
	close(file);
}

void getHash(uint8_t data[], int len)
{
	SHA256_CTX ctx;
	sha256_init(&ctx);
	sha256_update(&ctx, data, len);
	sha256_final(&ctx, hashNum);
}

void makeKeys(uint8_t random[])
{
	ecc_make_key(&publicK, privateK, random);
	for(i=0; i<NUM_ECC_DIGITS; i++)
	{
		publicKx[i] = publicK.x[i];
		publicKy[i] = publicK.y[i];
	}
}

void encryptData(uint8_t privK[])
{
	aes256_context ctx;
	aes256_init(&ctx, privK);
	aes256_encrypt_ecb(&ctx, data);
	aes256_done(&ctx);
}

void decryptData(uint8_t privK[])
{
	aes256_context ctx;
	aes256_init(&ctx, privK);
	aes256_decrypt_ecb(&ctx, data);
	aes256_done(&ctx);
}

uint8_t sign(uint8_t privK[], uint8_t random[], uint8_t hash[])
{
	return ecdsa_sign(ere, ese, privK, random, hash);
}

uint8_t verify(uint8_t pubKx[], uint8_t pubKy[], uint8_t hash[])
{
	for(i=0; i<NUM_ECC_DIGITS; i++)
	{
		publicK.x[i] = pubKx[i];
		publicK.y[i] = pubKy[i];
	}
	return ecdsa_verify(&publicK, hash, ere, ese);
}