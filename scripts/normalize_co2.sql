USE SCHEMA ANALYTICS_CO2;
CREATE OR REPLACE FUNCTION ANALYTICS_CO2.NORMALIZE_CO2_UDF(
    CO2_PPM NUMBER(35,4)
)
RETURNS NUMBER(35,4)
AS
$$
    (CO2_PPM - (SELECT MIN(CO2_PPM) FROM RAW_CO2.CO2_DATA)) /
    ((SELECT MAX(CO2_PPM) FROM RAW_CO2.CO2_DATA) - (SELECT MIN(CO2_PPM) FROM RAW_CO2.CO2_DATA))
$$;