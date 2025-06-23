---
title: "DHCP Tutorial: Understanding and Configuring DHCP"
date: 2024-04-14
draft: false
showInHome: false
---


## Introduction
Dynamic Host Configuration Protocol (DHCP) is a network management protocol that automates the assignment of IP addresses and other network configuration parameters to devices, allowing them to communicate on an IP network.

In this tutorial, we'll cover:
- What DHCP is
- Key concepts
- A hands-on example
- Best practices

---

## 1. What is DHCP?
DHCP (Dynamic Host Configuration Protocol) allows automatic assignment of IP addresses to devices.  
**Benefits:**
- Reduces manual IP configuration
- Enables IP address reusability
- Simplifies network administration

---

## 2. Key Terminology
- **DHCP Server:** Provides IP addresses.
- **DHCP Client:** Requests IP addresses.
- **Scope:** Range of IP addresses available for assignment.
- **Lease Time:** Time period a device can use an IP address.
- **Options:** Additional information like DNS and Default Gateway.

---

## 3. DHCP Process
Here is the basic process:

1. Client sends **Discover**
2. Server replies with **Offer**
3. Client sends **Request**
4. Server sends **Acknowledgment (Ack)**

## 4. Setting Up a DHCP Server on linux (Example just for test and learn )
🟩STEP 1: Install DHCP Server

Open a terminal on your Linux laptop and run:
sudo apt update
sudo apt install isc-dhcp-server


🟩 STEP 2: Identify Your Network Interface

Check your available interfaces:

ip addr
Look for the interface connected to your network, e.g., eth0 or wlan0.
for example my inf0 is :
IP: 10.187.54.102/8
Subnet Mask: 255.0.0.0 (Class A)
Broadcast: 10.255.255.255

This means:

    I am connected to a Wi‑Fi network (wlo1), 10.187.54.102/8

    DHCP server should operate within this range, e.g., 10.187.54.*.
    
    
    
🟩 STEP 3: Edit the DHCP Server Config

Edit your DHCP settings:

sudo vim /etc/dhcp/dhcpd.conf

add this subnet: 
subnet 10.187.0.0 netmask 255.0.0.0 {
    range 10.187.54.200 10.187.54.250;
    option routers 10.187.54.102;
    option subnet-mask 255.0.0.0;
    option broadcast-address 10.255.255.255;
    option domain-name-servers 8.8.8.8, 1.1.1.1;
    default-lease-time 600;
    max-lease-time 7200;
}
then 

Edit:

sudo vim /etc/default/isc-dhcp-server

Set:

INTERFACESv4="wlo1"


🟩 STEP 4: Restart and Test

Restart:

sudo systemctl restart isc-dhcp-server
sudo systemctl status isc-dhcp-server


 NEXT STEP: Test the DHCP Service

Try connecting another device (or a virtual machine) to the same Wi‑Fi network:

    The device should obtain an IP in the range you defined (10.187.54.200–250).

Watch the leases:

sudo tail -f /var/lib/dhcp/dhcpd.leases

Watch traffic:

sudo tail -f /var/log/syslog

