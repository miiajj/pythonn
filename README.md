# Exploit code v Tool

> Repo này tạo ra để lưu exploit python code. Hiện tại là như thế hoặc ...không.
## Update thì viết vào đây

### November 25, 2022
- Push ATutor exploit code
- Push XOR - bypass waf

### February 17, 2023
- Create directory **tools**
- Push get IPs from domains (kiểu vậy :>)

## Một số exploit

### ATutor 2.2.1
1. Lấy password hashed bằng  SQL Injection GET method tại path `/ATutor/mods/_standard/social/index_public.php?search_friends=`*`payload`*
2. Thêm và sửa login request params:
    - *token*=*<random_string>*
    - *form_password_hidden=SHA1(<password_hashed>\<token>)*

### XOR bypass waf

- WAF - Web Application Firewall có nhiệm vụ filter các ký tự được cho là nguy hiểm đối với ngữ cảnh hiện tại của hệ thống.
- XOR là kỹ thuật để tạo ra các ký tự bị filter bằng cách xor (^) những ký tự không bị filter  với nhau.
```
Ví dụ:
A = 65 = 1000001 
S = 83 = 1010011
B = 66 = 1000010

A        1000001
S        1010011
B        1000010 
---------------- 
result   1010000 = 80 = P 

A^S^B = P
```

## Tool

### getIpsFromDomains

- `python getIpsFromDomains.py <path_to_domains_file> <output_file>`