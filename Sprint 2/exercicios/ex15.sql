select va.cdven from tbvendas va
where va.deletado != 0
group by va.cdven
