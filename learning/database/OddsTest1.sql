USE master;
GO

IF DB_ID('OddsTest1') IS NOT NULL
  DROP DATABASE OddsTest1;

CREATE DATABASE OddsTest1;
GO

USE OddsTest1;

-- Team --

CREATE TABLE org (
  [id] int IDENTITY(1, 1),

  PRIMARY KEY ([id])
);

CREATE TABLE team (
  [id] int, -- team pk should always be the same as on firstcycling
  [org_id] int     
	FOREIGN KEY REFERENCES org([id])
    ON DELETE CASCADE,
  [name] nvarchar(50),
  [country] nvarchar(50),
  [category] nvarchar(8),
  [year] int

  PRIMARY KEY ([id])
);


-- Rider --

CREATE TABLE rider (
  [id] int,  -- rider pk should always be the same as on firstcycling
  [team_id] int     
	FOREIGN KEY REFERENCES team([id])
    ON DELETE CASCADE,
  [firstname] nvarchar(50),
  [lastname] nvarchar(50),
  [country] nvarchar(50),
  [date_of_birth] date,

  PRIMARY KEY (id)
);


-- Race --

CREATE TABLE race (
  [id] int IDENTITY(1, 1),
  [name] nvarchar(50),
  [category] nvarchar(8),
  [classification] nvarchar(25),
  [country] nvarchar(50),
  [date] date,

  PRIMARY KEY (id)
);

-- Bookmaker --

CREATE TABLE bookmaker (
  [id] int IDENTITY(1, 1),
  [name] nvarchar(50)

  PRIMARY KEY (id)
);

-- Odds --

CREATE TABLE odds (
  [id] int IDENTITY(1, 1),
  [bookmaker_id] int     
	FOREIGN KEY REFERENCES bookmaker([id])
    ON DELETE CASCADE,
  [race_id] int     
	FOREIGN KEY REFERENCES race([id])
    ON DELETE CASCADE,
  [rider_id] int     
	FOREIGN KEY REFERENCES rider([id])
    ON DELETE CASCADE,
  [size] decimal(6,2),
  [datetime] datetime,

  PRIMARY KEY (id)
);

-- Bet --

CREATE TABLE bet (
  [id] int IDENTITY(1, 1),
  [race_id] int
	FOREIGN KEY REFERENCES race([id])
    ON DELETE CASCADE,
  [rider_id] int     
	FOREIGN KEY REFERENCES team([id])
    ON DELETE CASCADE,
  [bookmaker_id] int     
	FOREIGN KEY REFERENCES bookmaker([id])
    ON DELETE CASCADE,
  [datetime] datetime,
  [type] nvarchar(25),
  [status] nvarchar(25),
  [live] BIT, -- 0=prerace / 1=live
  [odds] decimal(6,2),
  [size] decimal(7,2), 
  [profit] decimal(7,2),

  PRIMARY KEY (id)
);

-- rider_bet --

CREATE TABLE rider_bet (
  [rider_id] int
    FOREIGN KEY REFERENCES rider([id])
    ON DELETE CASCADE,
  [bet_id] int
    FOREIGN KEY REFERENCES bet([id])
    ON DELETE CASCADE
);