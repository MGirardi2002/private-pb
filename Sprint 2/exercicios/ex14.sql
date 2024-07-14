select distinct va.estado, round(avg(va.qtd * va.vrunt),2) as gastomedio from tbvendas va
where va.status = 'Concluído'
group by va.estado
order by gastomedio desc