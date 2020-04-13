SELECT a.code,
       a.text
FROM
  (SELECT Json_extract_scalar(JSON, '$.id') AS id
   FROM patient
   WHERE Json_extract_scalar(JSON, '$.name[0].given[0]') = %s
     AND Json_extract_scalar(JSON, '$.name[0].family[0]') = %s) p
LEFT JOIN
  (SELECT Split_part(Json_extract_scalar(JSON, '$.patient.reference'), ':', 3) AS id ,
          Json_extract_scalar(JSON, '$.substance.coding[0].code') AS code,
          Json_extract_scalar(JSON, '$.substance.text') AS text
   FROM allergyintolerance) a ON p.id = a.id
