# Who are you?
## Description
*Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn.* 
## Attachments
[http://mercury.picoctf.net:14804/](http://mercury.picoctf.net:14804/)

## Methodology
    It turns out that we need to satisfy multiple requirements in the header in order to get the flag. Please refer to the script.
## Solution
    This solution is divided into several steps.

### Stage1
    First, we use the wget command on the terminal to download the website content. After downloading and using vim to open the file, I found a sentence with content like the picture below:

![image](https://media.discordapp.net/attachments/871393677304553473/890139553577451530/unknown.png)

Based on that, I googled and found a wget command that allows me to modify the current User-Agent to the user-agent I want. [Explanation of the effect of the header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent), so we have to replace the value user-Agent: picobrowser.  



