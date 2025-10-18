# Simple URLShortener
A Simple URLShortener built using Django that encodes long URLs into compact, shareable links using Base62 encoding.

## Why Base62?
Base62 encoder allows us to use the combination of characters and numbers which contains A-Z, a-z, 0–9 total( 26 + 26 + 10 = 62).

So for 7 characters short URL, we can serve :
```bash
62^7 ~= 3500 billion URLs
```
which is quite enough in comparison to base10 (base10 only contains numbers 0-9 so you will get only 10M combinations).

This makes Base62 ideal for scalable short-link systems like Bitly or TinyURL.

## BASE62 ENCODING LOGIC
```bash
def encode_base62(num: int) -> str:
    """Convert a positive integer to a Base62 string."""
    if num == 0:
        return ALPHABET[0]
    base62 = ""
    while num > 0:
        num, rem = divmod(num, 62)
        base62 = ALPHABET[rem] + base62
    return base62
```

So for each long url typed in our template,its first saved in our database after which an auto genearate ID is created for it
Once saved and id generated ,the id is encoded
 
## HOW IT WORKS : 
1.Type url : [https://www.youtube.com/watch?v=P2wLb1njn4I&list=RDMMP2wLb1njn4I&start_radio=1&pp=0gcJCacEOCosWNin ] in our template and click submit
2.The URL is saved in DB afterwhich its automatically assigned an auto-generated numeric ID i.e say 125.
3.The numeric ID then gets encoded into a Base62 short code i.e. abc123
4.The short code then gets appended to your custom domain to form  i.e. https://yourapp.com/abc123

## 🧩 FUTURE ENHANCEMENTS
   - Add analytics dashboard (clicks by day, referrers of shortened urls)
   - Add QR code generation for short URLs
   - Enhance encoding logic ; switch to more secure, collision free IDs like hashids
   - Add user accounts and authenctication to ensure only registered users manage, delete and view statistics of their own shortened URLs
