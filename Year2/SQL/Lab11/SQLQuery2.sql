USE AdventureWorks2019;

-- Drop the existing stored procedure if it exists
IF OBJECT_ID('dbo.ProcessJournalRecords', 'P') IS NOT NULL
    DROP PROCEDURE dbo.ProcessJournalRecords;
GO

-- Recreate the stored procedure
CREATE PROCEDURE ProcessJournalRecords
AS
BEGIN
    -- Declare all variables
    DECLARE @AC_NUM VARCHAR(MAX)
    DECLARE @PD_NUM VARCHAR(MAX)
    DECLARE @AC_ID VARCHAR(MAX)
    DECLARE @PD_ID VARCHAR(MAX)
    DECLARE @SRC_STM_ID VARCHAR(MAX)
    DECLARE @EXCP_CODE_ID VARCHAR(MAX)
    DECLARE @TXN_SRC_KEY VARCHAR(MAX)
    DECLARE @CRT_DTM VARCHAR(MAX)
    DECLARE @BKG_DT DATE
    DECLARE @BUS_DY DATE
    DECLARE @SHARES FLOAT
    DECLARE @CCY VARCHAR(MAX)
    DECLARE @AMOUNT FLOAT
    DECLARE @RATE FLOAT
    DECLARE @SRC_CODE VARCHAR(MAX)
    DECLARE @ACTION_F VARCHAR(1)

    WHILE 1 = 1
    BEGIN
        -- If there are delete operations, remove them from TXN and J$SRC_TXN
        DELETE FROM TXN WHERE TXN_SRC_KEY IN (SELECT TXN_SRC_KEY FROM J$SRC_TXN WHERE ACTION_F='D')
        DELETE FROM J$SRC_TXN WHERE ACTION_F='D'

        -- Process data in a while loop where CONSUME_F = 0
        WHILE EXISTS (SELECT 0 FROM J$SRC_TXN WHERE CONSUME_F = 0 AND ACTION_F != 'D')
        BEGIN
            -- Set variables to NULL
            SET @AC_NUM = NULL
            SET @PD_NUM = NULL
            SET @SHARES = NULL
            SET @CCY = NULL
            SET @BKG_DT = NULL
            SET @BUS_DY = NULL
            SET @CRT_DTM = NULL
			SET @RATE = NULL

            -- Select necessary values
            SELECT TOP 1 
                @TXN_SRC_KEY = s.TXN_SRC_KEY,
                @AC_NUM = AC_NUM,
                @PD_NUM = PD_NUM,
                @SHARES = SHARES,
                @CCY = CCY,
                @BKG_DT = BKG_DT,
                @BUS_DY = BUS_DY,
                @ACTION_F = ACTION_F,
                @CRT_DTM = j.CRT_DTM,
                @SRC_CODE = SRC_CODE
            FROM SRC_TXN AS s 
            INNER JOIN J$SRC_TXN AS j ON s.TXN_SRC_KEY = j.TXN_SRC_KEY
            WHERE j.CONSUME_F = 0;

            -- Error handling
            PRINT @TXN_SRC_KEY
            IF NOT EXISTS (SELECT 0 FROM AC_LKP WHERE AC_NUM = @AC_NUM)
            BEGIN
                PRINT '1. AC_NUM DOES NOT EXISTS' + @AC_NUM
                -- Find the exception ID
                SELECT @EXCP_CODE_ID = EXCP_CODE_ID FROM EXCP_CODE
                WHERE EXCP_CODE_NM = 'ACEXCP';
                PRINT @EXCP_CODE_ID
                INSERT INTO TXN_EXCP (TXN_SRC_KEY, EXCP_CODE_ID)
                VALUES (@TXN_SRC_KEY, @EXCP_CODE_ID);
            END

            IF NOT EXISTS (SELECT 0 FROM PD_LKP WHERE PD_NUM = @PD_NUM)
            BEGIN
                PRINT '1. PD_NUM DOES NOT EXISTS' + @PD_NUM
                -- Find the exception ID
                SELECT @EXCP_CODE_ID = EXCP_CODE_ID FROM EXCP_CODE
                WHERE EXCP_CODE_NM = 'PDEXCP';
                INSERT INTO TXN_EXCP (TXN_SRC_KEY, EXCP_CODE_ID)
                VALUES (@TXN_SRC_KEY, @EXCP_CODE_ID);
            END

            -- Check if AC_ID in AC_LKP with source SRC_TXN is active (ACTV_F = 'Y')
            -- Check if PD_ID in PD_LKP with source SRC_TXN, if the transaction was made on a valid date
            --   i.e., PD_LKP.EFF_DT < SRC_TXN.BUS_DY < PD_LKP.END_DT
            -- Check if transaction type is correct in SRC_STM_LKP
            --   i.e., SRC_STM_CODE = SRC_CODE
            SELECT @AC_ID = AC_ID FROM AC_LKP WHERE AC_NUM = @AC_NUM AND ACTV_F = 'Y';
            SELECT @PD_ID = PD_ID FROM PD_LKP WHERE PD_NUM = @PD_NUM AND (@BUS_DY BETWEEN EFF_DT AND END_DATE);
            SELECT @SRC_STM_ID = SRC_STM_ID FROM SRC_STM_LKP WHERE SRC_STM_CODE = @SRC_CODE;

            -- Error handling
            IF @AC_ID IS NULL OR @PD_ID IS NULL OR @SRC_STM_ID IS NULL
            BEGIN
                SELECT @EXCP_CODE_ID = EXCP_CODE_ID FROM EXCP_CODE
                WHERE EXCP_CODE_NM = 'GENEXCP'
                INSERT INTO TXN_EXCP (TXN_SRC_KEY, EXCP_CODE_ID)
                VALUES (@TXN_SRC_KEY, @EXCP_CODE_ID);
            END
            ELSE
            BEGIN
                -- If everything is valid, calculate the amount
                IF @CCY = 'USD'
                BEGIN
                    SET @RATE = 1;
                END
                ELSE
                BEGIN
                    SELECT @RATE = EXCH_RATE.RATE FROM EXCH_RATE
                    WHERE EXCH_RATE.CCY_CODE = @CCY
                    AND @BUS_DY BETWEEN EXCH_RATE.EFF_DT AND EXCH_RATE.END_DATE;
					PRINT '====EXECUTED===='
					PRINT @RATE
					PRINT @CCY
					PRINT @BUS_DY
					PRINT '==========='
                END
				IF @RATE IS NULL
				BEGIN
					SET @RATE = 1;
				END

                -- Calculate AMOUNT using SHARES and RATE
                SET @AMOUNT = @SHARES / @RATE;

                -- Check if @BKG_DT is null, and if it is, assign @BUS_DY
                IF @BKG_DT IS NULL
                BEGIN
                    SET @BKG_DT = @BUS_DY;
                END

                -- Check the type of operation, if it is insert, perform insert, if update, perform update
                PRINT @TXN_SRC_KEY
                PRINT @CRT_DTM
                IF @ACTION_F = 'I'
                BEGIN
                    INSERT INTO TXN (TXN_SRC_KEY, AC_ID, PD_ID, SRC_STM_ID, QTY, CCY, AMOUNT, TD, BKG_DT)
                    VALUES (@TXN_SRC_KEY, @AC_ID, @PD_ID, @SRC_STM_ID, @SHARES, @CCY, @SHARES/@RATE, @BUS_DY, @BKG_DT);
                END
                ELSE IF @ACTION_F = 'U'
                BEGIN
                    UPDATE TXN SET AC_ID = @AC_ID, PD_ID = @PD_ID, SRC_STM_ID = @SRC_STM_ID, 
                    QTY = @SHARES, CCY = @CCY, AMOUNT = @SHARES / @RATE, TD = @BUS_DY, BKG_DT = @BKG_DT 
                    WHERE TXN_SRC_KEY = @TXN_SRC_KEY;
                END
            END
			UPDATE J$SRC_TXN SET CONSUME_F = 1 WHERE CONSUME_F = 0 AND TXN_SRC_KEY = @TXN_SRC_KEY AND CRT_DTM = @CRT_DTM;
                PRINT 'ESTE';
        END

        -- After processing all transactions, delete those with consume_F = 1
        DELETE FROM J$SRC_TXN WHERE CONSUME_F = 1;

        WAITFOR DELAY '00:00:15';
    END;
END;
GO
