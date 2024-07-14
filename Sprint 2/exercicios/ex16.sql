select va.estado, va.nmpro, round(avg(va.qtd),4) as quantidade_media from tbvendas va
where va.status = 'Concluído'
group by va.estado, va.nmpro
