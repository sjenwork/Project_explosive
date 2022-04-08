IF NOT EXISTS (
    SELECT *
    FROM sys.objects
    WHERE object_id = OBJECT_ID(N'explosive_records')
        AND type in (N'U')
) BEGIN CREATE TABLE explosive_records (
    id int IDENTITY(1, 1) PRIMARY KEY,
    operation NVARCHAR(8) NOT NULL,
    Time INT NOT NULL,
    ComFacBizName_m NVARCHAR(MAX) NOT NULL,
    ComFacBizName nvarchar(MAX) NOT NULL,
    casno nvarchar(20) NOT NULL,
    name nvarchar(max) NOT NULL,
    deptid NVARCHAR(20) NOT NULL,
    Quantity REAL NOT NULL,
    PlaceType nvarchar(MAX) NOT NULL,
    RegionType nvarchar(MAX) NOT NULL,
    X NVARCHAR(20) NULL,
    Y NVARCHAR(20) NULL,
    lon REAL NULL,
    lat REAL NULL,
    city nvarchar(20) NULL
)
END