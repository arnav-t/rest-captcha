# rest-captcha
REST API for solving ERP captchas.
## Usage
The REST API is currently hosted at [https://erp-captcha.herokuapp.com/](https://erp-captcha.herokuapp.com/)
### Using cURL
```cURL
curl -F 'image=@[path to captcha image]' http://erp-captcha.herokuapp.com/
```
```cURL
curl -F 'image=@/home/arnav/Documents/python/py-dep-rank/captcha.jpeg' http://erp-captcha.herokuapp.com/
7LXKCT
```
