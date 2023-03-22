USE master;
GO

IF DB_ID('OddsOnly1') IS NOT NULL
  DROP DATABASE OddsOnly1;

CREATE DATABASE OddsOnly1;
GO

USE OddsOnly1;


-- Odds --

CREATE TABLE odds (
  [id] int IDENTITY(1, 1),
  [race_name] nVarChar(100),
  [rider_name] nVarChar(100),
  [size] decimal(6,2),
  [datetime] datetime,

  PRIMARY KEY (id)
);