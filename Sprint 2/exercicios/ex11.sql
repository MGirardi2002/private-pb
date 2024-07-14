SELECT va.cdcli, va.nmcli, ROUND(SUM(va.qtd * va.vrunt)) AS gasto
FROM TBVENDAS va

WHERE va.status = 'Concluído'
GROUP BY va.cdcli, va.nmcli
ORDER BY gasto DESC
LIMIT 1