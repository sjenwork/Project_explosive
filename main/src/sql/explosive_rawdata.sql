IF NOT EXISTS (
    SELECT *
    FROM sys.objects
    WHERE object_id = OBJECT_ID(N'explosive_rawdata')
        AND type in (N'U')
) BEGIN CREATE TABLE [dbo].[explosive_rawdata](
    [DeptID] [nvarchar](10) NOT NULL,
    [DeclareTime] [nvarchar](20) NOT NULL,
    [CASNo] [nvarchar](500) NULL,
    [ChemicalChnName] [nvarchar](500) NULL,
    [ChemicalEngName] [nvarchar](500) NULL,
    [SourceDept] [nvarchar](500) NULL,
    [ResponsibleName] [nvarchar](100) NULL,
    [ResponsibleTel] [nvarchar](50) NULL,
    [ResponsiblePhone] [nvarchar](50) NULL,
    [EmergencyName] [nvarchar](100) NULL,
    [EmergencyTel] [nvarchar](50) NULL,
    [EmergencyPhone] [nvarchar](50) NULL,
    [ComFacBizName] [nvarchar](500) NULL,
    [BusinessAdminNo] [nvarchar](100) NULL,
    [FactoryRegNo] [nvarchar](100) NULL,
    [ComFacBizAddress] [nvarchar](500) NULL,
    [PlaceType] [nvarchar](100) NULL,
    [RegionType] [nvarchar](100) NULL,
    [RegionName] [nvarchar](100) NULL,
    [ComFacBizTWD97X] [nvarchar](20) NULL,
    [ComFacBizTWD97Y] [nvarchar](20) NULL,
    [DeclareDate] [datetime] NULL,
    [ImportQuantity] [nvarchar](20) NULL,
    [ProductionQuantity] [nvarchar](20) NULL,
    [ProductionTWD97X] [nvarchar](20) NULL,
    [ProductionTWD97Y] [nvarchar](20) NULL,
    [UseageQuantity] [nvarchar](20) NULL,
    [UseageTWD97X] [nvarchar](20) NULL,
    [UseageTWD97Y] [nvarchar](20) NULL,
    [StorageQuantity] [nvarchar](20) NULL,
    [StorageTWD97X] [nvarchar](20) NULL,
    [StorageTWD97Y] [nvarchar](20) NULL,
) ON [PRIMARY]
END