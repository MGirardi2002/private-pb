select va.cdpro, va.nmpro from tbvendas va

where va.status = 'Concluído' and va.dtven between '2014-02-03' and '2018-02-02'
order by va.cdven
limit 1