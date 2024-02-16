# Who are you?
## Description
*Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn.* 
## Attachments
[http://mercury.picoctf.net:14804/](http://mercury.picoctf.net:14804/)

## Methodology
It turns out that we need to satisfy multiple requirements in the header in order to get the flag. Please refer to the script.
## Solution
This solution is divided into several steps.
 
### Stage 1
First, we use the wget command on the terminal to download the website content. After downloading and using vim to open the file, I found a sentence with content like the     picture below:

![image](https://user-images.githubusercontent.com/54707979/134308149-7be2df14-d72e-49ec-8286-55c28e679d57.png)

Based on that, I googled and found a wget command that allows me to modify the current User-Agent to the user-agent I want. [Explanation of the effect of the header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent), so we have to replace the value user-Agent: picobrowser. 
```
wget -U "picoBrowser" "mercury.picoctf.net:52362"
```
### Stage 2
The web then returns the following content: "I don't trust user visiting from another site.".

![image](https://user-images.githubusercontent.com/54707979/134312729-c194755c-82d2-4338-b9e6-c5e783dbac9e.png)

We need to use more header: "Referer". [Explanation of the effect of the header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer), set the Referer value: http://mercury.picoctf.net:52362.
```
wget -U "picoBrowser" --header "Referer: http://mercury.picoctf.net:52362/" "mercury.picoctf.net:52362"
```
### Stage 3
![image](https://user-images.githubusercontent.com/54707979/134316059-bf6cdf63-2ac3-4c41-bb68-8213ef6fee9b.png)

Next we are suggested that: “this site only worked in 2018”. So we use [header: "Date"](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Date), give the value date: 2018

```
wget -U "picoBrowser" --header "Referer: http://mercury.picoctf.net:52362/" --header "Date: 2018"  "mercury.picoctf.net:52362"
```
### Stage 4
![image](https://user-images.githubusercontent.com/54707979/134316109-4013fe70-6e1d-40ba-a4fa-f89d6bdc837f.png)

Then proceed to the next page and get the instruction again: “I don't trust user who can be tracked”. Therefore we have to use [header: “DNT”](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/DNT) to allow people to go untracked on the web, give the value DNT: true.

```
wget -U "picoBrowser" --header "Referer: http://mercury.picoctf.net:52362/" --header "Date: 2018" --header "DNT: true" "mercury.picoctf.net:52362"
```
### Stage 5
![image](https://user-images.githubusercontent.com/54707979/134318054-e746a52a-4818-4bd2-ac4a-faf38439e4ef.png) 

The web then returns the content: "This website is only for people from Sweden". To get past this step we need to use [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) to determine the original IP address of the client connecting to the web server via an HTTP proxy, give the value for X-Forwarded-For: 192.80.17.1	
```
wget -U "picoBrowser" --header "Referer: http://mercury.picoctf.net:52362/" --header "Date: 2018" --header "DNT: true" --header "X-Forwarded-For: 192.80.17.1"  "mercury.picoctf.net:52362" 
```
### Stage 6
![image](https://user-images.githubusercontent.com/54707979/134320034-8f6a35ce-c767-4ea0-af2f-edb2316c1797.png)


Finally, we come to the page that says: "you are in Sweden but you don't speak Swedish" so we have to use the [header: "Accept-language"](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language), so that the server returns the selected language to the user. give the value for Accept-language: sv-SV
```
wget -U "picoBrowser" --header "Referer: http://mercury.picoctf.net:52362/" --header "Date: 2018" --header "DNT: true" --header "X-Forwarded-For: 192.80.17.1" --header "Accept-Language: sv-SV"  "mercury.picoctf.net:52362" 
```
### Finally
Tada, so I got the flag, now go and submit it to get points.

![image](https://user-images.githubusercontent.com/54707979/134323164-a0183973-6f3e-4c60-8315-eb312c678c8f.png)

## Flag
    picoCTF{http_h34d3rs_v3ry_c0ol_much_w0w_0c0db339}



