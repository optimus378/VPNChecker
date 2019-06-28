$Connection16 = "Your AZure VNG Connection"
$RG1 = 'Your Resource Group That the VNG Connection is located.' 
Remove-AzVirtualNetworkGatewayConnection -Name $Connection16 -ResourceGroupName $RG1 -Force