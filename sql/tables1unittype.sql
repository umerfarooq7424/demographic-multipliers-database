SELECT st,unit_type, sum(units_unwght) as units_unwght,sum(units_wght) as units_wght
FROM demographics.`database sel_alltyp`
GROUP BY st,unit_type ;