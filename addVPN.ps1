## This script is very specific. Use this if you're having trouble connecting your older IOS version Cisco ASA to an AZURE VNG. Site to Site VPN  

$RG1 = 'Your Resource Group' 
$GWName1 = 'Your Azure VNG NAME' 
$LNGName6 = 'Your Local Network Gateway Nme' 
$Connection16 = "Yoour Azure VNG Connection Name" 
$Location1 = "Central US" 
$PSK = 'The Preshared KEY' 
 
$ipsecpolicy6 = New-azIpsecPolicy -IkeEncryption AES256 -IkeIntegrity SHA384 -DhGroup DHGroup2 -IpsecEncryption AES256 -IpsecIntegrity SHA1 -PfsGroup None -SALifeTimeSeconds 28800 -SADataSizeKilobytes 4608000
$vnet1gw = Get-AzVirtualNetworkGateway -Name $GWName1  -ResourceGroupName $RG1 
$lng6 = Get-AzLocalNetworkGateway  -Name $LNGName6 -ResourceGroupName $RG1 
New-AzVirtualNetworkGatewayConnection -Name $Connection16 -ResourceGroupName $RG1 -VirtualNetworkGateway1 $vnet1gw -LocalNetworkGateway2 $lng6 -Location $Location1 -ConnectionType IPsec -UsePolicyBasedTrafficSelectors $True -IpsecPolicies $ipsecpolicy6 -SharedKey $PSK 