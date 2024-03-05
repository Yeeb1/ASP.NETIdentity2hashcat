# ASP.NETIdentity2hashcat

This script convert converts ASP.NET Identity's into a format compatible with Hashcat (`PBKDF2+HMAC-SHA1` and `PBKDF2+HMAC-SHA256`). 

## Usage

```sh
python3 ASP.NETIdentity2hashcat.py 'ALT8uRA+E0bciDkDuRx/VLNOd4MpeEcccPMRc11YtE8z9EtDJHksDChDdmcNFXgCAQ=='
sha1:1000:tPy5ED4TRtyIOQO5HH9Usw==:TneDKXhHHHDzEXNdWLRPM/RLQyR5LAwoQ3ZnDRV4AgE=

```

## Acknowledgments

Special thanks to [@ruidfigueiredo](https://twitter.com/ruidfigueiredo) for creating the original blog post [Anatomy of an ASP.NET Identity PasswordHash](https://www.blinkingcaret.com/2017/11/29/asp-net-identity-passwordhash/) that gives insigths into the ASP.NET Identity inner structure.

---

*The script is for informational and educational purposes only. The author and contributors of this script are not responsible for any misuse or damage caused by this tool.* <!-- meme -->
