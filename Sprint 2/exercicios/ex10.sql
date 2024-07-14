SELECT 
    ve.nmvdd AS vendedor, 
    SUM(va.qtd * va.vrunt) AS valor_total_vendas, 
    ROUND(SUM(va.qtd * va.vrunt * ve.perccomissao)/100, 2) AS comissao
FROM 
    TBVENDEDOR ve
JOIN 
    TBVENDAS va ON ve.cdvdd = va.cdvdd
WHERE 
    va.status = 'Concluído'
GROUP BY 
    ve.cdvdd, ve.nmvdd, ve.perccomissao
ORDER BY 
    comissao DESC