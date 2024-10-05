-- Drop the existing trigger if it exists
IF OBJECT_ID('dbo.trg_SrcTxn', 'TR') IS NOT NULL
    DROP TRIGGER dbo.trg_SrcTxn;
GO
--
-- Recreate the trigger
CREATE TRIGGER trg_SrcTxn
ON SRC_TXN
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
	Declare @SRC_KEY VARCHAR(MAX)
    IF EXISTS (SELECT 0 FROM deleted)
	Begin
		IF EXISTS (SELECT 0 FROM inserted)
		Begin
			Select @SRC_KEY = TXN_SRC_KEY From inserted
			Insert into J$SRC_TXN (TXN_SRC_KEY, CONSUME_F, ACTION_F)
			Values (@SRC_KEY, 0, 'U')
		End
		Else
		Begin
			Select @SRC_KEY = TXN_SRC_KEY From deleted
			Insert into J$SRC_TXN (TXN_SRC_KEY, CONSUME_F, ACTION_F)
			Values (@SRC_KEY, 0, 'D')
		End
	End
	Else
	Begin
		Select @SRC_KEY = TXN_SRC_KEY From inserted
		Insert into J$SRC_TXN (TXN_SRC_KEY, CONSUME_F, ACTION_F)
		Values (@SRC_KEY, 0, 'I')
	End
END;
GO
