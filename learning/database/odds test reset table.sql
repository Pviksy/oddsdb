DROP TABLE odds;
GO

CREATE TABLE odds (
  [id] int IDENTITY(1, 1),
  [race_name] nVarChar(100),
  [rider_name] nVarChar(100),
  [size] decimal(6,2),
  [datetime] datetime,

  PRIMARY KEY (id)
);
GO


SELECT * FROM odds
ORDER BY race_name, size


