# VPNChecker
Crude Script that check the status of a vpn with a ping and notifies MS Teams Channel if it goes down. 

This script was created because we had an older Cisco ASA with an older version of IOS that didn't play nice with Azure's Virtual Network gateway. This was a band-aid so that we could tranfer data over VPN to Azure and then Decommision the ASA.  

It works by sending a ping on the inside network to the ASA. If the VPN goes down, It runs a powershell script that removes the Azure VNG Connection and re-adds it. It also sends message to an msteams channel. 

