def check_supl(x):
    return f"""if exists 
(select * from supl where suplno='{x}')
     select 'true'
        else 
        select 'false'
"""


def main_query(x):
    big_sql_query = f"""declare @Error NVARCHAR(4000),
                     @error_line int,
                     @body NVARCHAR(4000),
                     @Error2 NVARCHAR(4000),
                     @error_line2 int,
                     @body2 NVARCHAR(4000)




    -- Insert statements for procedure here
       IF EXISTS 
( 
 SELECT  top 1 pl.ITEMNO,i.CHGDATE,i.BUYPR,pl.BUYPR,i.SELPR,pl.SELPR,i.CBUYPRBR,pl.CBUYPRBR,i.CBUYPRNET,pl.CBUYPRNET,pl.SUPLNO,i.SUPLNO
   FROM iprr pl WITH(NOLOCK) 
   JOIN ITEM AS i WITH(NOLOCK) ON pl.ITEMNO = i.ITEMNO and pl.SUPLNO=i.SUPLNO and pl.SUPLNO='{x}'
   left join igrp g on g.IGROUPID=pl.IGRPID
  WHERE (i.BUYPR <> pl.BUYPR OR i.SELPR <> pl.SELPR or i.name<>pl.name or i.skey<>pl.SKEY or i.mcode<>pl.MCODE or isnull(i.DDISCCD,0)<>isnull(pl.DDISCCD,0) or i.IGROUPID<>g.IGROUPID) AND isnull(i.ISSPECPR,0) <> 1

)
BEGIN 

BEGIN TRY
    BEGIN TRANSACTION

INSERT INTO ITPRHIS
(      BASECURR,     BUYPR, BVATCD,       CREATED,      ITEMNO,       SELPR, STRADEPR,     SUPLNO,       SVATCD,       TRADEPR,      VATCD)
(
       SELECT 'UAH',i.BUYPR,i.BVATCD,GETDATE(),i.ITEMNO,i.SELPR,i.STRADEPR,i.SUPLNO,i.SVATCD,i.TRADEPR,i.VATCD 
       FROM ITEM AS i WITH(NOLOCK)
       WHERE i.ITEMNO IN 
       (SELECT pl.itemno FROM iprr pl WITH(NOLOCK) 
       JOIN ITEM AS i WITH(NOLOCK) ON pl.ITEMNO = i.ITEMNO AND pl.SUPLNO=i.SUPLNO and pl.SUPLNO='{x}' 
       WHERE (i.BUYPR <> pl.BUYPR OR i.SELPR <> pl.SELPR or i.name<>pl.name 
       or i.skey<>pl.SKEY or i.mcode<>pl.MCODE or i.DDISCCD<>pl.DDISCCD or i.BRANDCODE<>pl.BRANDCODE) AND isnull(i.ISSPECPR,0) <> 1
       ) and i.SUPLNO='{x}' 
)

--SELECT i.BUYPR,i.SELPR,i.TRADEPR,i.OWNPR,i.CHGDATE,*
--FROM ITEM AS i WITH(NOLOCK)
--WHERE i.ITEMNO = '1084909'

--SELECT i.BUYPR,pl.BUYPR,i.SELPR,pl.SELPR,i.TRADEPR,pl.TRADEPR,i.OWNPR,pl.BUYPR,i.CHGDATE,pl.PRICEDATE, *
UPDATE i
SET --i.CHGDATE=pl.PRICEDATE,
i.BUYPR = pl.BUYPR,
i.SELPR = pl.SELPR,
i.CHGDATE = getdate(),
i.name=pl.name,
i.skey=pl.SKEY,
i.mcode=pl.MCODE,
i.DDISCCD=pl.DDISCCD,
i.prodcd=pl.prodcd,
i.BRANDCODE=pl.BRANDCODE,
i.HAS_EXPIRATION_DATE=pl.HAS_EXPIRATION_DATE,
i.IGROUPID=pl.igrpid

FROM IPRR pl  WITH(NOLOCK)
JOIN ITEM AS i WITH(NOLOCK) ON pl.ITEMNO = i.ITEMNO AND pl.SUPLNO=i.SUPLNO and pl.SUPLNO='{x}'
left join igrp g on g.IGROUPID=pl.IGRPID
  WHERE (i.BUYPR <> pl.BUYPR OR i.SELPR <> pl.SELPR  or i.name<>pl.name or i.skey<>pl.SKEY or i.mcode<>pl.MCODE 
  or i.DDISCPC<>pl.DDISCPC or i.BRANDCODE<>pl.BRANDCODE or isnull(i.DDISCCD,0)<>isnull(pl.DDISCCD,0) or i.IGROUPID<>g.IGROUPID) AND isnull(i.ISSPECPR,0) <> 1


COMMIT TRANSACTION
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK TRAN --RollBack in case of Error
    -- you can Raise ERROR with RAISEERROR() Statement including the details of the exception
SELECT   
      @Error = ERROR_MESSAGE(), 
        @error_line = ERROR_LINE(),
              @body =  @Error+' строка  '+convert(NVARCHAR(4000),@error_line)

EXEC msdb.dbo.sp_send_dbmail
@profile_name = 'AM',
@recipients = 'dmytro.kyrychenko@avtosojuz.ua;d@avtosojuz.ua',
@subject = 'ОШИБКА Обновления существуюих позиций ПРАЙСА {x}',
@body =@body
END CATCH



END






--print GETDATE()
--PRINT 'ITEM insert'
------------------------------------------------------------------------------------------------------------------------------------------------------
-------------ITEM insert
------------------------------------------------------------------------------------------------------------------------------------------------------
IF EXISTS (SELECT top(1) * FROM iprr pl WITH(NOLOCK) LEFT JOIN ITEM AS i WITH(NOLOCK) ON pl.ITEMNO = i.ITEMNO and i.suplno='{x}' WHERE i.ITEMNO IS NULL and pl.SUPLNO='{x}' )
BEGIN 

BEGIN TRY
    BEGIN TRANSACTION

INSERT INTO ITEM
(
       ITEMNO,       SUPLNO,       ADISCCD,      ADISCPC,      BUYPR, BVATCD,       DDISCCD,       DDISCPC,      DISCGRP,      ISSUPREG,     ITYPE, LPRCHD,       LSELLD,       MAKE,  MCODE,       MINCRPC,      NAME,  NOTE,  ODISCCD,
       ODISCPC,      PACKETSZ,     PRODCD,       SACCCD,       SELPR, SKEY,  SVATCD,       TRADEPR,       VATCD, LIncrD,       PackPr,       CBUYPRBR,     CBUYPRNET,    STRADEPR,     OWNPR, CURRCD,       PRILEVEL,     PRICECD,      PCFACTOR,
       KKCOVER,      CSCOVER,      CREATED,      CHGDATE,      USRSID,       LOCKDT,       EANCDTP,       EANCDCP,      SUBIGRPID,    NOTINUSE,     TARIFFNO,     PLENGTH,      PWIDTH,       PHEIGHT,       PWEIGHT,      SpSiZE,       SpSiZEUNIT,
       KCREDITCD,    ORIGCOUNTRY,  STOCKCODE,    IGROUPID,     INSTIME,      INETCD,       PURCHUNIT,       INETREMD,     INOTE, ISLIM, REPLCODE,     REPLDESC,     TRANSPCD,     NOSCHECK,     BBFLAG,       REMNOTE,      CATEG,
       EXTITEMNO,    DSMFLAG,      BONUSGRP,     TCPR,  TCFLAG,       SNTRACK,      DEFSTOCK,       WARRANTYCD,   PARTSTAT,     CSSIGN,       C9RASIGN,     DGSIGN,       TCREBATE,     AMORD,       ISSPECPR,     LISTPR,       DBUYPR,       ALTPACKSZ,
       NOLOYPOINTS,  IS_EXCH_UNIT, HAS_EXCH_UNIT,       ISSEASONAL,   INETSTATUS,   PICPATH,       GPSTATUS,     SKEY2, SKEY3, PACKAGE_EXPORT,      PACKAGE_IMPORT,      VERSIONNO,    UNIQUEPART,       -- _OID -- this column value is auto-generated
       HAS_EXPIRATION_DATE, POINTSFOREXCHANGE,   NOSTOCK,      ISSERIALNOREQ,       ITEMNOFP,       ITEMNOMP,     TYPEMARK,     PRODVERS,     ITEMTYPE,     DENSITY_RATE, NONAMEUPDATE, FEATURECODE,
       BRANDCODE,    WEBSTORES,    WEBSPSIZE
)
(
       SELECT  
       pl.ITEMNO,
       '{x}' as SUPLNO,
       '' AS 'ADISCCD',
       NULL AS 'ADISCPC',
       pl.BUYPR AS 'BUYPR',
       0 AS 'BVATCD',
       pl.DDISCCD,
       NULL AS 'DDISCPC',
       NULL AS 'DISCGRP',
       1 AS 'ISSUPREG',
       '' AS 'ITYPE',
       DATEADD(dd, 0, DATEDIFF(dd, 0, GETDATE())) AS 'LPRCHD',
       NULL AS 'LSELLD',
       '' AS 'MAKE',
       pl.MCODE,
       0.0500 AS 'MINCRPC',
       SUBSTRING(pl.NAME,0,80) AS 'NAME',
       '' AS 'NOTE',
       '' AS 'ODISCCD',
       0.0000 AS 'ODISCPC',
       1 AS 'PACKETSZ',
       '' AS 'PRODCD',
       '' AS 'SACCCD',
       pl.SELPR AS 'SELPR',
       pl.skey as SKEY,
       '1' AS 'SVATCD',
       pl.TRADEPR AS 'TRADEPR',
       '0' AS 'VATCD',
       NULL AS 'LIncrD',
       NULL AS 'PackPr',
       NULL AS 'CBUYPRBR',
       NULL AS 'CBUYPRNET',
       pl.TRADEPR AS 'STRADEPR',
       pl.BUYPR AS 'OWNPR',
       'UAH' AS 'CURRCD',
       0 AS 'PRILEVEL',
       '' AS 'PRICECD',
       0.0000 AS 'PCFACTOR',
       0.0000 AS 'KKCOVER',
       0.0000 AS 'CSCOVER',
       GETDATE() AS 'CREATED',
       getdate() AS 'CHGDATE',
       'BOND' AS 'USRSID',  
       NULL AS 'LOCKDT',
       '' AS 'EANCDTP',
       '' AS 'EANCDCP',
       '' AS 'SUBIGRPID',
       NULL AS 'NOTINUSE',
       '' AS 'TARIFFNO',
       10 AS 'PLENGTH',
       10 AS 'PWIDTH',
       10 AS 'PHEIGHT',
       10 AS 'PWEIGHT',
       1 AS 'SpSiZE',
       'шт' AS 'SpSiZEUNIT',
       1 AS 'KCREDITCD',
       '' AS 'ORIGCOUNTRY',
       '' AS 'STOCKCODE',
       pl.igrpid AS 'IGROUPID',
       NULL AS 'INSTIME',
       NULL AS 'INETC',
       NULL AS 'PURCHUNIT',
       NULL AS 'INETREMD',
       '' AS 'INOTE',
       NULL AS 'ISLIM',
       NULL AS 'REPLCODE',
       NULL AS 'REPLDESC',
       NULL AS 'TRANSPCD',
       NULL AS 'NOSCHECK',
       NULL AS 'BBFLAG',
       NULL AS 'REMNOTE',
       NULL AS 'CATEG',
       '' AS 'EXTITEMNO',
       NULL AS 'DSMFLAG',
       '' AS 'BONUSGRP',
       NULL AS 'TCPR',
       NULL AS 'TCFLAG',
       NULL AS 'SNTRACK',
       NULL AS 'DEFSTOCK',
       NULL AS 'WARRANTYCD',
       '' AS 'PARTSTAT',
       '' AS 'CSSIGN',
       '' AS 'C9RASIGN',
       '' AS 'DGSIGN',
       NULL AS 'TCREBATE',
       NULL AS 'AMORD',
       NULL AS 'ISSPECPR',
       pl.SELPR AS 'LISTPR',
       NULL AS 'DBUYPR',
       NULL AS 'ALTPACKSZ',
       NULL AS 'NOLOYPOINTS',
       NULL AS 'IS_EXCH_UNIT',
       NULL AS 'HAS_EXCH_UNIT',
       NULL AS 'ISSEASONAL',
       NULL AS 'INETSTATUS',
       NULL AS 'PICPATH',
       NULL AS 'GPSTATUS',
       '' AS 'SKEY2',
       '' AS 'SKEY3',
       NULL AS 'PACKAGE_EXPORT',
       NULL AS 'PACKAGE_IMPORT',
       0 AS 'VERSIONNO',
       0 AS 'UNIQUEPART',
       pl.HAS_EXPIRATION_DATE AS 'HAS_EXPIRATION_DATE',
       NULL AS 'POINTSFOREXCHANGE',
      NULL AS 'NOSTOCK',
       NULL AS 'ISSERIALNOREQ',
       NULL AS 'ITEMNOFP',
       NULL AS 'ITEMNOMP',
       NULL AS 'TYPEMARK',
       NULL AS 'PRODVERS',
       '' AS 'ITEMTYPE',
       NULL AS 'DENSITY_RATE',
       NULL AS 'NONAMEUPDATE',
       NULL AS 'FEATURECODE',
       pl.BRANDCODE AS 'BRANDCODE',
       NULL AS 'WEBSTORES',
       NULL AS 'WEBSPSIZE'
       FROM IPRR pl WITH(NOLOCK) 
       LEFT JOIN ITEM AS i WITH(NOLOCK) ON pl.ITEMNO = i.ITEMNO and i.suplno='{x}' WHERE i.ITEMNO IS NULL and pl.SUPLNO='{x}'
       )

COMMIT TRAN 
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK TRAN --RollBack in case of Error
    -- you can Raise ERROR with RAISEERROR() Statement including the details of the exception
SELECT   
        @Error2 = ERROR_MESSAGE(), 
        @error_line2 = ERROR_LINE(),
              @body2 =  @Error2+' строка  '+convert(NVARCHAR(4000),@error_line2)

        EXEC msdb.dbo.sp_send_dbmail
@profile_name = 'AM',
@recipients = 'dmytro.kyrychenko@avtosojuz.ua;d@avtosojuz.ua',
@subject = 'ОШИБКА ИМПОРТА НОВЫХ ПОЗИЦИЙ ПРАЙСА {x}',
@body =@body2

END CATCH
END 


 """
    return big_sql_query


def suplno_config(suplno):
    return f"""update SUDIS01
set DISCCD=rno   
where rno <10
and  SUPLNO = '{suplno}'"""


def delelet_from_iprr(suplno):
    return f"""delete from iprr
where SUPLNO = '{suplno}'"""


def delelet_from_iprh(suplno):
    return f"""delete from iprh
where SUPLNO = '{suplno}'"""
