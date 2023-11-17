import pyotp
import time

totp = pyotp.TOTP("base32secret3232")
print(totp.now())

print(totp.verify("581861"))
print(totp.at(1401))
print(totp.verify("271305",1402))
htop = pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name='alice@google.com', issuer_name='Secure App')
print(htop)

totp2 = pyotp.TOTP("JBSWY3DPEHPK3PXP")
print("Current OTP:", totp2.now())