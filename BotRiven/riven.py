import sys
import urllib3
import  certifi

if __name__ == "__main__":
    data = {}
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    h = {'Authorization' : 'Bot MzEzNzU4MTgzNzQ5NDUxNzc2.DA3hwg.kCaoga3G5AHTwN4NN4y9M1zjg6Q'};
    resp = http.request('GET', 'http://discordapp.com/api/users/@me', headers=h)
    print(resp.data)
