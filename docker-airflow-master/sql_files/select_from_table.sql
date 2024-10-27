SELECT
    Date
    , STORE_LOCATION
    , ROUND(SUM(SP) - SUM(CP)) AS lc_profit
FROM clean_store_transactions
WHERE Date = SUBDate(Date(now()), 1)
GROUP BY STORE_LOCATION
ORDER BY lc_profit DESC
INTO OUTFILE '/store_files_mysql/location_wise_profit.csv'
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n';

SELECT
    Date
    , STORE_ID
    , ROUND(SUM(SP) - SUM(CP)) AS st_profit
FROM clean_store_transactions
WHERE Date = SUBDate(Date(now()), 1)
GROUP BY STORE_ID
ORDER BY st_profit DESC
INTO OUTFILE '/store_files_mysql/store_wise_profit.csv'
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n';
