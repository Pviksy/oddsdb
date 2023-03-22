DROP TABLE [rider];
DROP TABLE [team];
DROP TABLE [org];
GO


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
GO


SELECT team.[name] AS Team, rider.id, rider.firstname, rider.lastname, rider.date_of_birth, rider. country FROM [rider] JOIN team ON rider.team_id = team.id

SELECT team.[name], rider.[firstname], rider.[lastname], rider.date_of_birth, rider.height FROM rider JOIN team on rider.team_id = team.id ORDER BY date_of_birth DESC

SELECT * FROM [org]
SELECT * FROM [team]
SELECT * FROM [rider] WHERE team_id = 21801

SELECT org_id FROM team WHERE id = 21801
SELECT team.[name] FROM team WHERE id = 