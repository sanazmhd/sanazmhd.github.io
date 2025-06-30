---
title: "Setting Up an FTP Server: What, Why, and How?(Linux/Windows)"
date: 2024-04-14
draft: false
showInHome: false
---


🤔 What is an FTP Server?

An FTP (File Transfer Protocol) server is a service that allows you to upload and download files. You might think:

    “Isn’t this a basic thing?”

Yes, it seems simple, but it has powerful features:

    You can upload large numbers of files efficiently.

    Multiple users can connect simultaneously and transfer files.

    Both uploading and downloading are supported.

---
Where is FTP Used?

FTP servers are widely used in:

    Download servers that need to handle many files.

    Backup services to store backup files securely.

    Scanners that automatically upload scanned documents to a central location.

    Freelancers who need a space to upload their project files for clients or teammates.

So yes – it is a very practical tool.

---

💻 Setting Up FTP Server on Windows



For Windows, we use FileZilla Server. Let’s go step by step:

    Download and install FileZilla Server on your Windows machine.

    Remember: FileZilla has a client version too, but here we focus on the server. You can use any client (FileZilla Client, WinSCP, or even Windows File Explorer) to connect later.
![Download-File-Zilla](/images/Download-File-Zilla.png)
    After installation:

        Open FileZilla Server.

        Go to Server settings-configure-administartion and set an admin password.
        ![Setting Up FTP Server on Windows](/images/configure.png)
         ![Setting Up FTP Server on Windows](/images/administartion.png)
        

        In Listener settings, set the IP to 0.0.0.0. This allows connections from all IPv4 and IPv6 addresses.
         ![Setting Up FTP Server on Windows](/images/port.png)

    Create a User:
![users](/images/user.png)

        Go to the Users section.

        Click Add, enter a username.

        Set a home directory path for this user.
          ![Setting Up FTP Server-path](/images/path.png)

        Enable authentication and set a password.

        Ensure both Read and Write permissions are enabled so users can upload and download.
---

Testing the FTP Server

    Use any FTP client. I use WinSCP.
![Testing the FTP Server](/images/winscp.png)
![Testing the FTP Server-host](/images/winscphost.png)


    Create a New Session:

        Protocol: FTP

        Port: 21

        Host: Your server IP

        Username and Password as set above

    Click Save and connect.

 
🐧 Setting Up a Simple FTP Server on Linux

Here is a step-by-step guide to set up an FTP server on Linux (Ubuntu):
✅ 1. Update packages

sudo apt update

✅ 2. Install vsftpd (Very Secure FTP Daemon)

sudo apt install vsftpd

✅ 3. Start and enable the vsftpd service

sudo systemctl start vsftpd
sudo systemctl enable vsftpd

✅ 4. Configure vsftpd

Edit the configuration file:

sudo nano /etc/vsftpd.conf

Uncomment or add these lines to allow uploads and local user login:

write_enable=YES
local_enable=YES

✅ 5. Restart the vsftpd service

sudo systemctl restart vsftpd

✅ 6. Test the FTP server

You can test your FTP server using any FTP client like FileZilla or WinSCP with the following details:

    Host: your server IP

    Username: your Linux username

    Password: your Linux user password

    Port: 21

✅ 7. Test using command line

ftp localhost

Then in your shell:

echo "This is my first FTP test file" > ftp_test.txt

Inside the ftp> prompt, upload the file:

put ftp_test.txt

Exit FTP:

bye

Download it back to test download functionality:

ftp localhost
get ftp_test.txt downloaded_test.txt
bye

Finally, verify the file content:

cat downloaded_test.txt

✔️ You should see:

This is my first FTP test file

📝 Now your FTP server is working successfully on Linux.

Let me know if you want a secure FTP configuration guide (SSL/TLS) or automated user creation scripts for your DevOps and Linux notes this week.





