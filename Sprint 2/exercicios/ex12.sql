select de.cddep, de.nmdep, de.dtnasc, sum(va.qtd * va.vrunt) as valor_total_vendas from tbdependente de
join tbvendedor ve on de.cdvdd = ve.cdvdd
join tbvendas va on ve.cdvdd = va.cdvdd
where va.status = 'Concluído'
GROUP BY de.cddep, de.nmdep, de.dtnasc
having valor_total_vendas > 0
order by valor_total_vendas
limit 1