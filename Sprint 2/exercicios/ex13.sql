select va.cdpro, va.nmcanalvendas, va.nmpro, sum(va.qtd) as quantidade_vendas from tbvendas va
where va.status = 'Concluído' and (va.nmcanalvendas = 'Ecommerce' or va.nmcanalvendas = 'Matriz')
group by va.cdpro, va.nmcanalvendas, va.nmpro
order by quantidade_vendas
limit 10