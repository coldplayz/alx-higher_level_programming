USE hbtn_0d_usa;

INSERT INTO states (name)
VALUES	('California'),
	('Arizona'),
	('Texas'),
	('Utah');

INSERT INTO cities (id, state_id, name)
VALUES	(1, 1, 'San Francisco'),
	(2, 1, 'San Jose'),
	(4, 2, 'Page'),
	(6, 3, 'Paris'),
	(7, 3, 'Houston'),
	(8, 3, 'Dallas');
