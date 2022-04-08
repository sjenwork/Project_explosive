IF NOT EXISTS (
    SELECT *
    FROM sys.objects
    WHERE object_id = OBJECT_ID(N'explosive_chemilist')
        AND type in (N'U')
) BEGIN CREATE TABLE explosive_chemilist (
    id int IDENTITY(1, 1) PRIMARY KEY,
    casno NVARCHAR(12) NOT NULL,
    chnname NVARCHAR(MAX) NOT NULL,
    label NVARCHAR(MAX) NOT NULL,
    engname NVARCHAR(MAX) NULL,
    matchno INT NULL
)
END