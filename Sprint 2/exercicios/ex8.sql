SELECT ve.cdvdd, ve.nmvdd
FROM TBVENDEDOR ve
JOIN TBVENDAS va ON ve.cdvdd = va.cdvdd
WHERE va.status = 'Concluído'
GROUP BY ve.cdvdd, ve.nmvdd
ORDER BY COUNT(va.cdven) DESC
LIMIT 1;