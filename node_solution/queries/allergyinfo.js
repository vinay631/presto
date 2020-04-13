module.exports = (firstName, familyName) => `SELECT a.code, a.text FROM
(
    SELECT json_extract_scalar(json, '$.id') as id
        FROM patient 
        WHERE json_extract_scalar(json,'$.name[0].given[0]')  = '${firstName}'
        AND json_extract_scalar(json,'$.name[0].family[0]') = '${familyName}'
) p
JOIN
(
    SELECT split_part(json_extract_scalar(json, '$.patient.reference'), ':', 3) as id,
        json_extract_scalar(json, '$.substance.coding[0].code') as code,
        json_extract_scalar(json, '$.substance.text') as text
        FROM allergyintolerance
) a 
ON a.id=p.id`