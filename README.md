# Format-preserving, Feistel-based cryptography command-line interface 

“Format Preserving Encryption is a method which allows the basic formatting of a message to stay in a similar format, and where the value itself is encrypted. It can be used to hide credit card details.”  — Bill Buchanan

## Examples

```bash
$ echo 8005551212 | python ffx.py -e mypassword 0123456789
9441166894
$ echo 9441166894 | python ffx.py -d mypassword 0123456789
8005551212
$ echo '+😊qwerty🍦*' | python ffx.py -e secret-squirrel '*+😊🍦abcdefghijklmnopqrstuvwxyz'
rgmty🍦udpv
$ echo 'rgmty🍦udpv' | python ffx.py -d secret-squirrel '*+😊🍦abcdefghijklmnopqrstuvwxyz'
+😊qwerty🍦*
$ 
```

## References

- [FFX schemes for Format-Preserving Encryption](https://medium.com/asecuritysite-when-bob-met-alice/ffx-schemes-for-format-preserving-encryption-a2a7aa4f1377), Bill Buchanan
- [pyffx is a pure Python implementation of Format-preserving, Feistel-based encryption (FFX)](https://github.com/emulbreh/pyffx), Johannes Dollinger
